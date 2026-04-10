from flask import Flask, render_template, request, redirect, url_for, session
import numpy as np
import pandas as pd

from db import get_connection

app = Flask(__name__)

app.secret_key="1234"

#home
@app.route("/")
def home():
    return redirect(url_for("input"))

#input
@app.route("/input", methods=['POST', 'GET'])
def input():
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.form['name'].strip()
        kor = int(request.form['kor'].strip())
        eng = int(request.form['eng'].strip())
        math = int(request.form['math'].strip())

        total = kor+eng+math
        average = round(total/3,2)

        if average>=90:
            grade="A"
        elif average>=80:
            grade="B"
        elif average>=70:
            grade="C"
        elif average>=60:
            grade="D"
        else:
            grade="F"

        sql = """
        insert into student
        (name, kor, eng, math, total, average, grade)
        values(%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql,(name, kor, eng, math, total, average, grade))
        conn.commit()

        #방금 입력된 ID가져오기
        #cursor.lastrowid
        id = cursor.lastrowid

        sql2 = """
        select * from student
        where id=%s
        """
        cursor.execute(sql2,(id,))
        row = cursor.fetchone()
        
        #.close
        conn.close()
        cursor.close()

        return render_template("inputOk.html", row=row)

    return render_template("input.html")

#chart
@app.route("/chart")
def chart():

    name = []
    avg = []

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    select * from student
    """
    cursor.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
        name.append(row['name'])
        avg.append(row['average'])

    #.close
    conn.close()
    cursor.close()

    return render_template("chart.html", name=name, avg=avg)

#selectAll
@app.route("/selectAll")
def selectAll():
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    select * from student
    order by id
    """
    cursor.execute(sql)
    rows = cursor.fetchall()

    #.close
    cursor.close()
    conn.close()

    return render_template("selectAll.html", rows=rows)

if __name__=="__main__":
    app.run(debug=True)