import time
import random
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

# =========================================================================
# 1. ฟังก์ชันสแกนเว็บ / ดึงข้อมูล (I/O Bound Task) สำหรับ ThreadPoolExecutor
# =========================================================================
def fetch_web_data(url):
    print(f"[Thread] กำลังเริ่มดึงข้อมูลจาก: {url}")
    # จำลองเวลาในการโหลดข้อมูลจากอินเทอร์เน็ต (0.5 ถึง 1.5 วินาที)
    time.sleep(random.uniform(0.5, 1.5))
    
    # จำลองเคสเกิด Error: ถ้า URL มีคำว่า 'bad-url' ให้สั่งโยน Error (Exception) ออกมา
    if "bad-url" in url:
        raise ConnectionError(f"ไม่สามารถเชื่อมต่อกับเซิร์ฟเวอร์ปลายทางได้: {url}")
        
    print(f"[Thread] ดึงข้อมูลเสร็จสิ้น: {url}")
    return f"ข้อมูลของ {url} (ดาวน์โหลดสำเร็จ)"
# =========================================================================
# 2. ฟังก์ชันคำนวณเลขหนักๆ (CPU Bound Task) สำหรับ ProcessPoolExecutor
# =========================================================================
# หมายเหตุ: ฟังก์ชันที่จะใช้กับ ProcessPool ต้องประกาศอยู่ที่ระดับบนสุด (Top-level) ของไฟล์
# เพื่อให้ระบบสามารถ Copy (Pickle) ไปรันที่ Process อื่นได้
def heavy_calculation(number):
    print(f"[Process] กำลังเริ่มคำนวณตัวเลข: {number}")
    time.sleep(0.8)  # จำลองงานประมวลผลหนักๆ
    
    # จำลองเคสเกิด Error: ถ้าส่งเลขติดลบมา ให้แสดงข้อผิดพลาด
    if number < 0:
        raise ValueError(f"เกิดข้อผิดพลาด! ไม่สามารถคำนวณตัวเลขติดลบได้: {number}")
        
    return number ** 2
# =========================================================================
# ฟังก์ชันหลักแสดงการทำงานแยกตามประเภท
# =========================================================================
def run_thread_pool_example():
    urls = [
        "https://example.com/page1",
        "https://bad-url.com/api/v1",  # ตัวนี้จะเกิด Error
        "https://example.com/page3",
    ]
    
    print("\n=== [วิธีที่ 1] รัน ThreadPoolExecutor + ใช้ as_completed (แนะนำสำหรับจัดการ Error) ===")
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        # สั่งยิงงานทั้งหมดออกไปพร้อมกันแบบ Asynchronous
        # มัดรวม Future Object คู่กับ URL เดิมไว้ใน Dictionary เพื่อใช้อ้างอิงตอน Error
        future_to_url = {executor.submit(fetch_web_data, url): url for url in urls}
        
        # as_completed จะคืนค่า Future ที่ทำงานเสร็จก่อนกลับมา (ใครเสร็จก่อน ได้ 처리 ก่อน ไม่เรียงตามลำดับ)
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                # การดึงผลลัพธ์ด้วย .result() จะเป็นการสั่งให้โยน Exception ออกมาถ้างานนั้นพัง
                result = future.result()
                print(f"[สำเร็จ] ได้รับ -> {result}")
            except ConnectionError as ce:
                print(f"[เกิดข้อผิดพลาด] สำหรับ {url} -> {ce}")
            except Exception as e:
                print(f"[เกิดข้อผิดพลาดทั่วไป] สำหรับ {url} -> {e}")
def run_process_pool_example():
    numbers = [10, 20, -5, 40]  # ตัวเลข -5 จะเกิด Error
    
    print("\n=== [วิธีที่ 2] รัน ProcessPoolExecutor + ใช้ executor.map ===")
    
    with ProcessPoolExecutor(max_workers=2) as executor:
        # executor.map จะส่งผลลัพธ์กลับมาตามลำดับอินพุต (เรียง 10, 20, -5, 40)
        # โดยตัวมันเองจะคืนค่าเป็น Iterator
        results_iterator = executor.map(heavy_calculation, numbers)
        
        # การดักจับ Error ของ .map จะต้องครอบ try-except ไว้ตอนที่ "วนลูปอ่านผลลัพธ์"
        for num in numbers:
            try:
                # ดึงผลลัพธ์ตัวถัดไป ถ้าตัวนั้นเกิด Error มันจะยกมาพ่นตรงนี้ทันที
                result = next(results_iterator)
                print(f"[สำเร็จ] ผลคำนวณของ {num} คือ -> {result}")
            except ValueError as ve:
                print(f"[เกิดข้อผิดพลาด] ของเลข {num} -> {ve}")
            except Exception as e:
                print(f"[เกิดข้อผิดพลาดทั่วไป] ของเลข {num} -> {e}")
if __name__ == "__main__":
    start_time = time.time()
    
    # 1. รันฝั่ง Thread (I/O)
    run_thread_pool_example()
    
    # 2. รันฝั่ง Process (CPU)
    run_process_pool_example()
    
    print(f"\n⏱️ ใช้เวลารวมทั้งหมด: {time.time() - start_time:.2f} วินาที")