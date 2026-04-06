from flask import Flask, render_template, request

app = Flask(__name__)

#home
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/insert", methods=["post"])
def insert():
    id = request.form["id"]
    password = request.form["password"]
    phone = request.form["phone"]
    age = request.form["age"]
    home = request.form["home"]

    return render_template("result.html",
                           id = id,
                           password = password,
                           phone = phone,
                           age = age,
                           home = home
                           )

if __name__ == "__main__":
    app.run(debug=True)
