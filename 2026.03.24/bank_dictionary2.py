accounts = []

while True:
    print("1.계좌생성")
    print("2.입금")
    print("3.출금")
    print("4.잔액조회")
    print("5.전체조회")
    print("6.종료")
    choice = input("메뉴를 선택하세요:")

    if choice == "1":
        acc_num = input("계좌번호:")
        
        check = 0
        for acc in accounts:
            if acc["acc_num"] == acc_num:
                print("이미 존재하는 계좌번호입니다.")
                check = 1
                break
        
        if check == 0:
            name = input("예금주명:")
            money = int(input("초기금액:"))
            new_acc = {"acc_num": acc_num, "name": name, "balance": money}
            accounts.append(new_acc)
            print("계좌가 생성되었습니다.")

    elif choice == "2":
        search_num = input("입금할 계좌번호:")
        for acc in accounts:
            if acc["acc_num"] == search_num:
                deposit = int(input("입금액:"))
                acc["balance"] = acc["balance"] + deposit
                print("입금이 완료되었습니다.")
                break

    elif choice == "3":
        search_num = input("출금할 계좌번호:")
        for acc in accounts:
            if acc["acc_num"] == search_num:
                withdraw = int(input("출금액:"))
                if acc["balance"] >= withdraw:
                    acc["balance"] = acc["balance"] - withdraw
                    print("출금이 완료되었습니다.")
                else:
                    print("잔액이 부족합니다.")
                break

    elif choice == "4":
        search_num = input("조회할 계좌번호:")
        for acc in accounts:
            if acc["acc_num"] == search_num:
                print("계좌번호 :", acc["acc_num"])
                print("예금주명 :", acc["name"])
                print("현재잔액 :", acc["balance"])
                break

    elif choice == "5":
        print("============================================")
        print("계좌번호\t예금주\t잔액")
        print("============================================")
        for acc in accounts:
            print(acc["acc_num"], "\t", acc["name"], "\t", acc["balance"])
        print("============================================")

    elif choice == "6":
        print("프로그램을 종료합니다.")
        break