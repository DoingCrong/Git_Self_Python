from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

students = [] #성적 데이터를 저장할 리스트, 전역변수로 사용하여 사용하기 쉽게

@app.route("/")
def home():
    return """
        <h2>Json을 이용한 성적 처리</h2>
        <hr>
        차트 확인 : <a href='/chart'>chart</a>
    """

@app.route("/input", methods=['POST'])
def input():
    data = request.get_json() #포스트맨에서 json 데이터를 받아 처리
    if not data:
        return jsonify({
            "status":"오류",
            "message":"JSON 데이터를 입력해주세요."
        }), 400
    
    name = data.get("name")
    kor = data.get("kor")
    eng = data.get("eng")
    math = data.get("math")

    total = kor+eng+math
    avg = total/3

    student = {
        "name":name,
        "kor":kor,
        "eng":eng,
        "math":math,
        "total":total,
        "avg":avg
    }

    students.append(student)

    return jsonify({
        "status":"success",
        "message":"성적 저장 및 처리 완료",
        "student":student
    })

@app.route("/chart")
def chart():
    names = [student["name"] for student in students] #students안에 있는 이름 전체 저장
    totals = [student["total"] for student in students] #students안에 있는 total 전체 저장
    #전체학생수 : len(totals)
    #전체평균 : total_avg = 전체총합(for문돌려서) / len(totals)

    return render_template("chart.html", names=names, totals=totals)

if __name__=="__main__":
    app.run(debug=True)