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
    name = request.form['name'].strip()
    kor = int(request.form['kor'].strip())
    eng = int(request.form['eng'].strip())
    math = int(request.form['math'].strip())

    if name=="" or kor==""or eng==""or math=="":
        return "모든값을 입력하세요. <a href="/">돌아가기</a>" 
    #값이 비어있으면 돌아가는 구문
    #굳이 작성하기 싫으면 html에서 input구문에 required작성

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

    #Mysql DB에 값대입(insert)
    sql = "insert into student(name, kor, eng, math, total, avg, grade)" \
          "values(%s, %s, %s, %s, %s, %s, %s)"
    
    #cursor로 execute(insert, update, delete에서만)
    #conn으로 commit
    cursor.execute(sql,(name, kor, eng, math, total, avg, grade))
    conn.commit()

    #Mysql selectAll
    #기존에는 자료가 적어서 일일이 던지면 됬는데 자료가 100개면 100개를 던질수 없으니까
    #하나의 변수에 담아서 던진 후 result.html로 for문을 돌려 출력하려는 내용
    cursor = conn.cursor(pymysql.cursors.DictCursor) #데이터 베이스에 들어있는 값을
                                                    #딕셔너리로 변경하여 저장
    sql = "select * from student"
    cursor.execute(sql)
    rows = cursor.fetchall() #하나면 row = cursor.fetchone()


    #.close
    cursor.close()
    conn.close()

    return render_template('result.html', rows=rows
                        #기존방식
                        # name=name, 
                        # kor=kor,
                        # eng=eng,
                        # math=math,
                        # total=total,
                        # avg=avg,
                        # grade=grade
                        )

if __name__ == '__main__':
    app.run(debug=True)