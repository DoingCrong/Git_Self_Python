"""
계좌번호와 예금주를 입력받아 계좌를 생성하고, 다음 기능을 수행하세요.

기능

계좌 생성
입금
출금
잔액 조회
전체 계좌 조회
종료

조건

계좌 여러 개 관리
계좌 정보는 딕셔너리
전체 계좌는 리스트
같은 계좌번호는 중복 불가
"""
#계좌번호 입력
def create_account(account_list):
    acc_no = input("계좌번호 입력 : ")
    
    for acc in account_list:
        if acc["계좌번호"] == acc_no:
            print("이미 존재하는 계좌번호입니다.")
            return

    owner = input("예금주 입력 : ")
    money = int(input("초기 입금액 입력 : "))

    account = {
        "계좌번호": acc_no,
        "예금주": owner,
        "잔액": money
    }

    account_list.append(account)
    print("계좌가 생성되었습니다.")

#입금
def deposit(account_list):
    acc_no = input("입금할 계좌번호 입력 : ")
    found = False

    for acc in account_list:
        if acc["계좌번호"] == acc_no:
            money = int(input("입금액 입력 : "))
            acc["잔액"] += money
            print("입금 완료, 현재 잔액 :", acc["잔액"])
            found = True
            break

    if found == False:
        print("계좌를 찾을 수 없습니다.")

#출금
def withdraw(account_list):
    acc_no = input("출금할 계좌번호 입력 : ")
    found = False

    for acc in account_list:
        if acc["계좌번호"] == acc_no:
            money = int(input("출금액 입력 : "))
            if money > acc["잔액"]:
                print("잔액이 부족합니다.")
            else:
                acc["잔액"] -= money
                print("출금 완료, 현재 잔액 :", acc["잔액"])
            found = True
            break

    if found == False:
        print("계좌를 찾을 수 없습니다.")

#전체 계좌 조회
def show_balance(account_list):
    acc_no = input("조회할 계좌번호 입력 : ")
    found = False

    for acc in account_list:
        if acc["계좌번호"] == acc_no:
            print("계좌번호 :", acc["계좌번호"])
            print("예금주 :", acc["예금주"])
            print("잔액 :", acc["잔액"])
            found = True
            break

    if found == False:
        print("계좌를 찾을 수 없습니다.")

#계별 조회
def show_all_accounts(account_list):
    if len(account_list) == 0:
        print("등록된 계좌가 없습니다.")
        return

    print("계좌번호 예금주 잔액")
    for acc in account_list:
        print(acc["계좌번호"], acc["예금주"], acc["잔액"])


accounts = []

while True:
    print("\n===== 은행 계좌 관리 =====")
    print("1. 계좌 생성")
    print("2. 입금")
    print("3. 출금")
    print("4. 잔액 조회")
    print("5. 전체 계좌 조회")
    print("6. 종료")

    menu = input("메뉴 선택 : ")

    if menu == "1":
        create_account(accounts)
    elif menu == "2":
        deposit(accounts)
    elif menu == "3":
        withdraw(accounts)
    elif menu == "4":
        show_balance(accounts)
    elif menu == "5":
        show_all_accounts(accounts)
    elif menu == "6":
        print("프로그램 종료")
        break
    else:
        print("잘못 입력했습니다.")