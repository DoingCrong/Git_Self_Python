from sklearn.linear_model import LinearRegression
import pandas as pd

product = ["키보드", "마우스", "캠", "마우스패드"]
price = [15000, 12000, 25000, 5000]

df = pd.DataFrame({
    "물품" : product,
    "단가" : price
})

print(df)
df.to_csv("물품판매금액예측.csv", index=False, encoding="utf-8-sig")


def menu():
    print("\n=== 사용자 입력 ===")
    name = input("물품명(q/Q입력시 종료) : ").strip().lower()
    
    if name == 'q':
        return name, 0

    try:
        count = int(input("수량 : "))
    except ValueError:
        print("수량은 정수만 입력 가능")
        return None
    
    return name, count

#def test():
    


while True:
    name, count = menu()

    if name == "q":
        print("프로그램을 종료합니다.")
        break

    print(f"\n물품명 : {name} / 수량 : {count}")

    df2 = pd.read_csv("물품판매금액예측.csv", encoding="utf-8")

    df2['수량'] = count
    df2["금액"] = df2["단가"] * df2["수량"]

    #test()

    x = df2["수량"]
    y = df2["금액"]

    model = LinearRegression()

    model.fit(x,y)

    print("원래 금액 : ", df2["금액"])
    print("예상금액 : ", model.predict([[count]]))

    df2.to_csv("물품판매금액예측2.csv", index=False, encoding='utf-8-sig')


