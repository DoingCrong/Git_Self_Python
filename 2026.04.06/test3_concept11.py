import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# 한글 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

#1. 데이터
X = np.array([20, 30, 40, 60, 80, 100]).reshape(-1, 1)  # 면적(㎡)
y = np.array([1000, 1500, 1800, 2400, 3000, 3600])      # 가격(만원)

#2. 데이터 분리
# 8:2, seed=0
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

# 3. 모델 생성
model = LinearRegression()

#4. 모델 학습
#반드시 트레인(소수) 데이터로
model.fit(X_train, y_train)

#5. 테스트 데이터로 예측
#반드시 테스트(다수) 데이터로
y_pre = model.predict(X_test)

#6. 결과 출력
print("테스트 입력 : ", X_test)
print("실제 값 : ", y_test)
print("예측 값 : ", y_pre)

#7. 그래프 출력
plt.scatter(X_train, y_train, label="Train(시식용)데이터")
plt.scatter(X_test, y_test, color='skyblue', label="Test(진짜)데이터")

plt.plot(X, model.predict(X), color="red", label="회귀선?")

plt.legend()
plt.title("선형회귀 - Train/Test 분리")
plt.xlabel("면적(㎡)")
plt.ylabel("가격(원)")
plt.show()