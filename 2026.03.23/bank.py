totalac=[]
ac=[]

name = input("이름 : ")
account = input("계좌번호 : ")
money = int(input("초기 금액 : "))

totalac.extend([account])
ac.extend([name, account,money])

print(totalac)
#초기에 입력한 값 기준으로 작동함
while True:
    
    menu = int(input(
        "====메뉴====\n" \
        "1. 계좌생성\n" \
        "2. 입금\n" \
        "3. 출금\n" \
        "4. 잔액조회\n" \
        "5. 전체계좌조회\n" \
        "0. 프로그램종료\n" \
        "\n숫자 입력 : "
    ))

    if menu==0:
        print("프로그램을 종료 합니다.")
        break

    elif menu==1:
        creac = input("생성하실 계좌번호를 입력 : ")
        if creac == totalac[0]:
            print("계좌는 중복되실 수 없습니다.")
        else:
            name = input("이름 : ")
            money = int(input("초기 금액 : "))

            totalac.extend([creac])
            ac.extend([creac, name, money])
            print(totalac)
            print(ac)

    elif menu==2:
        checkac = input("입금하실 계좌번호 : ")
        if checkac != totalac[0]:
            print("입력하신 계좌번호가 존재하지 않습니다.")
        else:
            plus = int(input("입금 금액 : "))
            ac[2] = ac[2]+plus
            print("현재 잔액",ac[2])

    elif menu==3:
        checkac = input("출금하실 계좌번호 : ")
        if checkac != totalac[0]:
            print("입력하신 계좌번호가 존재하지 않습니다.")
        else:
            min = int(input("출금 금액 : "))
            if min>ac[2]:
                print("잔액이 부족합니다.")
            else:
                ac[2] = ac[2]-min
                print("현재 잔액",ac[2])

    elif menu==4:
        checkac = input("조회하실 계좌번호 : ")
        if checkac != totalac[0]:
            print("입력하신 계좌번호가 존재하지 않습니다.")
        else:
            print("현재 잔액은 ",ac[2],"원 입니다.")
    
    elif menu==5:
        print("전체 계좌번호 조회")
        for data in totalac:
            print(totalac)
            print(ac)


