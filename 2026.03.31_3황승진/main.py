from household import (create_trade, select_all, select_one,
                       update_trade, delete_trade, show_stats)

def main():
    while True:
        print("\n" + "=" * 30)
        print("     가계부 관리 프로그램")
        print("=" * 30)
        print("1. 거래 등록")
        print("2. 전체 조회")
        print("3. 1건 조회")
        print("4. 거래 수정")
        print("5. 거래 삭제")
        print("6. 통계 조회")
        print("7. 프로그램 종료")
        print("=" * 30)

        match input("메뉴 선택 : ").strip():
            case "1": create_trade()
            case "2": select_all()
            case "3": select_one()
            case "4": update_trade()
            case "5": delete_trade()
            case "6": show_stats()
            case "7":
                print("프로그램을 종료합니다.")
                break
            case _:
                print("  1~7 중에서 선택하세요.")

if __name__ == "__main__":
    main()