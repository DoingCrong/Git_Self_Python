import pymysql
import numpy as np

from deal_db_config import db_connect

#deal_insert
def deal_insert():
    conn = db_connect()
    cursor = conn.cursor()

    try:
        print("\n==== 1. 거래 등록 ====")
        trade_no = input("거래번호 : ")

        trade_type = input("거래구분(수입/지출) : ").strip()
        if trade_type!="수입" and trade_type!="지출":
            print("\"수입 혹은 지출만 가능합니다.\"")
            return
        
        print("\n ex)월급,식비...")
        item_name = input("항목명 : ")

        while True:
            try:
                amount_input = input("금액 : ")
                amount = int(amount_input)
                break  
            except ValueError:
                print("Error : 금액은 숫자만 입력 가능합니다. 다시 입력해주세요.")

        print("\n ex) 2099-03-20")
        trade_date = input("거래일자 : ")
        memo = input("내용 : ")

        sql = """
        insert into household_book
        (trade_no, trade_type, item_name, amount, trade_date, memo)
        values(%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (trade_no, trade_type, item_name, amount, trade_date, memo))
        conn.commit()

        print(f"{trade_no}님 {trade_type} 가계부 작성 완료!")

    #pymysql.err.IntegrityError: 
    except pymysql.err.IntegrityError:
        print("이미 존재하는 거래번호 입니다.")
    
    finally:
        cursor.close()
        conn.close()

#deal_selectAll
def deal_selectAll():
    conn = db_connect()
    cursor = conn.cursor()

    try:
        print("\n==== 2. 전체 조회 ====")

        sql = """
        select * from household_book order by trade_type, trade_date desc
        """
        cursor.execute(sql)

        rows = cursor.fetchall()

        if len(rows) == 0:
            print("등록된 데이터가 없습니다.")

        print("거래번호  거래구분  항목명  금액 \t 거래일자  내용")

        for row in rows:
            print(f"{row[0]} \t {row[1]} \t {row[2]} \t {row[3]} \t {row[4]} \t {row[5]}")

    except Exception as e:
        print("조회 중 오류 발생 :", e)

    finally:
        cursor.close()
        conn.close()

#deal_selectById
def deal_selectById():
    conn = db_connect()
    cursor = conn.cursor()

    try:
        print("\n==== 3. 1건 조회 ====")

        check_no = input("조회하실 거래번호 : ").strip()

        check_sql = """
        select * from household_book where trade_no=%s
        """
        cursor.execute(check_sql,(check_no))

        row = cursor.fetchone()

        if row is None:
            print("해당 데이터가 존재하지 않습니다.")
            return
        
        print(f"\n======= {check_no}님의 정보 =======")
        print("거래번호 : ", row[0])
        print("거래구분(수입/지출) : ", row[1])
        print("항목명 : ", row[2])
        print("금액 : ", row[3],"원")
        print("거래일자 : ", row[4])
        print("내용 : ", row[5])
        print("="*25)

    except Exception as e:
        print("조회 중 오류 발생 :", e)

    finally:
        cursor.close()
        conn.close()

#deal_update
def deal_update():
    conn = db_connect()
    cursor = conn.cursor()

    try:
        print("\n==== 4. 거래 수정 ====")

        check_no = input("조회하실 거래번호 : ").strip()

        check_sql = """
        select * from household_book where trade_no=%s
        """
        cursor.execute(check_sql,(check_no))

        row = cursor.fetchone()

        if row is None:
            print("해당 데이터가 존재하지 않습니다.")
            return
        
        print("\n==== 4. 수정 페이지 ====")

        trade_type = input("거래구분(수입/지출) : ").strip()
        if trade_type!="수입" and trade_type!="지출":
            print("\"수입 혹은 지출만 가능합니다.\"")
            return
        
        print("\n ex)월급,식비...")
        item_name = input("항목명 : ")

        while True:
            try:
                amount_input = input("금액 : ")
                amount = int(amount_input)
                break  
            except ValueError:
                print("Error : 금액은 숫자만 입력 가능합니다. 다시 입력해주세요.")

        print("\n ex) 2099-03-20")
        trade_date = input("거래일자 : ")
        memo = input("내용 : ")

        sql = """
        update household_book
        set trade_type=%s, item_name=%s, amount=%s, trade_date=%s, memo=%s
        where trade_no=%s
        """
        cursor.execute(sql, (trade_type, item_name, amount, trade_date, memo, check_no))
        conn.commit()

        print(f"{check_no}님의 정보가 수정되었습니다.")

    except Exception as e:
        print("수정 중 오류 발생 :", e)

    finally:
        cursor.close()
        conn.close()

#deal_delete
def deal_delete():
    conn = db_connect()
    cursor = conn.cursor()

    try:
        print("\n==== 5. 거래 삭제 ====")

        check_no = input("조회하실 거래번호 : ").strip()

        check_sql = """
        select * from household_book where trade_no=%s
        """
        cursor.execute(check_sql,(check_no))

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
        delete from household_book where trade_no=%s
        """

        cursor.execute(sql, (check_no))
        conn.commit()

        print("삭제 완료!")

    except Exception as e:
        print("수정 중 오류 발생 :", e)

    finally:
        cursor.close()
        conn.close()



#deal_data
def deal_data():
    conn = db_connect()
    cursor = conn.cursor()

    try:
        print("\n==== 6. 통계 조회 ====")

        sql = "select trade_type, amount from household_book" #타입과 금액만을 select 한다.
        cursor.execute(sql)
        rows = cursor.fetchall()

        min = []
        plus = []

        for row in rows:
            if row[0]!="수입":
                min.append(row[1])
            elif row[0]=="수입":
                plus.append(row[1])

        min_np = np.array(min)
        plus_np = np.array(plus)

        print("\n==== 수입 통계 ====")
        print("수입 합계 : ", np.sum(plus_np))
        print("수입 평균 : ", round(np.mean(plus_np),2))
        print("수입 최대값 : ", np.max(plus_np))
        print("수입 최소값 : ", np.min(plus_np))
        print()
        print("\n==== 지출 통계 ====")
        print("지출 합계 : ", np.sum(min_np))
        print("지출 평균 : ", round(np.mean(min_np),2))
        print("지출 최대값 : ", np.max(min_np))
        print("지출 최소값 : ", np.min(min_np))

    except Exception as e:
        print("수정 중 오류 발생 :", e)

    finally:
        cursor.close()
        conn.close()