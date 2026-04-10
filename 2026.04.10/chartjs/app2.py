from flask import Flask, render_template, request, url_for, redirect, session

#라우터 생성
app = Flask(__name__)

@app.route("/")
def home():
    return """
        <h2> 성적 입력 </h2>
        <form action="/chart" method="POST">
            국어 : <input type="number" name="kor"> <br>
            영어 : <input type="number" name="eng"> <br>
            수학 : <input type="number" name="math"> <br>
            <input type="submit" value="그래프출력">
            <input type="reset" value="취소">
        </form>
    """

@app.route("/chart", methods=['POST'])
def chart():
    kor = int(request.form['kor'].strip())
    eng = int(request.form['eng'].strip())
    math = int(request.form['math'].strip())

    total = kor+eng+math
    average = round(total/3,2)

    return render_template("chart5.html",
                           kor=kor,
                           eng=eng,
                           math=math,
                           total=total,
                           average=average
                           )

#라우터 구동
if __name__ == "__main__":
    app.run(debug=True)