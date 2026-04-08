from db import get_connection

from flask import Flask, render_template, request
from flask import redirect, url_for, session

#라우터
app = Flask(__name__)

#session
app.secret_key = "1234"

#home
@app.route("/")
def home():
    return redirect(url_for("menu"))

#menu
@app.route("/menu", methods=['POST', "GET"])
def menu():
    if request.method == "POST":
        choice = int(request.form["choice"])

        match choice:
            case 1:
                if request.method=='POST':
                    return redirect(url_for("join"))
                return render_template("join.html")
            case 2:
                return redirect(url_for("login"))
            case 3:
                return selectAll()
            # case 4:
            #     if request.method==['POST']:
            #         return redirect(url_for("update"))
            #     return render_template("update.html")
            # case 5:
            #     return redirect(url_for("delete"))

    # id = session.get('id')

    # if id is None:
    #     msg = "로그아웃상태"
    #     return msg
    # else:
    #     msg = id
    #     return msg

    return render_template("menu.html")

#join
@app.route("/join", methods=['POST', 'GET'])
def join():
    if request.method == "POST":
        id = request.form['id'].strip()
        password = request.form['password'].strip()
        phone = request.form['phone'].strip()
        age = request.form['age'].strip()
        address = request.form['address'].strip()
        hobby = request.form['hobby'].strip()
        sex = request.form['sex'].strip()
        etc = request.form['etc'].strip()

        conn = get_connection()
        cursor = conn.cursor()

        if id=="" or password=="" or phone=="" or sex=="":
            return "id, password, phone, sex는 필수 항목입니다. <a href='/'>[ 다시돌아가기 ]</a>"

        sql = """
        insert into info
        (id, password, phone, age, address, hobby, sex, etc)
        values(%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql,(id,password,phone,age,address,hobby,sex,etc))
        conn.commit()

        #.close
        conn.close()
        cursor.close()

    return render_template("/menu.html")

#login
@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        id = request.form["id"].strip()
        password = request.form["password"].strip()

        conn = get_connection()
        cursor = conn.cursor()

        check_sql = """
        select * from info
        where id=%s and password=%s
        """
        cursor.execute(check_sql,(id,password))

        row = cursor.fetchone()

        #.close()
        cursor.close()
        conn.close()

        if row:
            session['id'] = row['id']
            return redirect(url_for("loginOk"))
        
        else:
            msg = "아이디 또는 비밀번호 오류 <a href='/'>[ 돌아가기 ]</a>"
            return msg
    
    return render_template("login.html")

#loginOk + selectById역할도 수행
@app.route("/loginOk", methods=['POST', 'GET'])
def loginOk():

    id = session['id']
    #password = session['password']

    conn = get_connection()
    cursor = conn.cursor()

    check_sql = """
    select * from info
    where id=%s
    """
    cursor.execute(check_sql,(id))
    row = cursor.fetchone()

    #.close
    cursor.close()
    conn.close()

    if "id" not in session:
        return redirect(url_for("login"))

    return render_template("loginOk.html", id=session['id'], row=row)

#logout
@app.route("/logout", methods=['POST', 'GET'])
def logout():
    session.pop("id", None)

    return redirect(url_for("login"))

#selectAll
@app.route("/selectAll")
def selectAll():
    #if request.method=='POST':
    conn = get_connection()
    cursor = conn.cursor()

    sql ="""
    select * from info
    """

    cursor.execute(sql)
    rows = cursor.fetchall()

    #.close
    cursor.close()
    conn.close()

    return render_template("selectAll.html", rows=rows)

#update
@app.route("/update", methods=['POST', 'GET'])
def update():
    if "id" not in session:
        return redirect(url_for("login"))

    id = session['id']
    conn = get_connection()
    cursor = conn.cursor()

    #POST방식
    if request.method == 'POST':
        password = request.form['password'].strip()
        phone = request.form['phone'].strip()
        age = request.form['age'].strip()
        address = request.form['address'].strip()
        hobby = request.form['hobby']
        sex = request.form['sex'].strip()
        etc = request.form['etc'].strip()

        sql = """
        update info
        set password=%s, phone=%s, age=%s, address=%s, hobby=%s, sex=%s, etc=%s
        where id=%s
        """
        cursor.execute(sql, (password, phone, age, address, hobby, sex, etc, id))
        conn.commit() 
        
        #.close
        cursor.close()
        conn.close()
        return redirect(url_for("loginOk")) 

    #GET방식
    check_sql = "select * from info where id=%s"
    cursor.execute(check_sql, (id,))
    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if row is None:
        return "해당 데이터가 존재하지 않습니다. <a href='/'>메뉴로 돌아가기</a>"

    return render_template("update.html", row=row)

#delete
@app.route("/delete", methods=['POST', 'GET'])
def delete():
    if "id" not in session:
        return redirect(url_for("login"))

    id = session['id']

    #POST방식
    if request.method == "POST":
        conn = get_connection()
        cursor = conn.cursor()

        try:
            sql = "delete from info where id = %s"
            cursor.execute(sql, (id,))
            conn.commit()

            session.pop("id", None)
            
            cursor.close()
            conn.close()
            
            return "회원탈퇴 완료! <a href='/'>[ 돌아가기 ]</a>"
        
        except Exception as e:
            return f"{e} <a href='/'>[ 돌아가기 ]</a>"

    return render_template("delete.html", id=id)

if __name__=="__main__":
    app.run(debug=True)