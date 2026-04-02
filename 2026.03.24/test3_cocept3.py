"""
8. 
상품 주문 관리 프로그램
문제

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
box = []
#food = {
#    "라면" : 4500,
#    "국수" : 5000,
#    "쫄면" : 5500,
#    "짜장면" : 6000
#}

def input_box(box):
    print("음식정보")
    code = int(input("1. 라면 / 4500 \n" \
                     "2. 국수 / 5000 \n" \
                     "3. 쫄면 / 5500 \n" \
                     "4. 짜장면 / 6000 \n" \
                     "0. 종료(음식코드에)" \
                     "\n음식코드 : "))
    count = int(input("갯수입력 : "))

    if code==1:
        howmuch=4500*count
    elif code==2:
        howmuch=5000*count
    elif code==3:
        howmuch=5500*count
    elif code==4:
        howmuch=6000*count
    elif code==0:
        return
    else:
        print("그런건없습니다.")

    print(f"음식코드 : {code} / {count}개 주문완료.")
    return box.append([code,count,howmuch])

def selectbybox_box(box):
    for i in box:
        print(f"상품명: {i[0]}, 수량: {i[1]}")

def selectbymoney_box(box):
    total=0
    for i in box:
        total+=i[2]
        print(total,"원 입니다.")

while True:
    menu = int(input("1. 상품주문\n" \
                     "2. 주문내역조회\n" \
                     "3. 총결제금액조회\n" \
                     "4. 종료\n" \
                     "\n입력 : "))

    if menu==1:
        input_box(box)
    elif menu==2:
        selectbybox_box(box)
    elif menu==3:
        selectbymoney_box(box)
    elif menu==4:
        print("프로그램이 종료됩니다.")
        break
    else:
        print("그건 할 수 없어요.")
        break

    
