from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

cals = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/input", methods=['POST'])
def input():
    data = request.get_json()
    if not data:
        return jsonify({
            "status":"error",
            "message":"Json Data Check"
        }), 400
    
    num1 = int(data.get("num1"))
    num2 = int(data.get("num2"))
    op = data.get("op")

    match op:
        case "+":
            result = num1+num2
        case "-":
            result = num1-num2
        case "*":
            result = num1*num2
        case "/":
            result = num1/num2

    cal = {
        "num1":num1,
        "num2":num2,
        "op":op,
        "result":result
    }

    cals.append(cal)

    return jsonify({
        "status":"success",
        "message":"Json Data Save Complete",
        "cal":cal
    })

if __name__=="__main__":
    app.run(debug=True)