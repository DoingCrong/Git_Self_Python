import pymysql
import numpy as np
from car_db_config import db_connect

loan_inter = [0.0,0.05,0.055,0.06,0.065,0.07]

def loan_insert():
    conn = db_connect()
    cursor = conn.cursor()

    try:
        print("\n=== 1. 대출 등록 ===")
        loan_no = input("대출번호 : ")
        car_price = int(input("자동차금액 : "))
        down_payment = int(input("선수금(피값) : "))
        loan_period = int(input("대출 기간(최대5년) : "))
        if loan_period <0 or loan_period >5: 
            print("대출최대기한은 5년 입니다.")
            return

        loan_amount = car_price - down_payment #대출금액
        loan_interest = loan_amount * loan_inter[int(loan_period)] * loan_period #대출이자
        total_payment = loan_amount + loan_interest #총 상환 금액
        monthly_payment = total_payment / (loan_period*12) #월 납입 금액


        sql = """
        insert into car_loan(loan_no, car_price, down_payment, loan_period, loan_amount, loan_interest, total_payment, monthly_payment)
        values(%s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql,(loan_no,car_price,down_payment,loan_period,loan_amount,loan_interest,total_payment,monthly_payment))
        conn.commit()

        print("대출 생성 완료!")
        print(f"{loan_no}님 환영합니다.")

    #pymysql.err.IntegrityError:  
    except pymysql.err.IntegrityError:
        print("이미 존재하는 대출번호 입니다.")

    finally:
        cursor.close()
        conn.close()

def loan_selectAll():
    conn = db_connect()
    cursor = conn.cursor()

    try: 
        print("\n=== 2. 전체 조회 ===")

        sql = """
        select * from car_loan
        """
        cursor.execute(sql)

        rows = cursor.fetchall()

        if len(rows) == 0:
            print("등록된 데이터가 없습니다.")
            return
        
        print("\n대출번호\t"
              "자동차금액\t"
              "선수금\t"
              "대출기간(년)\t"
              "대출금액\t"
              "대출이자\t"
              "총상환금액\t"
              "월납입금액")

        for row in rows:
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[7]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}")

    except Exception as e:
        print("조회 중 오류 발생 :", e)

    finally:
        cursor.close()
        conn.close()

def loan_selectById():
    conn = db_connect()
    cursor = conn.cursor()

    try:
        print("\n=== 3. 1건 조회 ===")

        check_no = input("확인하실 대출번호 : ").strip()

        sql = """
        select * from car_loan where loan_no=%s
        """
        cursor.execute(sql,(check_no))

        row = cursor.fetchone()

        if row is None:
            print("해당 데이터가 없습니다.")
            return
        
        print(f"\n======= {check_no}님의 정보 =======")
        print("대출번호 : ", row[0])
        print("자동차금액 : ", row[1],"원")
        print("선수금(피값) : ", row[2],"원")
        print("대출기간(년) : ", row[7],"년")
        print("대출금액 : ", row[3],"원")
        print("대출이자 : ", row[4],"원")
        print("총상환금액 : ", row[5],"원")
        print("월납입금액 : ", row[6],"원")
        print("="*25)

    except Exception as e:
        print("조회 중 오류 발생 :", e)

    finally:
        cursor.close()
        conn.close()

def loan_update():
    conn = db_connect()
    cursor = conn.cursor()

    try:
        print("\n=== 4. 대출 수정 === ")

        check_no = input("확인하실 대출번호 : ").strip()

        check_sql = "select * from car_loan where loan_no=%s"
        cursor.execute(check_sql, (check_no))
        row = cursor.fetchone()

        if row is None:
            print("해당 계좌번호가 없습니다.")
            return

        print("\n=== 4. 수정페이지 ===")
        re_car_price = int(input("[re]자동차 금액 : "))
        re_down_payment = int(input("[re]선수금(피값) : "))
        re_loan_period = int(input("[re]대출기간(년) : "))
        if re_loan_period <0 or re_loan_period >5: 
            print("대출최대기한은 5년 입니다.")
            return

        re_loan_amount = re_car_price - re_down_payment #대출금액
        re_loan_interest = re_loan_amount * loan_inter[int(re_loan_period)] * re_loan_period #대출이자
        re_total_payment = re_loan_amount + re_loan_interest #총 상환 금액
        re_monthly_payment = re_total_payment / (re_loan_period*12) #월 납입 금액

        sql = """
        update car_loan
        set car_price=%s, down_payment=%s, loan_period=%s, loan_amount=%s, loan_interest=%s, total_payment=%s, monthly_payment=%s
        where loan_no=%s
        """
        cursor.execute(sql, (re_car_price, re_down_payment, re_loan_period, re_loan_amount, re_loan_interest, re_total_payment, re_monthly_payment, check_no))
        conn.commit()

        print(f"{re_car_price}원 / {re_down_payment}원 / {re_loan_period}년")
        print(f"{check_no}님의 정보가 수정되었습니다.")
        

    except Exception as e:
        print("수정 중 오류 발생 :", e)

    finally:
        cursor.close()
        conn.close()

def loan_delete():
    conn = db_connect()
    cursor = conn.cursor()

    try:
        print("\n=== 5. 대출 삭제 === ")

        check_no = input("삭제하실 대출번호 : ").strip()

        check_sql = "select * from car_loan where loan_no=%s"
        cursor.execute(check_sql, (check_no))
        row = cursor.fetchone()

        if row is None:
            print("해당 계좌번호가 없습니다.")
            return
        
        print("\n=== 5. 삭제페이지 ===")
        yesorno = input("정말 삭제 하시겠습니까? (y/n) : ").lower().strip()

        if yesorno != "y":
            print("삭제를 취소합니다.\n" \
                  "다시 메인화면으로 돌아갑니다.")
            return
        
        sql = """
        delete from car_loan where loan_no=%s
        """

        cursor.execute(sql, (check_no))
        conn.commit()

        print("삭제 완료!")

    except Exception as e:
        print("수정 중 오류 발생 :", e)

    finally:
        cursor.close()
        conn.close()