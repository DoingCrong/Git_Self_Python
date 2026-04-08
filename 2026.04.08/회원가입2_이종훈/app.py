from db import get_connection
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "abc1234"

@app.route("/")
def index():
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = (
            request.form["id"],
            request.form["password"],
            request.form["phone"],
            request.form["birth"],
            request.form["address"],
            request.form["hobby"],
            request.form["gender"],
            request.form["memo"]
        )

        conn = get_connection()
        cur = conn.cursor()

        sql = """
        insert into users(id, password, phone, birth, address, hobby, gender, memo)
        values(%s,%s,%s,%s,%s,%s,%s,%s)
        """
        cur.execute(sql, data)
        conn.commit()

        cur.close()
        conn.close()

        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_id = request.form["id"]
        user_pw = request.form["password"]

        conn = get_connection()
        cur = conn.cursor()

        sql = "select * from users where id=%s and password=%s"
        cur.execute(sql, (user_id, user_pw))

        user = cur.fetchone()

        cur.close()
        conn.close()

        if user:
            session["user_id"] = user["id"]
            return redirect(url_for("home"))
        else:
            return render_template("login.html", msg="아이디 또는 비밀번호 오류")

    return render_template("login.html")


@app.route("/home")
def home():
    if "user_id" not in session:
        return redirect(url_for("login"))

    return render_template("home.html", user_id=session["user_id"])


@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)