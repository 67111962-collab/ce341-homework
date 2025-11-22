from flask import Flask, render_template

app = Flask(__name__)

# 1. หน้า Home ("/")
@app.route('/')
def home():
    # ข้อมูลนักศึกษา (แก้ไขตรงนี้)
    student_info = {
        "name": "นาย ภาสวิชญ์ สุขสุเมฆ",
        "id": "67xxx962", 
        "image_url": "https://raw.githubusercontent.com/67111962-collab/ce341-homework/main/S__27656194.jpg" # ใส่ URL รูปตัวเองจริงที่นี่
    }
    return render_template('index.html', info=student_info)

# 2. หน้า Git ("/git")
@app.route('/git')
def git_page():
    return render_template('git.html')

# 3. หน้า Docker ("/docker")
@app.route('/docker')
def docker_page():
    return render_template('docker.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
