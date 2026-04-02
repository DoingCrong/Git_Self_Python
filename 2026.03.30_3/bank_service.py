import pymysql
import numpy as np
from db_config import db_connect

##acc_balance
def acc_balance():
    while True:
        try:
            money = int(input("잔액 : "))

            if money < 0:
                print("잔액은 0아래일 수 없습니다.")
                continue

            return money

        except ValueError:
            print("숫자만 입력 가능합니다.")


#acc_cre()
def acc_cre():
    conn = db_connect()
    cursor = conn.cursor()

    try:
        print("=== 1. 계좌생성 === ")

        acc_no = int(input("계좌번호 : "))
        owner = input("이름 : ")
        password = input("비밀번호 : ")
        balance = acc_balance()

        sql ="""
        insert into account(acc_no, owner, password, balance)
        values(%s, %s, %s, %s)
        """

        cursor.execute(sql, (acc_no, owner, password, balance))
        conn.commit()

        print("계좌생성완료!")
        print(f"{owner}님 환영합니다.")

    #pymysql.err.IntegrityError:
    except pymysql.err.IntegrityError:
        print("이미 존재하는 계좌번호 입니다.")

    finally:
        cursor.close()
        conn.close()

#selectAll
def selectAll():
    conn = db_connect()
    cursor = conn.cursor()

    try:
        print("=== 2. 전체 계좌 조회 === ")

        sql = "select * from account order by acc_no"
        cursor.execute(sql)

        rows = cursor.fetchall()

        if len(rows) == 0:
            print("저장된 데이터가 없습니다.")
            return

        print("-" * 80)
        print("계좌번호\t이름\t비밀번호\t잔액")
        print("-" * 80)

        for row in rows:
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")

    except Exception as e:
        print("조회 중 오류 발생 :", e)

    finally:
        cursor.close()
        conn.close()

#selectByAcc
def selectByAcc():
    conn = db_connect()
    cursor = conn.cursor()

    try:
        print("=== 3. 특정 계좌 조회 === ")

        acc_no = input("조회하실 계좌번호 입력 : ").strip()

        sql = "select * from account where acc_no=%s"
        cursor.execute(sql, (acc_no,))

        row = cursor.fetchone()

        if row is None:
            print("해당 계좌번호가 없습니다.")
            return

        print("-" * 40)
        print("계좌번호 :", row[0])
        print("이름 :", row[1])
        print("비밀번호 :", row[2])
        print("잔액 :", row[3])
        print("-" * 40)

    except Exception as e:
        print("조회 중 오류 발생 :", e)

    finally:
        cursor.close()
        conn.close()

#acc_dep
def acc_dep():
    conn = db_connect()
    cursor = conn.cursor()

    try:
        print("=== 4. 입금 === ")
        acc_no = input("입금하실 계좌번호 입력 : ").strip()

        check_sql = "select * from account where acc_no=%s"
        cursor.execute(check_sql, (acc_no,))
        row = cursor.fetchone()

        if row is None:
            print("해당 계좌번호가 없습니다.")
            return

        print("=== 4. 입금페이지 ===")
        money = int(input("입금금액 : "))

        if money <= 0:
            print("입금금액이 0보다 작거나 같을 수 없습니다.")
            return

        total = row[3] + money
        
        sql = "update account set balance=%s where acc_no=%s"
        cursor.execute(sql, (total, acc_no))
        conn.commit()

        print(f"{money}원 입금 완료!")
        print(f"잔액 : {total}")

    except Exception as e:
        print("수정 중 오류 발생 :", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

#acc_with
def acc_with():
    conn = db_connect()
    cursor = conn.cursor()

    try:
        print("=== 5. 출금 === ")
        acc_no = input("출금하실 계좌번호 입력 : ").strip()

        check_sql = "select * from account where acc_no=%s"
        cursor.execute(check_sql, (acc_no,))
        row = cursor.fetchone()

        if row is None:
            print("해당 계좌번호가 없습니다.")
            return

        print("=== 5. 출금페이지 ===")
        money = int(input("출금금액 : "))

        if money <= 0:
            print("출금금액이 0보다 작거나 같을 수 없습니다.")
            return
        
        if row[3] < money:
            print("잔액이 부족합니다.")
            return

        total = row[3] - money

        sql = "update account set balance=%s where acc_no=%s"
        cursor.execute(sql, (total, acc_no))
        conn.commit()

        print(f"{money}원 출금 완료!")
        print(f"잔액 : {total}")

    except Exception as e:
        print("수정 중 오류 발생 :", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

#acc_update
def acc_update():
    conn = db_connect()
    cursor = conn.cursor()

    try:
        print("=== 6. 예금주명 수정 === ")
        total=0
        acc_no = input(" 계좌번호 입력 : ").strip()

        check_sql = "select * from account where acc_no=%s"
        cursor.execute(check_sql, (acc_no,))
        row = cursor.fetchone()

        if row is None:
            print("해당 계좌번호가 없습니다.")
            return

        print("=== 6. 수정페이지 ===")
        rename = input("이름 입력 : ")

        sql = """
        update account
        set owner=%s
        where acc_no=%s
        """

        cursor.execute(sql, (rename, acc_no))
        conn.commit()

        print(f"{rename}님 환영합니다!")

    except Exception as e:
        print("수정 중 오류 발생 :", e)

    finally:
        cursor.close()
        conn.close()

#acc_delete
def acc_delete():
    conn = db_connect()
    cursor = conn.cursor()

    try:
        print("=== 7. 계좌 삭제 === ")

        acc_no = input("삭제하실 계좌번호 입력 : ").strip()

        check_sql = "select * from account where acc_no=%s"
        cursor.execute(check_sql, (acc_no,))
        row = cursor.fetchone()

        if row is None:
            print("해당 계좌번호가 없습니다.")
            return

        print("=== 7. 삭제페이지 ===")
        answer = input("정말 삭제하시겠습니까? (y/n) : ").strip().lower()

        if answer != "y":
            print("삭제 취소")
            return

        sql = "delete from account where acc_no=%s"
        cursor.execute(sql, (acc_no,))
        conn.commit()

        print("계좌 삭제 완료")

    except Exception as e:
        print("삭제 중 오류 발생 :", e)

    finally:
        cursor.close()
        conn.close()