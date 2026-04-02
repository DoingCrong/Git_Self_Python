import pymysql
import numpy as np
import pandas as pd

from concept5_db_config import db_connect

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
