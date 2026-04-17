"""
비밀번호 암호화 로그인 예제
설치 : pip install flask bcrypt pymysql
"""

from flask import Flask, render_template, request, redirect, url_for, session
import bcrypt
from db import get_connection

app = Flask(__name__)

# session 사용을 위한 secret key
app.secret_key = "abcd1234"


# -----------------------------
# 회원가입
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def register():
    message = ""

    if request.method == "POST":
        user_id = request.form["user_id"].strip()
        user_pw = request.form["user_pw"].strip()

        if user_id == "" or user_pw == "":
            message = "아이디와 비밀번호를 모두 입력해주세요."
            return render_template("index.html", message=message)

        # 비밀번호 암호화
        hashed_pw = bcrypt.hashpw(
            user_pw.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        conn = get_connection()
        cursor = conn.cursor()

        sql = "INSERT INTO users (user_id, user_pw) VALUES (%s, %s)"
        cursor.execute(sql, (user_id, hashed_pw))
        conn.commit()

        cursor.close()
        conn.close()

        message = "회원가입이 완료되었습니다."

    return render_template("index.html", message=message)


# -----------------------------
# 로그인
# -----------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""

    if request.method == "POST":
        user_id = request.form["user_id"].strip()
        user_pw = request.form["user_pw"].strip()

        conn = get_connection()
        cursor = conn.cursor()

        sql = "SELECT * FROM users WHERE user_id = %s"
        cursor.execute(sql, (user_id,))
        row = cursor.fetchone()

        cursor.close()
        conn.close()

        if row:
            if bcrypt.checkpw(
                user_pw.encode("utf-8"), #내가 입력한 pw -> utf8로 인코딩
                row["user_pw"].encode("utf-8") #데이터베이스에 있는 pw -> utf8로 인코딩
            ):
                session["user_id"] = row["user_id"]
                return redirect(url_for("success"))
            else:
                message = "비밀번호가 틀립니다."
        else:
            message = "존재하지 않는 아이디입니다."

    return render_template("login.html", message=message)


# -----------------------------
# 로그인 성공 페이지
# -----------------------------
@app.route("/success")
def success():
    if "user_id" not in session:
        return redirect(url_for("login"))

    return render_template("success.html", user_id=session["user_id"])


# -----------------------------
# 로그아웃
# -----------------------------
@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)