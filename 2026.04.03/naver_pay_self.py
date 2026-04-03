import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 펄어비스 코드
code = "263750"

# URL
url = f"https://finance.naver.com/item/sise_day.naver?code=263750" #종목 코드입력


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

print("펄어비스 일별 종가")
print("=" * 50)

pearlabyss = []

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

        pearlabyss.append({
            "날짜": date,
            "종가": close,
            "전일비": update,
            "등락률": min,
            "거래량": total,
            "순매매량": soon
        })

        print(f"날짜: {date}, 종가: {close}, 전일비 : {update}, 등락률 : {min}, 거래량 : {total}, 순매매량 : {soon}")


#데이터프레임
df = pd.DataFrame(pearlabyss)
df["날짜"] = pd.to_datetime(df["날짜"])
df = df.sort_values("날짜")


#그래프
plt.plot(df['날짜'], df['종가'], marker="s")
plt.title("펄어비스")
plt.xlabel("날짜")
plt.ylabel("종가")

plt.show()

