from flask import Flask, render_template, request
import cv2, easyocr
import os #경로 지정 라이브러리

app = Flask(__name__)

#현재 app.py 파일이 있는 폴더 지정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#static 폴더 경로 지정(절대경로)
UPLOAD_FOLDER = os.path.join(BASE_DIR, "static")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

#static 폴더가 없으면 자동 생성하는 구문
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

#ocr 객체 생성
reader = easyocr.Reader(['ko', 'en'], gpu=True)

#시작 라우터 생성
@app.route("/", methods=['POST', 'GET'])
def home():
    result_text=[]
    if request.method=='POST':
        if "file" not in request.files:
            return "파일을 선택 해야 합니다."
        
        #html에서 action으로 받은게 아니기 때문에 form이 아니라 files
        file = request.files['file']

        #업로드 파일 위치 저장
        filepath = os.path.join(app.config["UPLOAD_FOLDER"],"abc.png")
        #파일 저장
        file.save(filepath)

        #이미지 읽기
        img = cv2.imread(filepath)

        #흑백변환
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #OCR 수행
        result = reader.readtext(gray)
        for r in result:
            result_text.append(r[1])

    return render_template("index.html", results = result_text)

if __name__=="__main__":
    app.run(debug=True)