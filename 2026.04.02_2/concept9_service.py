import pymysql
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

from concept9_db_config import db_connect

please = []

#insert
def insert():
    conn = db_connect()
    cursor = conn.cursor()

    try:
        print("\n==== 1. 입력 ====")
        trade_no = input("거래번호 : ")
        print("ex) 2099-04-25")
        trade_date = input("거래일자 : ")
        customer_name = input("거래처명 : ")
        item_name = input("품목명 : ")
        
        try:
            qty = int(input("수량 : "))
        except ValueError:
            print("정수만 입력가능합니다.")
            return None
        
        try:
            unit_price = int(input("단가 : "))
        except ValueError:
            print("정수만 입력가능합니다.")
            return None
        
        supply_amount = qty * unit_price #공급가액
        vat = supply_amount*0.1 #부가세
        total_amount = supply_amount+vat #합계금액

        #그래프 쓸때 딕셔너리가 필요할까 싶어서 집어넣음
        #나중엔 삭제할수도?
        save = {
            "거래번호" : trade_no,
            "거래일자" : trade_date,
            "거래처명" : customer_name,
            "품목명" : item_name,
            "수량" : qty,
            "단가" : unit_price,
            "공급가액" : supply_amount,
            "부가세" : vat,
            "합계금액" : total_amount
        }

        sql = """
        insert into trade_statement
        (trade_no, trade_date, customer_name, item_name, qty, unit_price, supply_amount, vat, total_amount)
        values(%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (trade_no, trade_date, customer_name, item_name, qty, unit_price, supply_amount, vat, total_amount))
        conn.commit()

        please.append(save)

        print(f"{trade_no}님 거래 명세서 작성완료!")

    #pymysql.err.IntegrityError: 
    except pymysql.err.IntegrityError:
        print("이미 존재하는 거래번호 입니다.")
    
    finally:
        cursor.close()
        conn.close()

def selectAll():
    conn = db_connect()
    cursor = conn.cursor()

    try:
        print("\n==== 2. 전체조회 ====")
        
        sql = """
        select * from trade_statement
        order by trade_date, total_amount desc
        """
        cursor.execute(sql)
        rows = cursor.fetchall()

        if len(rows) == 0:
            print("등록된 데이터가 없습니다.")
            return

        print("거래번호\t" \
              "거래일자\t" \
              "거래처명\t" \
              "품목명\t" \
              "수량\t" \
              "단가\t" \
              "공급가액\t" \
              "부가세\t" \
              "합계금액")
        
        for row in rows:
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}\t{row[7]}\t{row[8]}")

    except Exception as e:
        print("조회 중 오류 발생 :", e)

    finally:
        cursor.close()
        conn.close()

def selectById():
    conn = db_connect()
    cursor = conn.cursor()

    try:
        print("\n==== 3. 거래번호 조회 ====")

        check_no = input("검색하실 거래번호 : ").strip()

        check_sql = """
        select * from trade_statement
        where trade_no=%s
        """
        cursor.execute(check_sql,(check_no))

        row = cursor.fetchone()

        if row is None:
            print("해당 데이터가 존재하지 않습니다.")
            return
        
        print(f"======== {check_no}님의 정보 ========")
        print("거래번호 : ",row[0])
        print("거래일자 : ",row[1])
        print("거래처명 : ",row[2])
        print("품목명 : ",row[3])
        print("수량 : ",row[4])
        print("단가 : ",row[5])
        print("공급가액 : ",row[6])
        print("부가세 : ",row[7])
        print("합계금액 : ",row[8])
        print("="*25)

    except Exception as e:
        print("조회 중 오류 발생 :", e)

    finally:
        cursor.close()
        conn.close()

def update():
    conn = db_connect()
    cursor = conn.cursor()

    try:
        print("\n==== 4. 수정 ====")
        check_no = input("검색하실 거래번호 : ").strip()

        check_sql = """
        select * from trade_statement
        where trade_no=%s
        """
        cursor.execute(check_sql,(check_no))

        row = cursor.fetchone()

        if row is None:
            print("해당 데이터가 존재하지 않습니다.")
            return
        
        print("\n==== 수정페이지 ====")

        print("ex) 2099-04-25")
        trade_date = input("거래일자 : ")
        customer_name = input("거래처명 : ")
        item_name = input("품목명 : ")
        
        try:
            qty = int(input("수량 : "))
        except ValueError:
            print("정수만 입력가능합니다.")
            return None
        
        try:
            unit_price = int(input("단가 : "))
        except ValueError:
            print("정수만 입력가능합니다.")
            return None
        
        supply_amount = qty * unit_price #공급가액
        vat = supply_amount*0.1 #부가세
        total_amount = supply_amount+vat #합계금액

        #그래프 쓸때 딕셔너리가 필요할까 싶어서 집어넣음
        #update에서는 뭘 바꾸더라?
        save = {
            #"거래번호" : trade_no,
            "거래일자" : trade_date,
            "거래처명" : customer_name,
            "품목명" : item_name,
            "수량" : qty,
            "단가" : unit_price,
            "공급가액" : supply_amount,
            "부가세" : vat,
            "합계금액" : total_amount
        }

        sql = """
        update trade_statement
        set trade_date=%s, customer_name=%s, item_name=%s, qty=%s, unit_price=%s, supply_amount=%s, vat=%s, total_amount=%s
        where trade_no=%s
        """
        cursor.execute(sql, (trade_date, customer_name, item_name, qty, unit_price, supply_amount, vat, total_amount, check_no))
        conn.commit()

        please.append(save)

        print(f"{check_no}님의 정보가 수정되었습니다.")

    except Exception as e:
        print("수정 중 오류 발생 :", e)

    finally:
        cursor.close()
        conn.close()

def delete():
    conn = db_connect()
    cursor = conn.cursor()

    try:
        print("\n==== 5. 삭제 ====")
        check_no = input("검색하실 거래번호 : ").strip()

        check_sql = """
        select * from trade_statement
        where trade_no=%s
        """
        cursor.execute(check_sql,(check_no))

        row = cursor.fetchone()

        if row is None:
            print("해당 데이터가 존재하지 않습니다.")
            return
        
        print("\n==== 삭제페이지 ====")

        yesorno = input("정말 삭제 하시겠습니까? (y/n) : ").lower().strip()

        if yesorno != "y":
            print("삭제를 취소합니다.\n" \
                  "다시 메인화면으로 돌아갑니다.")
            return
        
        sql="""
        delete from trade_statement
        where trade_no=%s
        """
        cursor.execute(sql,(check_sql))
        conn.commit()

        print("삭제 완료!")

    except Exception as e:
        print("수정 중 오류 발생 :", e)

    finally:
        cursor.close()
        conn.close()

def graph():
    conn = db_connect()
    try:
        print("\n==== 6. 그래프 ====")
        df = pd.read_sql("SELECT * FROM trade_statement", conn)

        if df.empty:
            print("해당 데이터가 존재하지 않습니다.")
            return

        print("\n==== 차트페이지 ====")
        print("1. 그룹 기준: 1)거래처명 2)품목명 3)거래일자")
        group = input("선택: ")
        group_cols = {"1": "customer_name", "2": "item_name", "3": "trade_date"}
        group_col = group_cols.get(group, "customer_name")

        print("\n2. 집계 항목: 1)수량 2)공급가액 3)부가세 4)합계금액")
        v_idx = input("선택: ")
        val_cols = {"1": "qty", "2": "supply_amount", "3": "vat", "4": "total_amount"}
        val_col = val_cols.get(v_idx, "total_amount")

        print("\n3. 집계 방식: 1)합계 2)평균 3)개수")
        f_idx = input("선택: ")

        func_map = {"1": np.sum, "2": np.mean, "3": len}
        func_label = {"1": "합계", "2": "평균", "3": "개수"}
        agg_func = func_map.get(f_idx, np.sum)

        print("\n4. 차트 종류: 1)막대그래프 2)선그래프")
        c_idx = input("선택: ")

        result_df = df.groupby(group_col)[val_col].agg(agg_func)


        title = f"{group_col}별 {val_col} {func_label.get(f_idx, '합계')}"
        if c_idx == "2":
            result_df.plot(kind='line', marker='o', figsize=(10, 5))
        else:
            result_df.plot(kind='bar', figsize=(10, 5))

        plt.title(title)
        plt.ylabel(val_col)
        plt.grid(True, axis='y', linestyle='--', alpha=0.7)
        plt.show()

    except Exception as e:
        print(f"오류 발생: {e}")
    finally:
        conn.close()
