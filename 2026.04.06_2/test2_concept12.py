from flask import Flask

app = Flask(__name__) #웹 앱 생성

@app.route("/user/<name>") #스프링에서 rquesetMapping 이랑 비슷함 / 값을 전달받아서 대입
def hello(name):
    return f"{name}님 환영 합니다."

#처음에 Not Found
#주소창뒤에 /user/이름

@app.route('/abc')
def abc():
    return f"라우터 연습"

if __name__ == "__main__":
    app.run()