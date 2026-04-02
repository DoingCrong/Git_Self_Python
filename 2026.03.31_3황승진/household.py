import numpy as np
import pymysql
from db_config import db_connect


def input_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("   숫자만 입력하세요.")


def input_trade_type():
    while True:
        t = input("거래구분 (수입/지출) : ").strip()
        if t in ("수입", "지출"):
            return t
        print("   '수입' 또는 '지출'만 입력 가능합니다.")


def create_trade():
    conn   = db_connect()
    cursor = conn.cursor()
    try:
        print("\n[ 거래 등록 ]")
        trade_no   = input("거래번호 : ").strip()
        trade_type = input_trade_type()
        item_name  = input("항목명   : ").strip()
        amount     = input_int("금액     : ")
        trade_date = input("거래일자 : ").strip()
        memo       = input("내용     : ").strip()

        sql = "insert into household_book values(%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (trade_no, trade_type, item_name, amount, trade_date, memo))
        conn.commit()
        print("   거래 등록 완료")

    except pymysql.err.IntegrityError:
        print("   이미 존재하는 거래번호입니다.")
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
        cursor.execute("select * from household_book order by trade_no")
        rows = cursor.fetchall()

        if not rows:
            print("  등록된 거래가 없습니다.")
            return

        print("-" * 80)
        print(f"  {'거래번호':<12} {'구분':<6} {'항목명':<12} {'금액':>10} {'거래일자':<12} {'내용'}")
        print("-" * 80)
        for row in rows:
            print(f"  {row[0]:<12} {row[1]:<6} {row[2]:<12} {row[3]:>10,} {row[4]:<12} {row[5]}")
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
        trade_no = input("거래번호 : ").strip()
        cursor.execute("select * from household_book where trade_no=%s", (trade_no,))
        row = cursor.fetchone()

        if row is None:
            print("   해당 거래번호가 없습니다.")
            return

        print("-" * 40)
        print(f"  거래번호 : {row[0]}")
        print(f"  거래구분 : {row[1]}")
        print(f"  항목명   : {row[2]}")
        print(f"  금액     : {row[3]:,}원")
        print(f"  거래일자 : {row[4]}")
        print(f"  내용     : {row[5]}")
        print("-" * 40)

    except Exception as e:
        print("  오류 발생 :", e)
    finally:
        cursor.close()
        conn.close()


def update_trade():
    conn   = db_connect()
    cursor = conn.cursor()
    try:
        print("\n[ 거래 수정 ]")
        trade_no = input("거래번호 : ").strip()
        cursor.execute("select * from household_book where trade_no=%s", (trade_no,))
        row = cursor.fetchone()

        if row is None:
            print("   해당 거래번호가 없습니다.")
            return

        print("  새 정보를 입력하세요.")
        trade_type = input_trade_type()
        item_name  = input("항목명   : ").strip()
        amount     = input_int("금액     : ")
        trade_date = input("거래일자 : ").strip()
        memo       = input("내용     : ").strip()

        sql = """update household_book
                 set trade_type=%s, item_name=%s, amount=%s, trade_date=%s, memo=%s
                 where trade_no=%s"""
        cursor.execute(sql, (trade_type, item_name, amount, trade_date, memo, trade_no))
        conn.commit()
        print("   거래 수정 완료")

    except Exception as e:
        print("  오류 발생 :", e)
    finally:
        cursor.close()
        conn.close()


def delete_trade():
    conn   = db_connect()
    cursor = conn.cursor()
    try:
        print("\n[ 거래 삭제 ]")
        trade_no = input("거래번호 : ").strip()
        cursor.execute("select * from household_book where trade_no=%s", (trade_no,))
        row = cursor.fetchone()

        if row is None:
            print("   해당 거래번호가 없습니다.")
            return

        confirm = input(f"  '{row[2]}' 거래를 삭제하시겠습니까? (y/n) : ").strip().lower()
        if confirm != "y":
            print("  삭제 취소")
            return

        cursor.execute("delete from household_book where trade_no=%s", (trade_no,))
        conn.commit()
        print("   거래 삭제 완료")

    except Exception as e:
        print("  오류 발생 :", e)
    finally:
        cursor.close()
        conn.close()


def show_stats():
    conn   = db_connect()
    cursor = conn.cursor()
    try:
        print("\n[ 통계 조회 ]")

        cursor.execute("select amount from household_book where trade_type='수입'")
        income_rows = cursor.fetchall()

        cursor.execute("select amount from household_book where trade_type='지출'")
        expense_rows = cursor.fetchall()

        income_arr  = np.array([r[0] for r in income_rows]) if income_rows  else np.array([0])
        expense_arr = np.array([r[0] for r in expense_rows]) if expense_rows else np.array([0])

        total_income  = int(np.sum(income_arr))
        total_expense = int(np.sum(expense_arr))
        balance       = total_income - total_expense
        avg_income    = float(np.mean(income_arr))
        avg_expense   = float(np.mean(expense_arr))
        max_income    = int(np.max(income_arr))
        max_expense   = int(np.max(expense_arr))

        print("-" * 40)
        print(f"  총 수입     : {total_income:>15,}원")
        print(f"  총 지출     : {total_expense:>15,}원")
        print(f"  최종 잔액   : {balance:>15,}원")
        print(f"  수입 평균   : {avg_income:>15,.1f}원")
        print(f"  지출 평균   : {avg_expense:>15,.1f}원")
        print(f"  최대 수입   : {max_income:>15,}원")
        print(f"  최대 지출   : {max_expense:>15,}원")
        print("-" * 40)

    except Exception as e:
        print("  오류 발생 :", e)
    finally:
        cursor.close()
        conn.close()