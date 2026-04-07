from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/insert", methods=["POST"])
def insert():
    name = request.form["name"]
    tall = float(request.form["tall"])
    weight = float(request.form["weight"])

    tall_m = tall * 0.01
    bmi = round(weight / (tall_m * tall_m), 2)

    if bmi < 18.5:
        result = "저체중"
    elif bmi < 23:
        result = "정상"
    elif bmi < 25:
        result = "과체중"
    elif bmi < 30:
        result = "비만"
    else:
        result = "고도비만"

    return render_template(
        "result.html",
        name=name,
        tall=tall,
        weight=weight,
        bmi=bmi,
        result=result,
    )


if __name__ == "__main__":
    app.run(debug=True)
