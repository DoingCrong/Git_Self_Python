import numpy as np

from concept5_service import (
    insert,
    selectAll,
    selectById,
    # update,
    # delete,
    # graph
 )

def menu():
    print("\n==== 선택 화면 ====")
    print("1. 입력\n" \
          "2. 전체 조회\n" \
          "3. 거래번호 조회\n" \
          "4. 수정\n" \
          "5. 삭제\n" \
          "6. 차트출력\n" \
          "0. 종료")

while True:
    menu()

    try:
        choice = int(input("\n입력 : "))
    except ValueError:
        print("숫자만 입력 가능합니다.")
        #return None
    
    match choice:
        case 0:
            break
        case 1:
            insert()
        case 2:
            selectAll()
        case 3:
            selectById()
        case 4:
            update()
        case 5:
            delete()
        case 6:
            graph()