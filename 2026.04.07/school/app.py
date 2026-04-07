from flask import Flask, render_template, request

app = Flask(__name__)

#home
@app.route('/')
def index():
    return render_template('index.html')

#insert
@app.route('/insert', methods=['POST'])
def insert():

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