import numpy as np
import pymysql
from db_config import db_connect

RATES = np.array([0.0, 0.05, 0.055, 0.06, 0.065, 0.07])

def input_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("   숫자만 입력하세요.")

def input_period():
    while True:
        period = input_int("대출기간(1~5년) : ")
        if 1 <= period <= 5:
            return period
        print("   대출기간은 1년~5년만 가능합니다.")

def calc_loan(car_price, down_payment, period):
    loan_amount    = car_price - down_payment
    loan_interest  = int(loan_amount * RATES[period] * period)
    total_payment  = loan_amount + loan_interest
    monthly_payment = int(total_payment / (period * 12))
    return loan_amount, loan_interest, total_payment, monthly_payment

def create_loan():
    conn   = db_connect()
    cursor = conn.cursor()
    try:
        print("\n[ 대출 등록 ]")
        loan_no      = input("대출번호 : ").strip()
        car_price    = input_int("자동차 금액 : ")
        down_payment = input_int("선수금 : ")

        if down_payment >= car_price:
            print("   선수금이 자동차 금액보다 클 수 없습니다.")
            return

        period = input_period()
        loan_amount, loan_interest, total_payment, monthly_payment = calc_loan(car_price, down_payment, period)

        print(f"\n  대출금액    : {loan_amount:,}원")
        print(f"  연이율      : {RATES[period]*100:.1f}%")
        print(f"  대출이자    : {loan_interest:,}원")
        print(f"  총상환금액  : {total_payment:,}원")
        print(f"  월불입금액  : {monthly_payment:,}원")

        sql = "insert into car_loan values(%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (loan_no, car_price, down_payment, loan_amount,
                             loan_interest, total_payment, monthly_payment, period))
        conn.commit()
        print("   대출 등록 완료")

    except pymysql.err.IntegrityError:
        print("   이미 존재하는 대출번호입니다.")
    except Exception as e:
        print("  오류 발생 :", e)
    finally:
        cursor.close()
        conn.close()

def select_all():
    conn   = db_connect()
    cursor = conn.cursor()
    try:
        print("\n[ 전체 조회 ]")
        cursor.execute("select * from car_loan order by loan_no")
        rows = cursor.fetchall()

        if not rows:
            print("  등록된 대출이 없습니다.")
            return

        print("-" * 80)
        print(f"  {'대출번호':<12} {'차량금액':>12} {'선수금':>10} {'대출금액':>12} {'월불입금':>12} {'기간':>5}")
        print("-" * 80)
        for row in rows:
            print(f"  {row[0]:<12} {row[1]:>12,} {row[2]:>10,} {row[3]:>12,} {row[6]:>12,} {row[7]:>4}년")
        print("-" * 80)

    except Exception as e:
        print("  오류 발생 :", e)
    finally:
        cursor.close()
        conn.close()

def select_one():
    conn   = db_connect()
    cursor = conn.cursor()
    try:
        print("\n[ 1건 조회 ]")
        loan_no = input("대출번호 : ").strip()
        cursor.execute("select * from car_loan where loan_no=%s", (loan_no,))
        row = cursor.fetchone()

        if row is None:
            print("   해당 대출번호가 없습니다.")
            return

        print("-" * 40)
        print(f"  대출번호   : {row[0]}")
        print(f"  자동차금액 : {row[1]:,}원")
        print(f"  선수금     : {row[2]:,}원")
        print(f"  대출금액   : {row[3]:,}원")
        print(f"  대출이자   : {row[4]:,}원")
        print(f"  총상환금액 : {row[5]:,}원")
        print(f"  월불입금액 : {row[6]:,}원")
        print(f"  대출기간   : {row[7]}년 ({RATES[row[7]]*100:.1f}%)")
        print("-" * 40)

    except Exception as e:
        print("  오류 발생 :", e)
    finally:
        cursor.close()
        conn.close()

def update_loan():
    conn   = db_connect()
    cursor = conn.cursor()
    try:
        print("\n[ 대출 수정 ]")
        loan_no = input("대출번호 : ").strip()
        cursor.execute("select * from car_loan where loan_no=%s", (loan_no,))
        row = cursor.fetchone()

        if row is None:
            print("   해당 대출번호가 없습니다.")
            return

        print("  새 정보를 입력하세요.")
        car_price    = input_int("자동차 금액 : ")
        down_payment = input_int("선수금 : ")

        if down_payment >= car_price:
            print("   선수금이 자동차 금액보다 클 수 없습니다.")
            return

        period = input_period()
        loan_amount, loan_interest, total_payment, monthly_payment = calc_loan(car_price, down_payment, period)

        sql = """update car_loan set car_price=%s, down_payment=%s, loan_amount=%s,
                 loan_interest=%s, total_payment=%s, monthly_payment=%s, loan_period=%s
                 where loan_no=%s"""
        cursor.execute(sql, (car_price, down_payment, loan_amount,
                             loan_interest, total_payment, monthly_payment, period, loan_no))
        conn.commit()
        print("   대출 수정 완료")

    except Exception as e:
        print("  오류 발생 :", e)
    finally:
        cursor.close()
        conn.close()

def delete_loan():
    conn   = db_connect()
    cursor = conn.cursor()
    try:
        print("\n[ 대출 삭제 ]")
        loan_no = input("대출번호 : ").strip()
        cursor.execute("select * from car_loan where loan_no=%s", (loan_no,))
        row = cursor.fetchone()

        if row is None:
            print("   해당 대출번호가 없습니다.")
            return

        confirm = input(f"  '{loan_no}' 대출을 삭제하시겠습니까? (y/n) : ").strip().lower()
        if confirm != "y":
            print("  삭제 취소")
            return

        cursor.execute("delete from car_loan where loan_no=%s", (loan_no,))
        conn.commit()
        print("   대출 삭제 완료")

    except Exception as e:
        print("  오류 발생 :", e)
    finally:
        cursor.close()
        conn.close()