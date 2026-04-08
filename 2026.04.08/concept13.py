"""
---------------------------------------------------------------------------------------------------------------
===================================================== < Flask, render_template, request, redirect, url_for, session  > ================================================
---------------------------------------------------------------------------------------------------------------

from db import  get_connection 
#외부 파일에서 함수를 호출
from flask import Flask, render_template, request
# Flask : flask에서 사용하는 모든 명령어 사용
# render_template : html화면을 출력
# request : html from에서 전송 받은 값을 받아올때 사용
from flask import redirect, url_for, session
# redirect : 다른 웹 페이지 주소 이동
# url_for : 주소를 만들어 줌
# session : 로그인 상태를 유지(웹 페이지에서)

app = Flask(__name__)
app.secret_key = "abc1234" 
# app.secret_key : session을 사용하려면 반드시 필요함. 값은 사용자가 마음대료

@app.route("/")
def index():
    return redirect(url_for("login")) # #페이지를 이동하여 주소창에 주소 표시 함.
            #@app.route("/login")호출 하는 구문
    # return render_template("login.html") #페이지는 고정이고 화면만 이동.

# -------------------------------------------------
# 로그인 처리
# methods=["GET", "POST"]
# GET  : 페이지 처음 열 때
# POST : 사용자가 아이디/비밀번호 입력 후 전송할 때
# -------------------------------------------------
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        user_id = request.form["id"].strip()
        user_pw = request.form["password"].strip()

        conn = get_connection()
        cur = conn.cursor()

        sql = "select * from users where id=%s and password=%s"
        cur.execute(sql, (user_id, user_pw))

        user = cur.fetchone()

        cur.close()
        conn.close()

        # user 값이 있으면 로그인 성공
        if user:
            # 세션에 로그인한 사용자 아이디 저장
            # 브라우저가 켜져 있는 동안 로그인 상태 유지 가능
            session["user_id"] = user["id"]

            # 로그인 성공 후 home 페이지로 이동
            return redirect(url_for("home"))

        # user 값이 없으면 로그인 실패
        else:
            # login.html 다시 보여주면서 에러 메시지도 함께 전달
            return render_template("login.html", msg="아이디 또는 비밀번호오류")

    # GET 방식일 경우
    # 즉, 처음 /login 페이지에 접속했을 때 로그인 화면 출력
    return render_template("login.html")


# -------------------------------------------------
# 메인 페이지
# 로그인한 사용자만 접근 가능하게 처리
# -------------------------------------------------
@app.route("/home")
def home():

    # 세션에 user_id가 없으면 로그인 안 한 상태
    if "user_id" not in session:
        # 로그인 페이지로 강제 이동
        return redirect(url_for("login"))

    # 로그인 상태라면 home.html 화면 출력
    # user_id 값을 html로 넘겨줌
    return render_template("home.html", user_id=session["user_id"])


if __name__ == "__main__":
    app.run(debug=True)
    # debug=True : 서버 다시 실행, 오류 발생 구문 확인 가능
"""