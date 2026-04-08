from db import db_connect
from flask import Flask,render_template,request
from flask import redirect,url_for,session

app = Flask(__name__)
app.secret_key = "abc1234"

@app.route("/")
def index():
    return redirect(url_for("main"))

@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/join" , methods=["GET","POST"])
def join():
    if request.method == "POST":
        user_id = request.form["id"].strip()
        user_pw = request.form["password"].strip()
        user_name = request.form["name"].strip()
        user_email = request.form["email"].strip()
        user_phone = request.form["phone"].strip()
        user_address = request.form["address"].strip()
        user_gender = request.form["gender"].strip()
        user_birth = request.form["birth"].strip()
        user_hobby = request.form["hobby"].strip()
        user_memo = request.form["memo"].strip()

        conn = db_connect()
        cur = conn.cursor()
        sql = """insert into users(id,password,name,email,phone,address,gender,birth,hobby,memo)
                values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        cur.execute(sql,(user_id,user_pw,user_name,user_email,user_phone,user_address,user_gender,user_birth,user_hobby,user_memo))
        conn.commit()
        cur.close()
        conn.close()
        if user_id:
            session["user_id"] = user_id
            return redirect(url_for("joincheck"))
    return render_template("join.html")

@app.route("/joincheck")
def joincheck():
    if "user_id" not in session:
        return redirect(url_for("join"))
    return render_template("joincheck.html" , user_id=session["user_id"])

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        user_id = request.form["id"].strip()
        user_pw = request.form["password"].strip()

        conn = db_connect()
        cur = conn.cursor()
        sql = "select * from users where id=%s and password=%s"
        cur.execute(sql,(user_id,user_pw))
        user = cur.fetchone()
        cur.close()
        conn.close()
        if user:
            session["user_id"] = user["id"]
            return redirect(url_for("logincheck"))
        else:
            return render_template("login.html",msg="아이디 또는 비밀번호 오류")
    return render_template("login.html")

@app.route("/logincheck")
def logincheck():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("logincheck.html" , user_id=session["user_id"])

@app.route("/logout")
def logout():
    session.pop("user_id",None)
    return redirect(url_for("login"))

@app.route("/home")
def home():
    if "user_id" not in session:
        return redirect(url_for("login"))
    else:
        user_id = session["user_id"]
    return render_template("home.html" , user_id=user_id)

if __name__ == "__main__":
    app.run(debug=True) 