from flask import Flask, render_template # render_template 꼭 해야함

app = Flask(__name__) #웹 앱 생성

@app.route("/")
def home():
    return render_template("test.html")

if __name__ == "__main__":
    app.run()