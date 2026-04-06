from sklearn.linear_model import LinearRegression
import pandas as pd

try:
    time = int(input("학습시간 : "))
except ValueError:
    print("정수만 입력가능")

x = [[0], [1], [2], [3], [4], [5]] #공부시간
y = [10, 30, 50, 60, 70, 75] #점수

model = LinearRegression()

model.fit(x,y)

xx = []
for i in x:
    xx.append(i[0])

print("\n=== 예측 ===")
print(f"{time}시간 공부 : ", model.predict([[time]]))

# print("\n=== 확률 ===")
# print(f"{time}시간 공부 : ", model.predict_proba([[time]]))

xy = pd.DataFrame({
    "공부시간": xx, #[i[0] for i in x]
    "점수": y
})

xy.to_csv("공부시간-점수.csv", index=False, encoding='utf-8-sig')

print(xy)