import requests
import re

#네이버 발급받은 실제 값
CLIENT_ID = "9P4eBdcCbjqH2GZiejPI"
CLIENT_SECRET = "DTYBghdO7a"

def clean_html(text):
    return re.sub(r"<.*?>","",text)
    

def get_news(query):
    url = "https://openapi.naver.com/v1/search/news.json"
    
    headers = {
        "X-Naver-Client-Id": CLIENT_ID,
        "X-Naver-Client-Secret": CLIENT_SECRET
    }

    params = {
        "query": query,
        "display": 50,
        "start": 1,
        "sort": "date"
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    # 만약 결과에 'items'가 없으면 서버가 보낸 에러 메시지를 출력함
    if "items" not in data:
        print("네이버 API에서 보낸 에러 응답:", data)
        return

    print(f"검색어 : {query}")
    print("-" * 50)
    
    for i, item in enumerate(data["items"], start=1):
        title = clean_html(item["title"])
        link = item["link"]
        print(f"{i}. {title}")
        print(f" 링크 주소 : {link}\n")
    
query = input("검색어를 입력 하세요 : ")
get_news(query)