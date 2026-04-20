from flask import Flask, render_template, request
import os #운영체제 관련 기능
import sys #경로관련 라이브러리
import webbrowser #프로그램 실행 시 웹브라우저 자동 실행

def resource_path(re_path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path,re_path)


template_dir = resource_path("templates")

app = Flask(__name__,template_folder=template_dir)

@app.route("/", methods=['GET', 'POST'])
def index():
    num1=""
    num2=""
    op=""
    result=""

    if request.method=='POST':
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        op=request.form['op']

        match op:
            case "+":
                result=num1+num2
            case "-":
                result=num1-num2
            case "*":
                result=num1*num2
            case "/":
                result=num1/num2

    return render_template("index.html", num1=num1, num2=num2, op=op, result=result)

if __name__=="__main__":
    webbrowser.open("http://127.0.0.1:5000")
    app.run()