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

클래스 사용하여 작성해주세요
"""
class Box:
    def __init__(self, product_code, product_count):
        self.product_code = product_code
        self.product_count = product_count

        self.cal_pay = self.cal_pay()
        self.total_pay = self.total_pay()

    def cal_pay(self):
        match self.product_code:
            case 1:
                return 4500*self.product_count
            case 2:
                return 5000*self.product_count
            case 3:
                return 5500*self.product_count
            case 4:
                return 6000*self.product_count
            
    def total_pay(self):
        total=0
        for i in purchase:
            total+=i["현재금액"]

    def dic(self):
        return {
            "상품이름" : self.product_code,
            "상품개수" : self.product_count,
            "현재금액" : self.cal_pay
        }
    def dic2(self):
        return {
            "총금액" : self.total_pay
        }

# 1. 상품주문
def order_input():
    print("1. 라면 / 4500")
    print("2. 국수 / 5000")
    print("3. 쫄면 / 5500")
    print("4. 짜장면 / 6000")

    product_code = int(input("\n코드 : "))
    product_count = int(input("갯수 : "))
    
    b = Box(product_code, product_count)
    purchase.append(b.dic())

    print(f"{product_code}번 음식 / {product_count}개 / {b.cal_pay}원")

# 2. 주문내역조회
def order_list():
    if not purchase:
        print("====주문하신 내역이 없습니다.====")
        return

    for i in purchase:
        print(f"{i["상품이름"]}번 음식 / {i["상품개수"]}개 / {i["현재금액"]}원")

# 3. 총결제금액조회 
def order_pay():
    if not purchase:
        print("====주문하신 내역이 없습니다.====")
        return
    
    for i in purchase:
        print(f"{i["총금액"]}")

def menu():
    print("1. 상품주문")
    print("2. 주문내역조회")
    print("3. 총 결제금액 조회")
    print("0. 종료")

purchase = []

while True:
    menu()

    choice = int(input("\n입력 : "))

    match choice:
        case 1:
            order_input()
        case 2:
            order_list()
        case 3:
            order_pay()
        case 0:
            break
        case _:
            print("그건 할 수 없어요")
            break
