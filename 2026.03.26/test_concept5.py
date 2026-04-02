"""
문제명 : 은행 금융 상품 관리 프로그램 작성

프로그램 설명

은행에서 고객의 금융 상품을 관리하려고 한다.
상품은 적금과 대출 2가지가 있다.

각 상품은 공통적으로(부모클래스)

계좌번호
예금주
비밀번호
금액

정보를 가진다.

하지만 상품 종류에 따라 추가 정보가 다르다.

1. 적금 상품

적금은 다음 정보를 추가로 가진다.

기간(개월)
이율(%)

적금의 만기 예상 금액은 아래와 같이 계산한다.

만기금액 = 원금 + (원금 * 이율/100 * 기간/12)

2. 대출 상품

대출은 다음 정보를 추가로 가진다.

기간(개월)
이율(%)

대출의 총 상환 금액은 아래와 같이 계산한다.

총상환금액 = 대출금 + (대출금 * 이율/100 * 기간/12)

월 상환금액은 아래와 같이 계산한다.

월상환금액 = 총상환금액 / 기간


메뉴 구성

프로그램은 while 반복문으로 계속 실행되며, 아래 메뉴를 제공한다.

메인 메뉴
1. 적금 계좌 생성
2. 대출 계좌 생성
3. 전체 계좌 조회
4. 한 계좌 조회
5. 적금 만기금액 조회
6. 대출 상환정보 조회
7. 입금
8. 출금
9. 계좌 삭제
10. 종료

조건
모든 계좌 정보는 리스트에 저장한다.
공통 정보는 부모 클래스에서 관리한다.
적금과 대출은 자식 클래스로 작성한다.
공통 출력 메서드는 자식 클래스에서 오버라이딩한다.
메뉴 처리는 while + match 문을 사용한다.
비밀번호가 맞을 때만 출금/삭제 가능하도록 한다.

2. 프로그램 설계 설명

클래스 구조

2-1. 부모 클래스 : BankAccount

공통 정보 저장

계좌번호
예금주
비밀번호
금액

공통 기능

입금
출금
기본정보 출력

2-2. 자식 클래스 1 : SavingAccount

적금 전용 클래스

기간
이율
만기금액 계산
출력 메서드 오버라이딩

2-3. 자식 클래스 2 : LoanAccount

대출 전용 클래스

기간
이율
총상환금액 계산
월상환금액 계산
출력 메서드 오버라이딩
"""
#부모클래스
class BankAccount:
    def __init__(self, acc_num, pw, name, money):
        self.acc_num = acc_num
        self.pw = pw
        self.name = name
        self.money = money

    def display(self): 
        print(f"계좌번호 : {self.acc_num}")
        print(f"예금주 : {self.name}")
        print(f"잔액 : {self.money}")

#자식클래스 : 적금
class SavingAccount(BankAccount):
    def __init__(self, acc_num, pw, name, money, term, interest):
        super().__init__(acc_num, pw, name, money)
        self.term = term
        self.interest = interest

    def display(self):
        super().display()
        total = self.money + (self.money * self.interest / 100 * self.term / 12)
        print(f"계좌번호 : {self.acc_num}")
        print(f"예금주 : {self.name}")
        print(f"잔액 : {self.money}")
        print(f"기간 : {self.term}개월 | 이율 : {self.interest}% | 만기금액 : {int(total)}")

#자식클래스 : 대출
class LoanAccount(BankAccount):
    def __init__(self, acc_num, pw, name, money, term, interest):
        super().__init__(acc_num, pw, name, money)
        self.term = term
        self.interest = interest

    def display(self):
        super().display()
        total = self.money + (self.money * self.interest / 100 * self.term / 12)
        monthly = total / self.term
        print(f"계좌번호 : {self.acc_num}")
        print(f"예금주 : {self.name}")
        print(f"잔액 : {self.money}")
        print(f"기간 : {self.term}개월 / 이율 : {self.interest}%")
        print(f"총상환금액 : {int(total)} / 월상환금액 : {int(monthly)}")

#리스트
account = []

# 모든계좌찾기
def selectAll():
    for acc in account:
        print(f"계좌번호 : {acc.acc_num}")
        print(f"예금주 : {acc.name}")
        print(f"잔액 : {acc.money}")

# 한계좌찾기
def selectByAcc():
    search_num = input("계좌번호 입력: ")
    for acc in account:
        if acc.acc_num == search_num:
            pw = input("비밀번호 : ")
            if acc.pw == pw:
                acc.display()

# 적금계좌 만들기
def create_saving():
    acc_num = input("계좌번호 : ")
    for acc in account:
        if acc.acc_num == acc_num:
            print("중복된 계좌번호입니다.")
            return
    pw = input("비밀번호 : ")
    name = input("이름 : ")
    money = int(input("금액 : "))
    term = int(input("기간 : "))
    interest = float(input("이율 : "))
    account.append(SavingAccount(acc_num, pw, name, money, term, interest))

# 대출계좌 만들기
def create_loan():
    acc_num = input("계좌번호 : ")
    for acc in account:
        if acc.acc_num == acc_num:
            print("중복된 계좌번호입니다.")
            return
    pw = input("비밀번호 : ")
    name = input("이름 : ")
    money = int(input("대출금 : "))
    term = int(input("기간 : "))
    interest = float(input("이율 : "))
    account.append(LoanAccount(acc_num, pw, name, money, term, interest))

def menu():
    print("\n1.적금생성 2.대출생성 3.전체조회 4.계좌조회 7.입금 8.출금 9.삭제 0.종료")

while True:
    menu()
    choice = int(input("입력 : "))

    match choice:
        case 1:
            create_saving()
        case 2:
            create_loan()
        case 3:
            selectAll()
        case 4:
            selectByAcc()
        case 7:
            despot = selectByAcc()
            if despot:
                despot.money += int(input("입금액 : "))
        case 8:
            withdraw = selectByAcc()
            if withdraw and withdraw.pw == input("비번 : "):
                min = int(input("출금액 : "))
                if withdraw.money >= min: 
                    withdraw.money -= min
        case 9:
            find = selectByAcc()
            if find:
                account.remove(find)
        case 0:
            break