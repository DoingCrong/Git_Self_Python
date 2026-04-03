import requests
from bs4 import BeautifulSoup

code = "005930"
headers = {"User-Agent": "Mozilla/5.0"}

for page in range(1, 4):  # 1~3페이지
    url = f"https://finance.naver.com/item/sise_day.naver?code={code}&page={page}"

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    rows = soup.find_all("tr")

    for row in rows:
        cols = row.find_all("td")

        if len(cols) >= 7:
            date = cols[0].text.strip()
            close = cols[1].text.strip()

            print(f"[{page}페이지] {date} - {close}")