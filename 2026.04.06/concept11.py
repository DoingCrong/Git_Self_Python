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


"""
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
