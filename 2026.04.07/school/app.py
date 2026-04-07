from flask import Flask, render_template, request
import pymysql

#flask 객체 생성

app = Flask(__name__)

#db연동함수 생성
def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        database="flaskdb",
        charset="utf8"
    )

#home
@app.route('/')
def index():
    return render_template('index.html')

#insert
@app.route('/insert', methods=['POST'])
def insert():

    #db 연결 변수 생성
    conn = get_connection()
    cursor = conn.cursor()

    #index.html에서 받아온 값
    name = request.form['name']
    kor = int(request.form['kor'])
    eng = int(request.form['eng'])
    math = int(request.form['math'])

    total = kor+eng+math
    avg = float(total/3)

    if avg >= 90:
        grade = 'A'
    elif avg >= 80:
        grade = 'B'
    elif avg >= 70:
        grade = 'C'
    elif avg >= 60:
        grade = 'D'
    else:
        grade = 'F'

    #Mysql DB에 값대입
    sql = "insert into student(name, kor, eng, math, total, avg, grade)" \
          "values(%s, %s, %s, %s, %s, %s, %s)"
    
    #cursor로 execute(insert, update, delete에서만)
    #conn으로 commit
    cursor.execute(sql,(name, kor, eng, math, total, avg, grade))
    conn.commit()

    #.close
    cursor.close()
    conn.close()

    return render_template('result.html',
                        name=name,
                        kor=kor,
                        eng=eng,
                        math=math,
                        total=total,
                        avg=avg,
                        grade=grade)

if __name__ == '__main__':
    app.run(debug=True)