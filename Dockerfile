# ใช้ Python Image เป็นฐาน
FROM python:3.9-slim

# กำหนด Folder ทำงาน
WORKDIR /app

# Copy ไฟล์ requirements มาลงก่อน
COPY requirements.txt .

# Install Library ที่จำเป็น
RUN pip install --no-cache-dir -r requirements.txt

# Copy โค้ดทั้งหมดเข้าไปใน Image
COPY . .

# เปิด Port 80
EXPOSE 80

# คำสั่งเมื่อ Container เริ่มทำงาน
CMD ["python", "app.py"]
