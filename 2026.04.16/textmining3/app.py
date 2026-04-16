# -*- coding: utf-8 -*-
"""
기능:
1. 회사명 입력
2. corp_code 찾기
3. 재무제표 가져오기
4. 필요한 항목만 추출
5. CSV 저장

추출 항목:
- 매출액
- 영업이익
- 당기순이익
"""

import requests #인터넷에서 데이터 가져오는 라이브러리
import zipfile #압축 파일 열기
import io #메모리에서 파일 처럼 사용
import xml.etree.ElementTree as ET #xml파일 분석 라이브러리
import pandas as pd

# 본인 API KEY 입력
API_KEY = "45074dbef1f1fbfb86b5b8c488909540da773ddb"



# 1. 회사명 조회

def get_corp_code(company_name):

    url = "https://opendart.fss.or.kr/api/corpCode.xml"
    params = {"crtfc_key": API_KEY}

    res = requests.get(url, params=params)

    z = zipfile.ZipFile(io.BytesIO(res.content))
       #다트 사이트에서 제공하는 파일은 압축(zip)파일이라서 현 메모리에서
        #풀어서 사용하도록 함.
    xml_data = z.read(z.namelist()[0])
    root = ET.fromstring(xml_data)

    for item in root.findall("list"):
        name = item.findtext("corp_name")

        #  완전 일치로 변경
        if company_name == name:
            print("찾은 회사:", name)
            return item.findtext("corp_code")

    return None



# 2. 재무제표 가져오기

def get_finance(corp_code, year):
    """
    재무제표 전체 가져오기
    """

    url = "https://opendart.fss.or.kr/api/fnlttSinglAcntAll.json"

    params = {
        "crtfc_key": API_KEY,
        "corp_code": corp_code,
        "bsns_year": str(year),
        "reprt_code": "11011",  # 사업보고서
        "fs_div": "OFS"         # 연결재무제표
    }

    res = requests.get(url, params=params)
    data = res.json()
    print("응답확인 :", data)

    # 오류 처리
    if data["status"] != "000":
        print("데이터 없음")
        return pd.DataFrame()

    return pd.DataFrame(data["list"])



# 3. 필요한 항목만 추출

def extract_data(df):
    """
    매출액, 영업이익, 당기순이익만 추출
    """

    result = {}

    # 반복문으로 계정 찾기
    for _, row in df.iterrows():
        name = row["account_nm"]

        # 매출액
        if "매출액" in name:
            result["매출액"] = row["thstrm_amount"]

        # 영업이익
        elif "영업이익" in name:
            result["영업이익"] = row["thstrm_amount"]

        # 당기순이익
        elif "당기순이익" in name:
            result["당기순이익"] = row["thstrm_amount"]

    return result


# 4. 실행

def main():
    company = input("회사명 입력: ")
    year = input("연도 입력 (예: 2026): ")

    # corp_code 찾기
    corp_code = get_corp_code(company)

    if not corp_code:
        print("회사 찾기 실패")
        return

    print("corp_code:", corp_code)

    # 재무제표 가져오기
    df = get_finance(corp_code, year)

    if df.empty:
        print("재무 데이터 없음")
        return

    # 필요한 데이터 추출
    data = extract_data(df)

    if not data:
        print("원하는 데이터 없음")
        return

    # DataFrame 생성
    result_df = pd.DataFrame([data])

    # CSV 저장
    file_name = f"{company}_{year}_재무요약.csv"
    result_df.to_csv(file_name, index=False, encoding="utf-8-sig")

    print("저장 완료:", file_name)
    print(result_df)



# 5. 시작

if __name__ == "__main__":
    main()