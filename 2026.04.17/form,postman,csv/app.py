from flask import Flask, render_template, request, redirect, session, url_for
from flask import jsonify
import bcrypt
from db import get_connection
import pandas as pd

app = Flask(__name__)

app.secret_key = "1234"

#total 함수(리턴값으로)
def total_cal(kor, eng, math):
    return kor + eng + math

#avg함수
def avg_cal(total):
    return round(total / 3, 2)

#grade함수
def grade_cal(avg):
    if avg >= 90: 
        return "A"
    elif avg >= 80: 
        return "B"
    elif avg >= 70: 
        return "C"
    else: 
        return "F"


# 1번,2번,3번 선택지 부모인자로 만들어야겠
@app.route("/")
def index():
    return render_template("index.html")

# 1. form에서 받는
@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method=='POST':
        student_no = request.form['student_no'].strip()
        password = request.form['password'].strip()
        name = request.form['name'].strip()

        kor = int(request.form['kor'].strip())
        eng = int(request.form['eng'].strip())
        math = int(request.form['math'].strip())

        #total, avg, grade함수 호출+변수에 저장
        #쓰려는 함수명과 변수명 똑같이 만들면 안됨
        total = total_cal(kor, eng, math)
        avg = avg_cal(total)
        grade = grade_cal(avg)

        # 비밀번호 암호화
        hashed_pw = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        #db연결
        conn = get_connection()
        cursor = conn.cursor()

        #sql insert
        sql = """
        insert into students
        (student_no, password, name, kor, eng, math, total, avg, grade)
        values(%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql,(student_no, hashed_pw, name, kor, eng, math, total, avg, grade))
        conn.commit()

        #방금 회원가입한놈 정보 끌고오기
        sql2 = "select * from students where student_no = %s"
        cursor.execute(sql2, (student_no,)) 
        rows = cursor.fetchone() 

        #.close
        cursor.close()
        conn.close()

        return render_template("form.html", rows=rows)
    
    return render_template("form.html")

#포스트맨에서만 쓰는 리스트
schools = []

# 2. 포스트맨(json) 받는
@app.route("/postman", methods=['GET', 'POST'])
def postman():
    if request.method=='POST':
        #postman에서 받아오기?
        data = request.get_json()

        if not data:
            return jsonify({
                "status":"error",
                "message":"Json Data Check"
            }), 400
        
        #포스트맨에서 전달한 변수와 받은변수 통일
        student_no = data.get("student_no")
        password = data.get("password")
        name = data.get("name")

        kor = int(data.get("kor"))
        eng = int(data.get("eng"))
        math = int(data.get("math"))

        #total, avg, grade함수 호출+변수에 저장
        #쓰려는 함수명과 변수명 똑같이 만들면 안됨
        total = total_cal(kor, eng, math)
        avg = avg_cal(total)
        grade = grade_cal(avg)

        # 비밀번호 암호화
        hashed_pw = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        #딕셔너리 형태로 저장
        school = {
            "student_no":student_no,
            "password":hashed_pw,
            "name":name,
            "kor":kor,
            "eng":eng,
            "math":math,
            "total":total,
            "avg":avg,
            "grade":grade
        }

        #딕셔너리 append
        schools.append(school)

        #db연결
        conn = get_connection()
        cursor = conn.cursor()

        #sql insert
        sql = """
        insert into students
        (student_no, password, name, kor, eng, math, total, avg, grade)
        values(%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql,(student_no, hashed_pw, name, kor, eng, math, total, avg, grade))
        conn.commit()

        #.close
        cursor.close()
        conn.close()

        #포스트맨한테 정보 전달
        return jsonify({
            "status":"success",
            "message":"Json Data Save Complete",
            "schools":schools
        })
    
    #sql3용 db연결
    conn = get_connection()
    cursor = conn.cursor()
    
    """
    postman으로 들어왔을때 (post방식일시) 리턴값을 반드시 postman쪽으로만 전달해야해서
    (return jsonify({...}), render_template("postman.html", rows=rows) 두개 리턴 불가능X)
    get방식으로 보내는 형태로
    마지막으로 들어온 mysql값을 꺼내는 방법은
    sql3 = select * from students order by id desc limit 1 -> 내림차순으로 만들고 limit 1 붙이면 되는듯?

    기준점이 될 값이 auto_increment? 이거면 방법이 달라지는거 같은데
    LAST_INSERT_ID() mysql함수?
    last_id = SELECT LAST_INSERT_ID()
    sql3 = "select * from students WHERE student_no = %s"
    cursor.execute(sql3,(last_id,))
    기준점이 되는 값만 뽑혀 나와서 다시 조회 때려서 sql3값을 rows = cursor.fetchone()해라
    """
    sql3 = """
    select * from students 
    order by student_no 
    desc limit 1
    """
    cursor.execute(sql3) 
    rows = cursor.fetchone() 

    #.close
    cursor.close()
    conn.close()

    return render_template("postman.html", rows=rows)
        
# 3. csv파일로 받는
@app.route("/csv", methods=['GET', 'POST'])
def csv():
    rows = [] # 결과를 담을 리스트
    if request.method == 'POST':
        file = request.files['csv']
        if file:
            df = pd.read_csv(file, encoding="utf-8")
            
            conn = get_connection()
            cursor = conn.cursor()
            
            for i in range(len(df)):
                student_no = str(df.loc[i, "student_no"])
                password = str(df.loc[i, "password"])
                name = str(df.loc[i, "name"])
                kor = int(df.loc[i, "kor"])
                eng = int(df.loc[i, "eng"])
                math = int(df.loc[i, "math"])

                total = total_cal(kor, eng, math)
                avg = avg_cal(total)
                grade = grade_cal(avg)

                # 비밀번호 암호화
                hashed_pw = bcrypt.hashpw(
                    password.encode("utf-8"),
                    bcrypt.gensalt()
                ).decode("utf-8")

                sql = """
                insert into students
                (student_no, password, name, kor, eng, math, total, avg, grade)
                values(%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (student_no, hashed_pw, name, kor, eng, math, total, avg, grade))
                
            conn.commit()

            sql2 = "select * from students" 
            cursor.execute(sql2)
            rows = cursor.fetchall() 

            #.close
            cursor.close()
            conn.close()

            return render_template("csv.html", rows=rows)

    return render_template("csv.html")

#chart.js
@app.route("/chart", methods=['GET', 'POST'])
def chart():
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    select * from students
    """
    cursor.execute(sql)
    rows = cursor.fetchall()

    x = [row['name'] for row in rows]
    y = [row['avg'] for row in rows]

    #.close
    cursor.close()
    conn.close()

    return render_template("chart.html", x=x, y=y)

#selectAll
@app.route("/selectAll")
def selectAll():
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    select * from students
    """
    cursor.execute(sql)
    rows = cursor.fetchall()

    return render_template("selectAll.html", rows=rows)

#login
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #login.html에서 값 받아오기
        student_no = request.form.get('student_no')
        password = request.form.get('password')

        #db연결
        conn = get_connection()
        cursor = conn.cursor()
        
        sql = "select * from students where student_no = %s"
        cursor.execute(sql, (student_no,))
        row = cursor.fetchone()

        #session부분 기억안나서 재미나이 돌림
        if row and row['password'] == password:
            session['user_id'] = row['student_no']
            session['user_name'] = row['name']
            
            return render_template("login.html", row=row)
        else:
            return "<script>alert('학번 또는 비밀번호가 틀렸습니다.'); history.back();</script>"

    return render_template("login.html")

#logout
@app.route("/logout")
def logout():
    session.clear() # 세션 초기화
    return redirect(url_for('login'))

#update
@app.route("/update", methods=['GET', 'POST'])
def update():
    conn = get_connection()
    cursor = conn.cursor()
    student_no = session.get('user_id')
    
    # 로그인 안되어있으면 리다이렉트
    if not student_no:
        return redirect(url_for('login')) 

    update = None

    if request.method == 'POST':

        password = request.form.get('password')
        name = request.form.get('name')
        kor = int(request.form.get('kor'))
        eng = int(request.form.get('eng'))
        math = int(request.form.get('math'))

        total = total_cal(kor,eng,math)
        avg = avg_cal(total)
        grade = grade_cal(avg)

        sql_update = """
            update students 
            set password=%s, name=%s, kor=%s, eng=%s, math=%s, total=%s, avg=%s, grade=%s 
            where student_no=%s
        """
        cursor.execute(sql_update, (password, name, kor, eng, math, total, avg, grade, student_no))
        conn.commit()
        
        sql = "select * from students where student_no = %s"
        cursor.execute(sql, (student_no,))
        update = cursor.fetchone()

    #GET방식일때(사실 처음접속하면 거의)
    sql2 = "SELECT * FROM students WHERE student_no = %s"
    cursor.execute(sql2, (student_no,))
    row = cursor.fetchone()
    
    return render_template("update.html", row=row, update=update)

#delete
@app.route("/delete", methods=['GET', 'POST'])
def delete():
    conn = get_connection()
    cursor = conn.cursor()
    student_no = session.get('user_id')
    
    if not student_no:
        return redirect(url_for('login'))

    if request.method == 'POST':
        sql_delete = "DELETE FROM students WHERE student_no = %s"
        cursor.execute(sql_delete, (student_no,))
        conn.commit()
        
        session.clear()
        return "<script>alert('성공적으로 탈퇴되었습니다.'); location.href='/login';</script>"

    # GET 방식일 때
    sql = "SELECT * FROM students WHERE student_no = %s"
    cursor.execute(sql, (student_no,))
    row = cursor.fetchone()
    
    return render_template("delete.html", row=row)


if __name__=="__main__":
    app.run(debug=True)