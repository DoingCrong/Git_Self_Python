from flask import Flask, render_template, request, redirect

import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/csv", methods=['GET', 'POST'])
def csv():
    rows = []
    x = []
    y = []
    if request.method == 'POST':
        file = request.files['csv']
        area = str(request.form['area'].strip()) 
        
        if file:
            df = pd.read_csv(file, encoding='UTF-8')
            
            data = df.to_dict(orient='records')

            for row in data:
                if area in row:
                    rows.append({'날짜': row['날짜'],
                                 area: row[area]})
                    x.append(row['날짜'])
                    y.append(row[area])

                x.reverse()
                y.reverse()
                rows.reverse()

            # 1. 데이터를 숫자로 변환 (시간을 인덱스 0, 1, 2...로 변환)
            # X: [0, 1, 2, ..., 데이터개수-1]
            X = np.array(range(len(x))).reshape(-1, 1) 
            Y = np.array(y).reshape(-1, 1)

            """
            range(len(x)): 선형 회귀는 '날짜'라는 텍스트를 이해하지 못합니다. 따라서 첫 번째 달을 0, 두 번째 달을 1로 치환하는 **순서(인덱스)**가 필요합니다. range(len(x))는 0부터 데이터 개수-1까지의 숫자를 생성합니다.

            np.array(...): 파이썬의 기본 리스트는 수학적 연산(행렬 계산)에 적합하지 않습니다. 고속 연산을 위해 넘파이(NumPy) 배열로 변환하는 과정입니다.

            .reshape(-1, 1) (가장 중요):

            사이킷런의 LinearRegression은 데이터를 "행렬(Matrix)" 구조로 받습니다.

            1차원 리스트는 [0, 1, 2]와 같이 '값의 나열'이지만, 모델은 이를 N행 1열의 2차원 형태([[0], [1], [2]])로 요구합니다.

            -1은 "행의 개수는 데이터에 맞게 자동으로 맞춰라"라는 뜻이고, 1은 "열은 딱 하나(특성 하나)"라는 뜻입니다.
            """

            # 2. 모델 학습
            model = LinearRegression()
            model.fit(X, Y)

            """
            LinearRegression(): 오차 제곱합을 최소화하는 직선($y = wx + b$)을 찾기 위한 객체를 생성합니다.
            model.fit(X, Y): 실제 학습 단계입니다.컴퓨터는 $X$와 $Y$의 관계를 보고 가장 최적의 **기울기($w$)**와 **절편($b$)**을 계산합니다.
            """

            # 3. 다음 달 예측 (데이터 개수번째 인덱스)
            next_idx = np.array([[len(x)]])
            prediction = model.predict(next_idx)

            """
            next_idx = np.array([[len(x)]]):만약 데이터가 36개(0~35)라면, 다음 달은 36번 인덱스가 됩니다.
            len(x)는 데이터의 총 개수이므로, 바로 다음 달의 순서가 됩니다.마찬가지로 2차원 배열 형태로 넘겨주어야 하므로 
            [[len(x)]]로 감싸서 행렬로 만듭니다.
            model.predict(next_idx): 학습된 공식($y = wx + b$)에 $x=36$을 대입하여 결과를 계산합니다.
            결과값은 항상 배열 형태로 반환되므로 prediction[0][0]을 통해 실제 숫자값만 추출합니다.
            """
            
            # 예측값을 템플릿으로 전달
            return render_template("csv.html", rows=rows, x=x, y=y, 
                                   area=area, prediction=round(prediction[0][0], 2))
    
    return render_template("csv.html", rows=rows)

if __name__=="__main__":
    app.run(debug=True)