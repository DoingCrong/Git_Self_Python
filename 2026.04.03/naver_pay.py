import requests
from bs4 import BeautifulSoup

# 삼성전자 코드
code = "005930"

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

print("삼성전자 일별 종가")
print("=" * 50)

for row in rows:
    cols = row.find_all("td")

    # 데이터가 있는 행만 처리
    if len(cols) >= 7:
        date = cols[0].text.strip()
        close = cols[1].text.strip()
        update = cols[2].text.strip()

        print(f"날짜: {date}, 종가: {close}, 전일비 : {update}")