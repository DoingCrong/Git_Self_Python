from flask import Flask, render_template, request
#render_template : html파일 좌표 찍으려면 필요
#request : html파일에서 받은 값들을 가져오려면 필요

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/abc")
def abc():
    return render_template("a.html")

@app.route("/result", methods=["post"]) #action에서 post방식으로 전송?받기?때문에 methods는 post로..?
def result():
    # num1 = request.form["num1"] #a.html에서 name=''으로 선언된 값 받아오기 
    # num2 = request.form["num2"] #python에서는 값의 형태는 자동으로 맞춰줌 / java에서는 직접 맞추었어야함
                                #지금 이렇게 받으면 그냥 문자열 더하기로 10+10=1010 이상태로 출력
                                #형변환 해주어서 넣어줘야함
    num1 = int(request.form["num1"])
    num2 = int(request.form["num2"])
    op = request.form["op"]

    match op:
        case "+":
            kk = num1+num2
        case "-":
            kk = num1-num2
        case "*":
            kk = num1*num2
        case "/":
            kk = num1/num2

    # result.html로 값4개 전송
    return render_template("result.html", 
                           num1=num1, 
                           num2=num2,
                           op=op,
                           result=kk
                           )

if __name__ == "__main__":
    app.run(debug=True)