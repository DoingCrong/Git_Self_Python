import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

def load_data():
    df = pd.read_csv("C:/Users/1Class_015/Desktop/LEEHONGJUNE/Python/Git_Self_Python/2026.04.16/textmining4/HMM3.csv")
    
    return df

@app.route("/")
def home():
    return render_template("index.html", x=[], y=[])

@app.route("/index", methods=['GET', 'POST'])
def index():
    df = load_data()

    x = df['년도'].tolist()[::-1]
    y = df['자산총계'].tolist()[::-1]

    return render_template("result.html", df=df, x=x, y=y)


if __name__=="__main__":
    app.run(debug=True)