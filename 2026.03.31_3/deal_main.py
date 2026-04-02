from deal_service import(
    deal_insert,
    deal_selectAll,
    deal_selectById,
    deal_update,
    deal_delete,
    deal_data
)



def main():
    while True:
        print("\n===== 가계부 관리 프로그램 =====")
        print("1. 거래 등록\n" \
              "2. 전체 조회\n" \
              "3. 1건 조회\n" \
              "4. 거래 수정\n" \
              "5. 거래 삭제\n" \
              "6. 통계 조회\n" \
              "0. 프로그램 종료")
        print("="*32)

        menu = int(input("\n입력 : "))

        match menu:
            case 1:
                deal_insert()
            case 2:
                deal_selectAll()
            case 3:
                deal_selectById()
            case 4:
                deal_update()
            case 5:
                deal_delete()
            case 6:
                deal_data()
            case 0:
                print("\"프로그램을 종료합니다.\"")
                break
            case _:
                print("그건 할 수 없어요")
                return
            
if __name__ == "__main__":
    main()