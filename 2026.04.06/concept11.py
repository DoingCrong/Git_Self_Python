"""
scikit-learn 은 파이썬 기반 머신러닝 라이브러리로,
데이터 분석과 예측 모델을 쉽게 만들 수 있도록 도와주는 도구
설치 : pip install scikit-learn 또는 python -m pip install scikit-learn
사용 : from sklearn.linear_model import LogisticRegression

머신런닝 기본 : 데이터 준비 -> 모델 선택 -> 학습 -> 예측

LinearRegression() : 숫자를 예측할 때 사용
선형 회귀 분석 : 입력값 X 와 결과값 y 사이를 직선 관계로 보고, 가장 잘 맞는 직선을 찾아 예측합니다. 
예) 공부시간과 점수사이의 관계, 평수와 집값, 광고비와 매출관계 (결과가 숫자일때 주로 사용)


LogisticRegression() : 분류(종류)를 예측할 때 사용합니다.
예) 합격/불합격, 구매함/구매안함, 예방접종 함/예방접종 안함 (결과가 종류일때 주로 사용)

ex)
# 1. 라이브러리 import
from sklearn.linear_model import LinearRegression

# 입력 데이터: 공부시간
X = [[1], [2], [3], [4], [5]] #입력 데이터 변수는 주로 X 대문자를 사용한다.

# 결과 데이터: 시험점수
y = [50, 60, 70, 80, 90] #결과 데이터는 주로 소문자 y를 사용

# 모델 생성
model = LinearRegression()

# 학습
model.fit(X, y)

# 기울기와 절편 확인
print("기울기:", model.coef_) #입력값이 결과에 얼마나 영향을 주는지 보여줌
print("절편:", model.intercept_) #x값이 0일때 y값

#점수 게산 : 40 + 10 * 공부시간

k = int(input("공부시간 입력 : "))

# 예측
print(f"{k}시간 공부 점수 예측:", model.predict([[k]]))

print(model.score(X,y)) #1에 가까울수록 잘 맞는 모델로 인식함.


print("-"*50)
from sklearn.linear_model import LogisticRegression

# 입력 데이터: 공부시간
X = [[1], [2], [3], [4], [5], [6]]

# 결과 데이터: 불합격(0), 합격(1)
y = [0, 0, 0, 1, 1, 1]

# 모델 생성
model = LogisticRegression()

# 학습
model.fit(X, y)

# 예측
# print("3시간 공부:", model.predict([[3]])) #분석 결과
# print("5시간 공부:", model.predict([[5]]))
print(f"{k}시간 공부:", model.predict([[k]]))


# 확률 확인
# print("3시간 공부 확률:", model.predict_proba([[3]]))#3시간 공부 확률: [[0.63650301 0.36349699]] 클래스가 0일 확률이 약 63%, 클래스가 1일 확률이 약 30%
# print("5시간 공부 확률:", model.predict_proba([[5]]))#5시간 공부 확률: [[0.15694029 0.84305971]] 클래스가 0일 확률이 약 15%, 클래스가 1일 확률이 약 84%
print(f"{k}시간 공부 확률:", model.predict_proba([[k]]))


데이터의 정확도를 확인 하기 위해서는 원 자료를 불리하여 확인 절차가 필요하다.
보통 원 자료를 학습용과 테스트용으로 분리를 하는데 8:2, 7:3정도로 분리하여 테스트를 수행한다.
데이터를 분리 : 실습용(훈련 데이터)과 테스트용(검증 데이터)을 나누어서 모델이 새로운 데이터에도 잘 맞는지 확인하는 방법 
데이터를 분리  이유 : 모든 데이터를 한 번에 학습하면 모델이 과적합 발생
Train(훈련) : 모델 학습, Test(테스트) : 성능 평가
흐름 분석 : 데이터 준비 -> Train/Test 분리 (보통 8:2, 7:3) -> 모델 학습(Train) -> 예측 수행(Test) -> 정확도 평가
라이브러리 : from sklearn.model_selection 
            import train_test_split

ex1)
# 라이브러리
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 한글 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
# 1. 데이터 준비
X = np.array([[1],[2],[3],[4],[5],[6],[7],[8]]) #공부시간
y = np.array([50,55,65,70,75,85,90,95]) # 점수

# 2. 데이터 분리 (훈련: 70%, 테스트: 30%)
X_train, X_test, y_train, y_test = train_test_split( #X_train : 공부시간 일부, y_test : 공부 시간에 대한 실제 점수, X_test : 모델이 처음 보는 데이터(시험 문제), y_test(정답-비교용)
    X, y, test_size=0.3, random_state=0  #X : 시간, y : 점수, test_size=0.3 : 테스트 비율 30%, random_state=0 : 데이터를 섞는 기준(랜덤 고정값) - 동일값을 주면 항상 같은 방식
                                        #randoM_state :  없으면 실행할때 마다 다른 결과로 변경
)

# 3. 모델 생성
model = LinearRegression()

# 4. 학습 (훈련 데이터만 사용)
model.fit(X_train, y_train) #반드시 훈련 데이터만 사용 해야함.

# 5. 테스트 데이터로 예측
y_pred = model.predict(X_test) #반드시 테스트용 데이터를 넣어야함

# 6. 결과 출력
print("테스트 입력:", X_test)
print("실제 값:", y_test)
print("예측 값:", y_pred)

# 7. 그래프 출력
plt.scatter(X_train, y_train, label="Train 데이터")
plt.scatter(X_test, y_test, color='red', label="Test 데이터")

plt.plot(X, model.predict(X), color='green', label="회귀선")

plt.legend()
plt.title("선형 회귀 - Train/Test 분리")
plt.xlabel("공부시간")
plt.ylabel("시험점수")
plt.show()

ex2)
import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. CSV 파일 읽기
df = pd.read_csv("score.csv")

# 2. 데이터 확인
print("데이터 확인")
print(df)

# 3. X, y 분리
X = df[["시간"]]   # 반드시 2차원
y = df["점수"]

# 4. 모델 생성
model = LinearRegression()

# 5. 학습
model.fit(X, y)

# 6. 기울기, 절편 출력
print("\n기울기:", model.coef_[0])
print("절편:", model.intercept_)

# 7. 사용자 입력
while True:
    try:
        study_time = float(input("\n공부시간 입력 (종료: q): "))
        
        # 8. 예측
        result = model.predict([[study_time]])
        
        print(f" 예상 점수: {result[0]:.2f}점")
        
    except:
        print("프로그램 종료")
        break
"""

# 라이브러리
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 한글 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
# 1. 데이터 준비
X = np.array([[1],[2],[3],[4],[5],[6],[7],[8]]) #공부시간
y = np.array([50,55,65,70,75,85,90,95]) # 점수

# 2. 데이터 분리 (훈련: 70%, 테스트: 30%)
X_train, X_test, y_train, y_test = train_test_split( #X_train : 공부시간 일부, y_test : 공부 시간에 대한 실제 점수, X_test : 모델이 처음 보는 데이터(시험 문제), y_test(정답-비교용)
    X, y, test_size=0.3, random_state=1  #X : 시간, y : 점수, test_size=0.3 : 테스트 비율 30%, random_state=0 : 데이터를 섞는 기준(랜덤 고정값) - 동일값을 주면 항상 같은 방식
                                        #randoM_state :  없으면 실행할때 마다 다른 결과로 변경
)

# 3. 모델 생성
model = LinearRegression()

# 4. 학습 (훈련 데이터만 사용)
model.fit(X_train, y_train) #반드시 훈련 데이터만 사용 해야함.

# 5. 테스트 데이터로 예측
y_pred = model.predict(X_test) #반드시 테스트용 데이터를 넣어야함

# 6. 결과 출력
print("테스트 입력:", X_test)
print("실제 값:", y_test)
print("예측 값:", y_pred)

# 7. 그래프 출력
plt.scatter(X_train, y_train, label="Train 데이터")
plt.scatter(X_test, y_test, color='red', label="Test 데이터")

plt.plot(X, model.predict(X), color='green', label="회귀선")

plt.legend()
plt.title("선형 회귀 - Train/Test 분리")
plt.xlabel("공부시간")
plt.ylabel("시험점수")
plt.show()
