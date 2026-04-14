from flask import Flask, render_template, request
import cv2, easyocr, re
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "static")
app.config["UPLOAD_FOLDER"]=UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

reader = easyocr.Reader(['ko','en'], gpu=True)

@app.route("/", methods=['GET','POST'])
def index():
    result_num=[]
    names=[]
    if request.method=='POST':
        if "file" not in request.files:
            return "파일좀 선택하세요"
        
        file = request.files['file']

        filepath = os.path.join(app.config["UPLOAD_FOLDER"],"aaa.png")
        file.save(filepath)

        img = cv2.imread(filepath)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        result = reader.readtext(gray)

        for r in result:
            text = r[1]

            number = re.findall(r'\d+',text)
            name = re.findall(r'\s+',text)
            address = re.findall(r'\s+',text)
            email = re.findall(r'\s+',text)

            for i in number:
                result_num.append(int(i))

        names.append(name)

    return render_template("index.html", result_num=result_num, 
                           names=names)

if __name__=="__main__":
    app.run(debug=True)