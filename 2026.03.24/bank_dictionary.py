accounts = []

while True:
    print("\n==============================")
    print("      은행 예금 프로그램")
    print("==============================")
    print("1. 계좌 생성")
    print("2. 입금")
    print("3. 출금")
    print("4. 잔액 조회")
    print("5. 전체 계좌 조회")
    print("6. 프로그램 종료")
    print("==============================")

    menu = input("메뉴 선택 : ")

    # 1. 계좌 생성
    if menu == '1':
        acc_no = input("계좌번호 입력 : ")

        # 중복 체크
        exists = False
        for acc in accounts:
            if acc['acc_no'] == acc_no:
                exists = True
                break

        if exists:
            print("이미 존재하는 계좌번호입니다.")
        else:
            name = input("예금주명 입력 : ")
            money = int(input("초기금액 입력 : "))
            
            #딕셔너리 입력
            account = {
                'acc_no': acc_no,
                'name': name,
                'balance': money
            }

            accounts.append(account)
            print("계좌 생성 완료")

    # 2. 입금
    elif menu == '2':
        acc_no = input("계좌번호 입력 : ")
        deposit = int(input("입금 금액 : "))

        found = False
        for acc in accounts:
            if acc['acc_no'] == acc_no:
                acc['balance'] += deposit
                print("입금 완료")
                print("현재 잔액 :", acc['balance'])
                found = True
                break

        if not found:
            print("계좌가 없습니다.")

    # 3. 출금
    elif menu == '3':
        acc_no = input("계좌번호 입력 : ")
        withdraw = int(input("출금 금액 : "))

        found = False
        for acc in accounts:
            if acc['acc_no'] == acc_no:
                found = True
                if acc['balance'] >= withdraw:
                    acc['balance'] -= withdraw
                    print("출금 완료")
                    print("현재 잔액 :", acc['balance'])
                else:
                    print("잔액 부족")
                break

        if not found:
            print("계좌가 없습니다.")

    # 4. 잔액 조회
    elif menu == '4':
        acc_no = input("계좌번호 입력 : ")

        found = False
        for acc in accounts:
            if acc['acc_no'] == acc_no:
                print("\n===== 계좌 정보 =====")
                print("계좌번호 :", acc['acc_no'])
                print("예금주 :", acc['name'])
                print("잔액 :", acc['balance'])
                found = True
                break

        if not found:
            print("계좌가 없습니다.")

    # 5. 전체 조회
    elif menu == '5':
        if len(accounts) == 0:
            print("등록된 계좌가 없습니다.")
        else:
            print("\n계좌번호\t예금주\t잔액")
            for acc in accounts:
                print(f"{acc['acc_no']}\t{acc['name']}\t{acc['balance']}")

    # 6. 종료
    elif menu == '6':
        print("프로그램 종료")
        break

    else:
        print("잘못된 입력입니다.")