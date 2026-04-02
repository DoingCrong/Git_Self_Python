"""
(1) 클래스 사용
Bank 클래스를 작성한다.
생성자 __init__()를 이용하여 계좌 정보를 초기화한다.
(2) 계좌 정보

계좌 1개의 정보는 다음과 같이 구성한다.

계좌번호
예금주명
비밀번호
잔액
(3) 저장 구조
계좌 1개 정보는 딕셔너리로 저장
전체 계좌는 리스트에 저장
(4) 기능 구현

다음 기능을 구현하시오.

1.계좌생성
계좌번호, 예금주명, 비밀번호, 초기입금액을 입력받는다.
계좌번호가 중복되면 생성할 수 없다.
2. 입금
계좌번호를 입력받아 해당 계좌에 입금한다.
존재하지 않는 계좌번호이면 메시지를 출력한다.
3. 출금
계좌번호와 비밀번호를 확인한 후 출금한다.
비밀번호가 틀리면 출금할 수 없다.
잔액이 부족하면 출금할 수 없다.
4. 한 계좌 잔액조회
계좌번호와 비밀번호를 입력받아 한 계좌의 잔액을 조회한다.
5. 전체 계좌 잔액조회
모든 계좌의 계좌번호, 예금주명, 잔액을 출력한다.
6. 계좌 삭제
계좌번호와 비밀번호를 입력받아 계좌를 삭제한다.
7. 종료
"""

class Bank:
    def __init__(self, acc_num, name, pw, money):
        self.acc_num = acc_num
        self.name = name
        self.pw = pw
        self.money = money

    def dic(self):
        return {
            "계좌번호" : self.acc_num,
            "이름" : self.name,
            "비밀번호" : self.pw,
            "잔액" : self.money
        }

# 1. 계좌생성
def acc_cre():
    acc_num = input("계좌번호 입력 : ")
    
    # 중복 확인
    for acc in account:
        if acc["계좌번호"] == acc_num:
            print("이미 존재하는 계좌번호입니다.")
            return

    pw = input("비밀번호 입력 : ")
    name = input("이름 입력 : ")
    money = int(input("초기금액 입력 : "))

    b = Bank(acc_num, name, pw, money)
    account.append(b.dic())
    print(f"계좌번호 : {acc_num}, 비밀번호 : {pw}, 이름 : {name}, 잔액 : {money}\n계좌 생성 완료!")

# 2. 입금
def acc_plus():
    acc_num = input("계좌번호 입력 : ")

    # 중복 확인
    for acc in account:
        if acc["계좌번호"] == acc_num:
            money = int(input("입금하실 금액 : "))
            acc["잔액"] += money
            print(f"입금 금액 : {money}원\n현재잔액 : {acc['잔액']}원")
            return
        else:  
            print("계좌번호를 다시 확인해 주세요")

# 3. 출금
def acc_min():
    acc_num = input("계좌번호 입력 : ")

    # 중복 확인
    for acc in account:
        if acc["계좌번호"] == acc_num:
            #중복 확인2
            pw = input("비밀번호 입력 : ")
            if acc["비밀번호"] == pw:
                money = int(input("출금하실 금액 : "))
                if acc["잔액"] < money:
                    print("잔액이 부족합니다.")
                else:
                    acc["잔액"] -= money
                    print(f"출금 금액 : {money}원\n현재잔액 : {acc['잔액']}원")
                return
            else:
                print("비밀번호를 다시 확인해 주세요")
                return
        else:
            print("계좌번호를 다시 확인해 주세요")

# 4. 한사람계좌조회
def selectByAcc():
    acc_num = input("계좌번호 입력 : ")

    # 중복 확인
    for acc in account:
        if acc["계좌번호"] == acc_num:
            #중복 확인2 
            pw = input("비밀번호 입력 : ")
            if acc["비밀번호"] == pw:
                print(f"계좌번호 : {acc['계좌번호']} / 비밀번호 : {acc['비밀번호']} / 예금주명 : {acc['이름']} / 현재잔액 : {acc['잔액']}")
                return
            else:
                print("비밀번호를 다시 확인해 주세요")
                return
        else:
            print("계좌번호를 다시 확인해 주세요")

# 5. 전체 계좌조회
def selectAll():
    #전에 for acc in account는 리스트에 아무 정보가 없어서 0이라 for문이 돌지않아 작동하지 않았음
    if not account:
        print("계좌가 없어요")
        print("*"*50)
        return
    
    for acc in account:
        print(f"계좌번호 : {acc['계좌번호']} / 비밀번호 : {acc['비밀번호']} / 예금주명 : {acc['이름']} / 현재잔액 : {acc['잔액']}")

# 6. 계좌 삭제
def acc_delete():
    acc_num = input("계좌번호 입력 : ")

    # 중복 확인
    for acc in account:
        if acc["계좌번호"] == acc_num:
            #중복 확인2
            pw = input("비밀번호 입력 : ")
            if acc["비밀번호"] == pw:
                account.remove(acc)
                print("계좌 삭제 완료!")
                return
            else:
                print("비밀번호를 다시 확인해 주세요")
                return
        else:
            print("계좌번호를 다시 확인해 주세요")

# 리스트
account = []

while True:
    menu = int(input("1. 계좌생성\n" \
                     "2. 입 금\n" \
                     "3. 출 금\n" \
                     "4. 한 계좌 조회\n" \
                     "5. 전체 계좌 조회\n" \
                     "6. 계좌 삭제\n" \
                     "7. 종료\n"
                     "\n입력 : "))
    
    if menu == 1:
        acc_cre()
    elif menu == 2:
        acc_plus()
    elif menu == 3:
        acc_min()
    elif menu == 4:
        selectByAcc()
    elif menu == 5:
        selectAll()
    elif menu == 6:
        acc_delete()
    elif menu == 7:
        break
    else:
        print("그런메뉴는 없습니다.")
        break