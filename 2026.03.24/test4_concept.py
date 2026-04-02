"""
상품 목록이 다음과 같을 때, 주문 프로그램을 작성하세요.

상품 정보

1 : 라면 / 4500
2 : 국수 / 5000
3 : 쫄면 / 5500
4 : 짜장면 / 6000

기능

상품 주문
주문 내역 조회
총 결제금액 조회
종료

조건

상품 정보는 딕셔너리 사용
주문 내역은 리스트에 저장
주문 시 상품명, 수량, 금액 저장
함수 사용
"""
#딕셔너리 상품  등록
products = {
    1: {"상품명": "라면", "단가": 4500},
    2: {"상품명": "국수", "단가": 5000},
    3: {"상품명": "쫄면", "단가": 5500},
    4: {"상품명": "짜장면", "단가": 6000}
}

#상품관련 조회
def show_products():
    print("상품코드 상품명 단가")
    for code, info in products.items():
        print(code, info["상품명"], info["단가"])

#주문
def order_product(order_list):
    show_products()
    code = int(input("상품코드 입력 : "))

    if code not in products:
        print("존재하지 않는 상품입니다.")
        return

    qty = int(input("수량 입력 : "))
    name = products[code]["상품명"]
    price = products[code]["단가"]
    amount = price * qty

    order = {
        "상품명": name,
        "수량": qty,
        "금액": amount
    }

    order_list.append(order)
    print("주문 완료")

#주문내역
def show_orders(order_list):
    if len(order_list) == 0:
        print("주문 내역이 없습니다.")
        return

    print("상품명 수량 금액")
    for order in order_list:
        print(order["상품명"], order["수량"], order["금액"])

#상품 주문 금액
def total_amount(order_list):
    total = 0
    for order in order_list:
        total += order["금액"]
    return total


orders = []

while True:
    print("\n===== 상품 주문 관리 =====")
    print("1. 상품 주문")
    print("2. 주문 내역 조회")
    print("3. 총 결제금액 조회")
    print("4. 종료")

    menu = input("메뉴 선택 : ")

    if menu == "1":
        order_product(orders)
    elif menu == "2":
        show_orders(orders)
    elif menu == "3":
        print("총 결제금액 :", total_amount(orders))
    elif menu == "4":
        print("프로그램 종료")
        break
    else:
        print("잘못 입력했습니다.")