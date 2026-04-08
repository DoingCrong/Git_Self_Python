from db import get_connection
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "member1234"

@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uid = request.form["id"].strip()
        upw = request.form["password"].strip()
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("select * from members where id=%s and password=%s", (uid, upw))
        user = cur.fetchone()
        cur.close()
        conn.close()
        if user:
            session["user_id"] = user["id"]
            session["user_name"] = user["name"] if "name" in user else uid
            return redirect(url_for("home"))
        return render_template("login.html", msg="아이디 또는 비밀번호가 틀렸습니다.")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = {
            "id":       request.form["id"].strip(),
            "password": request.form["password"].strip(),
            "phone":    request.form["phone"].strip(),
            "birth":    request.form["birth"].strip(),
            "address":  request.form["address"].strip(),
            "hobby":    request.form["hobby"].strip(),
            "gender":   request.form["gender"].strip(),
            "note":     request.form["note"].strip(),
        }
        conn = get_connection()
        cur = conn.cursor()
        sql = """insert into members(id,password,phone,birth,address,hobby,gender,note)
                 values(%s,%s,%s,%s,%s,%s,%s,%s)"""
        cur.execute(sql, tuple(data.values()))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/home")
def home():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("home.html", user_id=session["user_id"])

@app.route("/list")
def member_list():
    if "user_id" not in session:
        return redirect(url_for("login"))
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("select * from members")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("list.html", rows=rows)

@app.route("/edit/<id>")
def edit(id):
    if "user_id" not in session:
        return redirect(url_for("login"))
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("select * from members where id=%s", (id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return render_template("edit.html", row=row)

@app.route("/update", methods=["POST"])
def update():
    data = (
        request.form["password"].strip(),
        request.form["phone"].strip(),
        request.form["birth"].strip(),
        request.form["address"].strip(),
        request.form["hobby"].strip(),
        request.form["gender"].strip(),
        request.form["note"].strip(),
        request.form["id"].strip(),
    )
    conn = get_connection()
    cur = conn.cursor()
    sql = """update members set password=%s,phone=%s,birth=%s,
             address=%s,hobby=%s,gender=%s,note=%s where id=%s"""
    cur.execute(sql, data)
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for("member_list"))

@app.route("/delete/<id>")
def delete(id):
    if "user_id" not in session:
        return redirect(url_for("login"))
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("delete from members where id=%s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for("member_list"))

if __name__ == "__main__":
    app.run(debug=True)
