from flask import Flask, render_template, request
from flask import redirect, url_for, session

app = Flask(__name__)

#index
@app.route("/")
def index():
    return redirect(url_for("chart"))

#chart
@app.route("/chart")
def chart():
    return render_template("chart1.html")

if __name__ == "__main__":
    app.run(debug=True)