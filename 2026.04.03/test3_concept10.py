import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

already_code = {
    "삼성전자" : "005930",
    "SK하이닉스" : "000660",
    "현대차" : "005380",
    "기아" : "000270",
    "LG에너지솔루션" : "373220"
}
name_list = list(already_code.keys())

def process():
    if choice==1:
        name = name_list[0]
        code = already_code["삼성전자"]
    elif choice==2:
        for i in range(choice):
            name = name_list[choice-1]
            code = already_code.get(choice-1)
    elif choice==3:
        name = "현대차"
        code = already_code["현대차"]
    elif choice==4:
        name = "기아"
        code = already_code["기아"]
    elif choice==5:
        name = "LG에너지솔루션"
        code = already_code["LG에너지솔루션"]
    else:
        print("그건 할 수 없어요")

    # URL
    url = f"https://finance.naver.com/item/sise_day.naver?code={code}" #종목 코드입력


    # 헤더 
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    # 요청
    response = requests.get(url, headers=headers)

    # 파싱
    soup = BeautifulSoup(response.text, "html.parser")

    # 테이블 찾기
    table = soup.find("table")

    # 모든 행
    rows = table.find_all("tr")

    print(f"{name} 일별 종가")
    print("=" * 50)

    stock = []

    for row in rows:
        cols = row.find_all("td")

        # 데이터가 있는 행만 처리
        if len(cols) >= 7:
            date = cols[0].text.strip()
            close = cols[1].text.strip()
            update = cols[2].text.strip()
            min = cols[3].text.strip()
            total = cols[4].text.strip()
            soon = cols[5].text.strip()

            #리스트에 저장(그뭐냐 딕셔너리)
            stock.append({
                "날짜": date,
                "종가": close,
                "전일비": update,
                "등락률": min,
                "거래량": total,
                "순매매량": soon
            })

            print(f"날짜: {date}, 종가: {close}, 전일비 : {update}, 등락률 : {min}, 거래량 : {total}, 순매매량 : {soon}")

    #데이터프레임 저장
    df = pd.DataFrame(stock)

    #데이터 프레임을 csv파일로 저장
    df.to_csv(f"{name}[주식].csv", index=False, encoding='utf-8-sig')

    print(f"{name}[주식] / {code}[code] 을(를) csv파일로 저장완료!")

def menu():
    print("1. 삼성전자\n" \
          "2. SK하이닉스\n" \
          "3. 현대차\n" \
          "4. 기아\n" \
          "5. LG에너지솔루션\n" \
          "0. 종료")

while True:
    menu()

    try:
        choice = int(input("\n입력 : "))
    except ValueError:
        print("제발 정수만 입력하세요.")
        break

    match choice:
        case 1:
            process()
        case 2:
            process()
        case 3:
            process()
        case 4:
            process()
        case 5:
            process()
        case 0:
            print("종료종료종료")
            break
    
