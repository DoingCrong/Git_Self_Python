from car_service import(
    loan_insert,
    loan_selectAll,
    loan_selectById,
    loan_update,
    loan_delete
)


def main():
    while True:
        print("\n=== 자동차 대출 관리 ===")
        print("1. 대출 등록" \
             "\n2. 전체 조회" \
             "\n3. 1건 조회" \
             "\n4. 대출 수정" \
             "\n5. 대출 삭제" \
             "\n0. 프로그램 종료")
        
        menu = int(input("\n입력 : "))

        match menu:
            case 0:
                print("\"프로그램을종료합니다.\"")
                break
            case 1:
                loan_insert()
            case 2:
                loan_selectAll()
            case 3:
                loan_selectById()
            case 4:
                loan_update()
            case 5:
                loan_delete()
            case _:
                print("그런메뉴는 없습니다.")

if __name__ == "__main__":
    main()