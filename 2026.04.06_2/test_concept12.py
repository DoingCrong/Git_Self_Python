from flask import Flask

app = Flask(__name__) #웹 앱 생성

@app.route('/') #url 연결 #home좌표
def home():
    return "안녕하세요 플라스크 처음입니다!"

@app.route("/hello") #스프링에서 rquesetMapping 이랑 비슷함 #좌표찍고싶은곳 작성
def hello():
    return "Hello World"

#Not Found
#주소창뒤에 /hello

if __name__ == "__main__":
    app.run()