from flask import Flask ,request, render_template
import pandas as pd

app = Flask(__name__)

def load_data():
    df = pd.read_csv("아파트.csv")
    
    return df

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/total")
def total():
    df = load_data()

    # if df is None:
    #     return "데이터가 없습니다."
    
    x = df['지역'].tolist()
    y = df['2026년 1월'].tolist()

    return render_template("total.html", df=df, x=x , y=y)

#x축값이 잘 안들어가는듯 함
#y축값이 제대로 들어가는지 모름
@app.route("/monthly", methods=['POST', 'GET'])
def monthly():
    df = load_data()
    y = df['지역'].tolist()
    if request.method=='GET':
        return render_template("monthly.html", y=y)
    
    #문제1. option에서 받은 select값이랑 df안의 '지역'이 같을때 값을 전송해야함
    # select = request.form['select']
    # select = df[df["지역"] == select]

    # #df2=df.drop(df.columns[[0,1]], axis=1)
    # df2=df.drop(df.columns[[0,1]], axis=1)

    # #문제 2. df중 0,1번 열을 짜르고 실수값만 들어있는 상태로 전달하려 했음
    # x = df2.values.tolist()

    # return render_template("monthly.html", select=select)
    return render_template("monthly.html")
    
# @app.route("/new")
# def new():
#     df = load_data()


if __name__=="__main__":
    app.run(debug=True)
