from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

#db연동함수 생성
def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        database="selfdb",
        charset="utf8"
    )

#home
@app.route('/')
def home():
    return render_template("menu.html")

@app.route('/menu', methods=['POST'])
def menu():

    select = int(request.form['select'].strip())

    match select:
        case 1:
            return render_template("insert.html")
        case 2:
            return selectAll()#render_template("selectAll.html")
        case 3:
            return render_template("selectById.html")
        case 4:
            return render_template("updateById.html")
        
@app.route('/insert', methods=['POST'])
def insert():

    #db 연결 변수 생성
    conn = get_connection()
    cursor = conn.cursor()

    name = request.form['name'].strip()
    kor = int(request.form['kor'].strip())
    eng = int(request.form['eng'].strip())
    math = int(request.form['math'].strip())

    if name=="" or kor==""or eng==""or math=="":
        return "모든값을 입력하세요. <a href="/">돌아가기</a>" 

    total = kor+eng+math
    average = round(total/3,2)

    if average>=90:
        grade = "A"
    elif average>=80:
        grade = "B"
    elif average>=70:
        grade = "C"
    elif average>=60:
        grade = "D"
    else:
        grade = "F"

    sql = """
    insert into student(name, kor, eng, math, total, average, grade)
    values(%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql,(name, kor, eng, math, total, average, grade))
    conn.commit()

    #.close
    conn.close()
    cursor.close()

    return render_template("/menu.html")

@app.route('/selectAll')#받을건 없긴한데 혹시나
def selectAll():
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor) #조회부분에서는 python-html 할때 그냥 딕셔너리 로 던져라?
                                                     #어 왜그런지는 잘 모르겠음
                                                     #조회하는부분에서는 반드시 써야 (딕셔너리 형태로) 조회가 가능함

    sql = """
    select * from student
    """
    cursor.execute(sql)
    rows = cursor.fetchall()

    #.close()
    conn.close()
    cursor.close()

    return render_template("selectAll.html", rows=rows)

@app.route('/selectById', methods=['POST', 'GET'])
def selectById():
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    id = int(request.form['id'].strip())

    sql = """
    select * from student
    where id=%s
    """
    cursor.execute(sql,(id,))

    row = cursor.fetchone()

    if row is None:
        return "해당 데이터가 존재 하지 않습니다. <a href='/'>메뉴로돌아가기</a>"
    
    #.close
    conn.close()
    cursor.close()

    return render_template("selectOne.html", row= row)

@app.route('/updateById', methods=['POST', 'GET'])
def updateById():
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    id = int(request.form['id'].strip())

    check_sql = """
    select * from student
    where id=%s
    """
    cursor.execute(check_sql,(id,))

    #id None값 체크용도
    row2 = cursor.fetchone()

    if row2 is None:
        return "해당 데이터가 존재 하지 않습니다. <a href='/'>메뉴로돌아가기</a>"
    
    return render_template("update.html", row2=row2)


@app.route('/update', methods=['POST', 'GET'])
def update():

    conn = get_connection()
    cursor = conn.cursor()

    #update된 값
    kor = int(request.form['kor'].strip())
    eng = int(request.form['eng'].strip())
    math = int(request.form['math'].strip())

    total = kor+eng+math
    average = round(total/3,2)

    if average>=90:
        grade = "A"
    elif average>=80:
        grade = "B"
    elif average>=70:
        grade = "C"
    elif average>=60:
        grade = "D"
    else:
        grade = "F"

    sql = """
    update student
    set kor=%s, eng=%s, math=%s, total=%s, average=%s, grade=%s
    where id=%s
    """
    cursor.execute(sql, (kor, eng, math, total, average, grade, id))
    conn.commit()

    #업데이트 후 데이터
    row = cursor.fetchone()

    #.close
    conn.close()
    cursor.close()

    return render_template("selectOne.html", row=row, row2=row2)

if __name__ == '__main__':
    app.run(debug=True)