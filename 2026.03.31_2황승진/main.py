from car_loan import create_loan, select_all, select_one, update_loan, delete_loan

def main():
    while True:
        print("\n" + "=" * 30)
        print("   자동차 대출 관리 프로그램")
        print("=" * 30)
        print("1. 대출 등록")
        print("2. 전체 조회")
        print("3. 1건 조회")
        print("4. 대출 수정")
        print("5. 대출 삭제")
        print("6. 프로그램 종료")
        print("=" * 30)

        match input("메뉴 선택 : ").strip():
            case "1": create_loan()
            case "2": select_all()
            case "3": select_one()
            case "4": update_loan()
            case "5": delete_loan()
            case "6":
                print("프로그램을 종료합니다.")
                break
            case _:
                print("1~6 중에서 선택하세요.")

if __name__ == "__main__":
    main()