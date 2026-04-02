from bank_service import(
    acc_cre,
    selectAll,
    selectByAcc,
    acc_dep,
    acc_with,
    acc_update,
    acc_delete
)

def main():
    while True:
        print("\n=== 은행메뉴기능 ===")
        print("1. 계좌생성" \
        "\n2. 전체 계좌 조회" \
        "\n3. 특정 계좌 조회" \
        "\n4. 입금" \
        "\n5. 출금" \
        "\n6. 예금주명 수정" \
        "\n7. 계좌 삭제" \
        "\n0. 프로그램 종료")

        menu = int(input("\n입력 : "))

        match menu:
            case 1:
                acc_cre()
            case 2:
                selectAll()
            case 3:
                selectByAcc()
            case 4:
                acc_dep()
            case 5:
                acc_with()
            case 6:
                acc_update()
            case 7:
                acc_delete()
            case 0:
                break
            case _:
                print("메뉴를 다시 선택하세요.")

if __name__ == "__main__":
    main()