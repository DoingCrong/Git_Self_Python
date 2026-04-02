import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def menu():
    print("\n=== 선택창 ===")
    print("1. 식자재\n" \
          "2. 가전제품\n" \
          "3. 여행물품\n" \
          "4. 기타\n" \
          "5. 조회\n" \
          "6. 그래프출력\n" \
          "0. 종료\n")

def menu2():
    print("\n==== 입력창 ====")
    if choice == 1:
        name = "식자재"
    elif choice == 2:
        name = "가전제품"
    elif choice == 3:
        name = "여행물품"
    elif choice == 4:
        name = "기타"
    else:
        print("그건 할 수 없어요")

    try:
        count = int(input("수량 : "))
        cost = int(input("단가 : "))
        money = count * cost

        select = {
        "물품명": name,
        "수량": count,
        "단가": cost,
        "금액": money,
        }
        
        print(f"{count}개 * {cost}원 = {money}원")
        return count, cost, money
        
    except ValueError:
        print("숫자만 입력 가능합니다.")
        return None
    
def combination():
    select = menu2()
    if select:
        name, count, cost, money = select
        product.append([name, count, cost, money])

def selectAll():
    print("\n=== 전체 조회 ===")
    print("상품명\t수량\t단가\t금액")
    for i in product:
        print(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}")

def graph():
    name = [i[0] for i in product]
    sum = [i[3] for i in product]

    plt.bar(name, sum)
    plt.title("물품별 그래프 합계")
    plt.xlabel("물품명")
    plt.ylabel("합계")
    plt.show()

product = []

while True:
    menu()

    choice = int(input("입력 : "))

    match choice:
        case 0:
            break
        case 1:
            combination()
        case 2:
            combination()
        case 3:
            combination()
        case 4:
            combination()
        case 5:
            selectAll()
        case 6:
            graph()
        