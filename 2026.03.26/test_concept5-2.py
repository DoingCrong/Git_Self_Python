# 은행 공통 계좌 클래스(부모 클래스)
class BankAccount:
    # 생성자
    def __init__(self, account_no, owner, password, money):
        self.account_no = account_no   # 계좌번호
        self.owner = owner             # 예금주
        self.password = password       # 비밀번호
        self.money = money             # 금액(적금 원금 또는 대출금)

    # 입금 메서드
    def deposit(self, amount):
        self.money += amount
        print(f"{amount}원 입금 완료")
        print(f"현재 금액 : {self.money}원")

    # 출금 메서드
    def withdraw(self, amount, password):
        # 비밀번호 확인
        if self.password != password:
            print("비밀번호가 틀렸습니다.")
            return

        # 금액 확인
        if amount > self.money:
            print("잔액이 부족합니다.")
            return

        self.money -= amount
        print(f"{amount}원 출금 완료")
        print(f"현재 금액 : {self.money}원")

    # 계좌 기본 정보 출력
    def display(self):
        print("===== 계좌 정보 =====")
        print(f"계좌번호 : {self.account_no}")
        print(f"예금주 : {self.owner}")
        print(f"현재금액 : {self.money}원")


# 적금 클래스(자식 클래스)
class SavingAccount(BankAccount):
    # 생성자
    def __init__(self, account_no, owner, password, money, months, rate):
        # 부모 생성자 호출
        super().__init__(account_no, owner, password, money)
        self.months = months   # 적금 기간(개월)
        self.rate = rate       # 이율(%)

    # 만기금액 계산
    def calc_maturity(self):
        return self.money + (self.money * self.rate / 100 * self.months / 12)

    # 부모의 display()를 재정의(오버라이딩)
    def display(self):
        print("===== 적금 계좌 정보 =====")
        print(f"상품종류 : 적금")
        print(f"계좌번호 : {self.account_no}")
        print(f"예금주 : {self.owner}")
        print(f"원금 : {self.money}원")
        print(f"기간 : {self.months}개월")
        print(f"이율 : {self.rate}%")
        print(f"만기예상금액 : {self.calc_maturity():.2f}원")


# 대출 클래스(자식 클래스)
class LoanAccount(BankAccount):
    # 생성자
    def __init__(self, account_no, owner, password, money, months, rate):
        # 부모 생성자 호출
        super().__init__(account_no, owner, password, money)
        self.months = months   # 대출 기간(개월)
        self.rate = rate       # 이율(%)

    # 총 상환 금액 계산
    def calc_total_repayment(self):
        return self.money + (self.money * self.rate / 100 * self.months / 12)

    # 월 상환 금액 계산
    def calc_month_payment(self):
        return self.calc_total_repayment() / self.months

    # 부모의 display()를 재정의(오버라이딩)
    def display(self):
        print("===== 대출 계좌 정보 =====")
        print(f"상품종류 : 대출")
        print(f"계좌번호 : {self.account_no}")
        print(f"예금주 : {self.owner}")
        print(f"대출금 : {self.money}원")
        print(f"기간 : {self.months}개월")
        print(f"이율 : {self.rate}%")
        print(f"총상환금액 : {self.calc_total_repayment():.2f}원")
        print(f"월상환금액 : {self.calc_month_payment():.2f}원")


# 계좌 찾기 함수
def find_account(account_list, account_no):
    for acc in account_list:
        if acc.account_no == account_no:
            return acc
    return None


# 계좌 전체 조회 함수
def show_all_accounts(account_list):
    if len(account_list) == 0:
        print("등록된 계좌가 없습니다.")
        return

    print("\n===== 전체 계좌 조회 =====")
    for acc in account_list:
        acc.display()
        print()


# 메인 프로그램 시작
account_list = []   # 모든 계좌를 저장할 리스트

while True:
    print("\n==============================")
    print(" 은행 금융 상품 관리 프로그램 ")
    print("==============================")
    print("1. 적금 계좌 생성")
    print("2. 대출 계좌 생성")
    print("3. 전체 계좌 조회")
    print("4. 한 계좌 조회")
    print("5. 적금 만기금액 조회")
    print("6. 대출 상환정보 조회")
    print("7. 입금")
    print("8. 출금")
    print("9. 계좌 삭제")
    print("0. 종료")
    print("==============================")

    menu = input("메뉴 선택 : ")

    match menu:
        case "1":
            print("\n[적금 계좌 생성]")
            account_no = input("계좌번호 : ")

            # 계좌번호 중복 검사
            if find_account(account_list, account_no) is not None:
                print("이미 존재하는 계좌번호입니다.")
                continue

            owner = input("예금주 : ")
            password = input("비밀번호 : ")
            money = int(input("원금 : "))
            months = int(input("기간(개월) : "))
            rate = float(input("이율(%) : "))

            acc = SavingAccount(account_no, owner, password, money, months, rate)
            account_list.append(acc)
            print("적금 계좌가 생성되었습니다.")

        case "2":
            print("\n[대출 계좌 생성]")
            account_no = input("계좌번호 : ")

            # 계좌번호 중복 검사
            if find_account(account_list, account_no) is not None:
                print("이미 존재하는 계좌번호입니다.")
                continue

            owner = input("예금주 : ")
            password = input("비밀번호 : ")
            money = int(input("대출금액 : "))
            months = int(input("기간(개월) : "))
            rate = float(input("이율(%) : "))

            acc = LoanAccount(account_no, owner, password, money, months, rate)
            account_list.append(acc)
            print("대출 계좌가 생성되었습니다.")

        case "3":
            show_all_accounts(account_list)

        case "4":
            print("\n[한 계좌 조회]")
            account_no = input("조회할 계좌번호 : ")
            acc = find_account(account_list, account_no)

            if acc is None:
                print("해당 계좌가 없습니다.")
            else:
                acc.display()

        case "5":
            print("\n[적금 만기금액 조회]")
            account_no = input("계좌번호 : ")
            acc = find_account(account_list, account_no)

            if acc is None:
                print("해당 계좌가 없습니다.")
            elif isinstance(acc, SavingAccount):
                print(f"만기예상금액 : {acc.calc_maturity():.2f}원")
            else:
                print("이 계좌는 적금 계좌가 아닙니다.")

        case "6":
            print("\n[대출 상환정보 조회]")
            account_no = input("계좌번호 : ")
            acc = find_account(account_list, account_no)

            if acc is None:
                print("해당 계좌가 없습니다.")
            elif isinstance(acc, LoanAccount):
                print(f"총상환금액 : {acc.calc_total_repayment():.2f}원")
                print(f"월상환금액 : {acc.calc_month_payment():.2f}원")
            else:
                print("이 계좌는 대출 계좌가 아닙니다.")

        case "7":
            print("\n[입금]")
            account_no = input("계좌번호 : ")
            acc = find_account(account_list, account_no)

            if acc is None:
                print("해당 계좌가 없습니다.")
            else:
                amount = int(input("입금금액 : "))
                acc.deposit(amount)

        case "8":
            print("\n[출금]")
            account_no = input("계좌번호 : ")
            acc = find_account(account_list, account_no)

            if acc is None:
                print("해당 계좌가 없습니다.")
            else:
                amount = int(input("출금금액 : "))
                password = input("비밀번호 : ")
                acc.withdraw(amount, password)

        case "9":
            print("\n[계좌 삭제]")
            account_no = input("삭제할 계좌번호 : ")
            acc = find_account(account_list, account_no)

            if acc is None:
                print("해당 계좌가 없습니다.")
            else:
                password = input("비밀번호 : ")
                if acc.password == password:
                    account_list.remove(acc)
                    print("계좌가 삭제되었습니다.")
                else:
                    print("비밀번호가 틀렸습니다.")

        case "0":
            print("프로그램을 종료합니다.")
            break

        case _:
            print("잘못된 메뉴입니다. 다시 선택하세요.")