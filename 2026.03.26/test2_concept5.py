"""
가게 물품 판매관리 프로그램 작성

프로그램 설명

한 가게에서 여러 종류의 물품을 판매하려고 한다.
판매 물품은 식품과 전자제품 2가지 종류로 관리한다.

모든 물품은 공통적으로 다음 정보(부모클래스)
상품코드
상품명
가격
재고수량



1. 식품 상품(자식 클래스)

식품은 다음 정보를 추가로 가진다.

유통기한
할인율(%)

식품 판매 시 결제금액은 아래와 같이 계산한다.

결제금액 = 가격 * 수량
할인금액 = 결제금액 * 할인율 / 100
최종금액 = 결제금액 - 할인금액
전자제품 상품

2. 전자제품(자식 클래스)

보증기간(개월)
배송비

전자제품 판매 시 결제금액은 아래와 같이 계산한다.

결제금액 = 가격 * 수량 + 배송비

메뉴 구성
프로그램은 while 반복문으로 계속 실행되며 다음 메뉴를 가진다.

메뉴
1. 식품 등록
2. 전자제품 등록
3. 전체 상품 조회
4. 한 상품 조회
5. 상품 판매
6. 재고 추가
7. 상품 삭제
8. 종료

조건
모든 상품은 리스트에 저장한다.
공통 정보와 기능은 부모 클래스에 작성한다.
식품과 전자제품은 자식 클래스로 작성한다.
출력 메서드는 자식 클래스에서 오버라이딩한다.
메뉴는 while + match 문으로 처리한다.
판매 시 재고가 부족하면 판매되지 않도록 한다.

2. 프로그램 설명
클래스 구조
부모 클래스 : Product

공통 정보

상품코드
상품명
가격
재고수량

공통 기능

재고 추가

판매

기본 출력


자식 클래스 1 : FoodProduct

추가 정보

유통기한
할인율

기능
할인 적용 결제금액 계산
출력 메서드 오버라이딩


자식 클래스 2 : ElectronicProduct

추가 정보

보증기간
배송비

기능
배송비 포함 결제금액 계산
출력 메서드 오버라이딩
"""
# 부모클래스
class Product:
    def __init__(self, product, product_code, product_price, product_count, product_term, product_cost):
        self.product = product
        self.product_code = product_code
        self.product_price = product_price
        self.product_count = product_count
        self.product_term = product_term
        self.product_cost = product_cost

    def display(self):
        print(f"상품명 : {self.product} / 코드 : {self.product_code} / 가격 : {self.product_price} / 재고 : {self.product_count}")

# 자식클래스 : food
class FoodProduct(Product):
    def __init__(self, product, product_code, product_price, product_count, product_term, product_cost):
        super().__init__(product, product_code, product_price, product_count, product_term, product_cost)

    def calculate_payment(self, count):
        payment = self.product_price * count
        discount = payment * self.product_cost / 100
        return int(payment - discount)

    #오버라이딩
    def display(self):
        print(f"상품명 : {self.product} / 코드 : {self.product_code} / 가격 : {self.product_price} / 재고 : {self.product_count}")
        print(f" 유통기한 : {self.product_term} / 할인율 : {self.product_cost}%")

# 자식클래스 : elc
class ElectronicProduct(Product):
    def __init__(self, product, product_code, product_price, product_count, product_term, product_cost):
        super().__init__(product, product_code, product_price, product_count, product_term, product_cost)

    def calculate_payment(self, count):
        return (self.product_price * count) + self.product_cost

    #오버라이딩
    def display(self):
        print(f"상품명 : {self.product} / 코드 : {self.product_code} / 가격 : {self.product_price} / 재고 : {self.product_count}")
        print(f" 보증기간 : {self.product_term}개월 / 배송비 : {self.product_cost}원")

# 리스트
box = []

# 상품 판매
def sell():
    code = input("판매하실 상품코드 입력 : ")
    for i in box:
        if i.product_code == code:
            count = int(input("판매하실 상품개수 입력 : "))
            if i.product_count >= count:
                total = i.calculate_payment(count)
                i.product_count -= count
                print(f"상품이름 : {i.product} / 판매개수 : {count} / 총가격 : {total}")
            else:
                print("상품개수가 부족합니다.")
            return
    print("상품코드를 잘 확인해주세요.")

# 재고 추가
def add_count():
    code = input("추가하실 상품코드 입력 : ")
    for i in box:
        if i.product_code == code:
            count = int(input("추가하실 상품개수 입력 : "))
            i.product_count += count
            print(f"상품이름 : {i.product} / 현재재고 : {i.product_count}")
            return
    print("상품코드를 잘 확인해주세요.")

# 한 상품 조회
def selectByCode():
    code = input("검색하실 상품코드 입력 : ")
    for i in box:
        if i.product_code == code:
            i.display()
            return
    print("해당 상품이 없습니다.")

# 전체 상품 조회
def selectAll():
    for i in box:
        i.display()

# 상품 삭제
def delete_product():
    code = input("삭제하실 상품코드 입력 : ")
    for i in box:
        if i.product_code == code:
            box.remove(i)
            print("삭제가 완료되었습니다.")
            return
    print("해당 상품코드를 찾을 수 없습니다.")

# --- 메인 루프 ---
while True:
    print("\n===== 메뉴 =====")
    print("1. 식품 등록")
    print("2. 전자제품 등록")
    print("3. 전체 상품 조회")
    print("4. 한 상품 조회")
    print("5. 상품 판매")
    print("6. 재고 추가")
    print("7. 상품 삭제")
    print("0. 종료")
    print("================")

    menu = int(input("\n입력 : "))

    match menu:
        case 1:
            product_code = input("상품코드 : ")

            product = input("상품명 : ")
            product_price = int(input("상품가격 : "))
            product_count = int(input("재고수량 : "))
            product_term = input("유통기한 : ")
            product_cost = int(input("할인율(%) : "))

            f = FoodProduct(product, product_code, product_price, product_count, product_term, product_cost)
            box.append(f)
            
        case 2:
            product_code = input("상품코드 : ")
            
            product = input("상품명 : ")
            product_price = int(input("상품가격 : "))
            product_count = int(input("재고수량 : "))
            product_term = int(input("보증기간(개월) : "))
            product_cost = int(input("배송비 : "))

            e = ElectronicProduct(product, product_code, product_price, product_count, product_term, product_cost)
            box.append(e)

        case 3:
            selectAll()

        case 4:
            selectByCode()

        case 5:
            sell()

        case 6:
            add_count()

        case 7:
            delete_product()

        case 0:
            print("프로그램을 종료합니다.")
            break
        case _:
            print("그건 할 수 없어요")
            break