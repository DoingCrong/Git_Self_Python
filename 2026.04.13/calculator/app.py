from flask import Flask, render_template, request, redirect
from db import get_connection

app = Flask(__name__)


# home
@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "GET":
        return render_template("index.html")

    num1 = int(request.form['num1'].strip())
    num2 = int(request.form['num2'].strip())

    total = num1 + num2
    sub = num1 - num2
    mult = num1 * num2
    avg = round(total / 2, 2)

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    insert into calculator
    (num1, num2, total, sub, mult, avge)
    values(%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (num1, num2, total, sub, mult, avg))
    conn.commit()

    # .close
    cursor.close()
    conn.close()

    labels = ["합", "차", "곱", "평균"]  # 수정: 깨진 차트 라벨 복구
    values = [total, sub, mult, avg]

    return render_template(
        "chart.html",
        num1=num1,
        num2=num2,
        total=total,
        sub=sub,
        mult=mult,
        avg=avg,
        labels=labels,
        values=values
    )


@app.route("/history")
def history():
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    select * from calculator
    order by id desc
    """
    cursor.execute(sql)
    rows = cursor.fetchall()

    # .close
    cursor.close()
    conn.close()

    return render_template("index.html", rows=rows)


@app.route("/avg_chart")
def avg_chart():
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    select id, avge from calculator
    """
    cursor.execute(sql)
    rows = cursor.fetchall()

    # .close
    cursor.close()
    conn.close()

    # 수정: id와 avge를 각각 리스트로 분리
    labels = []
    values = []

    for row in rows:
        labels.append(f"ID{row['id']}")
        values.append(row['avge'])

    return render_template("avg_chart.html", labels=labels, values=values, rows=rows)  # 수정: 템플릿 파일명 복구


if __name__ == "__main__":
    app.run(debug=True)
