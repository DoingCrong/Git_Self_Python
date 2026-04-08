from db import get_connection # 외부 파일에서 함수를 호출하는 방법
                               # db파이썬에서 get_connection(db연결구문)함수 호출

from flask import Flask, render_template, request
# Flask : flask에서 사용하는 모든 명령어 사용
# render_template : html화면을 출력할때 사용 (주소이동이 아님, 화면만 바뀜)
# request : html form에서 전송 받은 값을 받아올때 사용

# 신규추가
from flask import redirect, url_for, session
# redirect : 다른 웹 페이지 주소 이동
# url_for : 주소를 생성(만들어줌)
# session : 로그인 상태를 유지(웹 페이지에서)

app = Flask(__name__) # 라우터 만드는 용도

# session을 만드는 과정
app.secret_key = "abc1234" 
# app.secret_key : session을 만드려면(사용) 반드시 필요함. 값은 사용자가 마음대로 정의
# 이걸 사용하면 컴퓨터?가 session을 쓴다는것을 인지

#home
@app.route("/")
def index():
    # 기존방식: return render_template("login.html")
    #           return render_template("처음가려는화면.html")
    # render_template은 주소창에 html페이지(라우터)가 잡히질 않음
    
    # 새로운 방식: redirect(url_for("라우터이름"))를 사용하여 주소를 변경해줌
    return redirect(url_for("login")) # login이라는 라우터를 호출

# -------------------------------------------------------------
# 로그인 처리
# methods=['POST', 'GET'] : 전송방식이 애매하면 둘 다 작성
# GET : 페이지 처음 열 때 / POST : 아이디, 비번 입력 후 전송 시
# -------------------------------------------------------------

# 30라인 : return redirect(url_for("login"))에서 login이라는 라우터를 호출(왜 여기로 가는가? : 나중에 이유 나옴)
"""
◎ 기본개념
redirect의 역할: 서버가 브라우저에게 특정 주소(/login)로 다시 접속하라고 명령하여, 해당 경로의 함수(login())를 처음부터 다시 실행하게 만드는 방아쇠 역할을 합니다.

함수 실행 방식: 호출된 login() 함수는 접속 방식(Method)에 따라 GET 방식이면 로그인 화면(render_template)을 보여주고, POST 방식이면 입력받은 데이터로 로그인 처리를 수행합니다.

데이터 흐름: 사용자가 입력한 데이터는 HTML의 <form> 태그를 통해 login() 함수로 전달되며, 서버는 이때 request.form을 사용하여 해당 값을 받아와 DB와 비교합니다.

◎ 추가추가
**redirect(url_for("login"))**은 서버가 브라우저에 /login으로 접속하라는 명령을 내려 login() 함수를 GET 방식으로 호출하게 만드는 방아쇠입니다.

호출된 login() 함수는 내부에서 GET 방식이면 마지막 줄의 render_template("login.html")을 실행해 로그인 화면을 출력합니다.

이후 사용자가 데이터를 입력하면 POST 방식으로 동일한 함수가 다시 실행되어, request.form으로 값을 받아 DB와 비교하는 로그인 처리를 수행합니다.
"""
# 89라인에서도 호출(89라인은 로그인 실패했을때 다시 가는 용도)
@app.route("/login", methods=["GET", "POST"])
def login():

    # 전송방식이 POST방식일 때만 수행 (사용자가 로그인 버튼 눌렀을 때)
    if request.method == "POST":
        # login.html에서 받아온 값을 변수에 저장 (.strip()으로 공백 제거)
        user_id = request.form["id"].strip()
        user_pw = request.form["password"].strip()

        # db 연결구문
        conn = get_connection()
        cur = conn.cursor()

        # 실제 로그인 비교를 위해 db에 있는 값 땡겨와서 체크
        check_sql = "select * from users where id=%s and password=%s"
        cur.execute(check_sql, (user_id, user_pw))

        user = cur.fetchone() # 한 사람의 정보를 변수에 저장(db에 있는)

        # .close()
        cur.close()
        conn.close()

        # 로그인 성공 (db에 있는 값과 입력한 값이 같아서 user 객체가 존재할 때)
        if user:
            # 세션에 로그인한 사용자 아이디 저장 (브라우저 켜져 있는 동안 유지)
            session["id"] = user["id"]

            # 로그인 성공 후 home이라는 라우터 호출
            return redirect(url_for("home"))

        # 로그인 실패 (user 값이 없을 때)
        #elif user is None:
        else:
            # 에러 메시지와 함께 다시 로그인 화면 보여줌
            msg = "아이디 또는 비밀번호 오류 <a href='/'>[ 돌아가기 ]</a>"
            return msg
            #return "입력된 값이 없습니다. <a href="/">[ 돌아가기 ]</a>"

    # GET 방식일 경우 
    # 즉, (처음 /login 페이지에 접속했을 때) 로그인 화면 출력
    return render_template("login.html")


# -------------------------------------------------
# 메인 페이지
# -------------------------------------------------
# 69라인 : return redirect(url_for("home"))에서 home이라는 라우터 호출
@app.route("/home")
def home():

    # 로그인이 안됐다면(세션에 id가 없으면) login 라우터로 이동
    # 정확도를 위한 이중 방지용
    if "id" not in session:
        return redirect(url_for("login"))

    # 로그인 성공 시 render_template으로 html에 값 전달 용도
    # user_id 값을 html로 넘겨줌
    return render_template("home.html", id=session["id"])


# 서버가 구동하려면 좌표(진입점) 지정해준다
if __name__ == "__main__":
    app.run(debug=True)
    # debug=True : 기존에는 수정 후 서버를 재시작해야 했으나, 
    # 이제는 수정 시 서버 자동 재실행 및 오류 발생 구문 확인 가능