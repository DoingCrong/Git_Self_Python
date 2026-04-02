from student_service import(
    insert_student,
    select_all,
    select_one,
    update_student,
    delete_student
)


def main():
    while True:
        print("\n" + "=" * 30)
        print("   성적 관리 프로그램")
        print("=" * 30)
        print("1. 성적입력")
        print("2. 전체 조회")
        print("3. 1명 조회")
        print("4. 성적 수정")
        print("5. 성적 삭제")
        print("6. 프로그램 종료")
        print("=" * 30)

        menu = input("메뉴 선택 : ").strip()

        # match-case 사용
        match menu:
            case "1":
                insert_student()

            case "2":
                select_all()

            case "3":
                select_one()

            case "4":
                update_student()

            case "5":
                delete_student()

            case "6":
                print("프로그램을 종료합니다.")
                break

            case _:
                # default 역할
                print("메뉴를 다시 선택하세요.")


# ===============================
# 프로그램 시작 지점
# ===============================
if __name__ == "__main__":
    main()