import urllib.request
import json

url = "https://jsonplaceholder.typicode.com/todos/1"

try:
    with urllib.request.urlopen(url) as response:

        raw_data = response.read().decode('utf-8')

        # แปลงข้อความ JSON ให้กลายเป็น Dictionary ใน Python เพื่อให้ใช้งานง่าย
        data = json.loads(raw_data)

        print("=== ดึงข้อมูลสำเร็จ ===")
        print(f"ชื่อเรื่อง: {data['title']}")
        print(f"สถานะ: {data['completed']}")

except Exception as e:
    print(f"เกิดข้อผิดพลาดในการดึงข้อมูล: {e}")