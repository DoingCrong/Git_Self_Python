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
