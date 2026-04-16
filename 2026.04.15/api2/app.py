from flask import Flask, render_template, request, session
import requests
import re

from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

CLIENT_ID = "9P4eBdcCbjqH2GZiejPI"
CLIENT_SECRET = "DTYBghdO7a"

def clean_html(text):
    return re.sub(r"<.*?>", "", text)

app = Flask(__name__)

app.secret_key = '1234'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        naver = request.form.get('naver')
        url = "https://openapi.naver.com/v1/search/news.json"

        headers = {
            "X-Naver-Client-Id": CLIENT_ID,
            "X-Naver-Client-Secret": CLIENT_SECRET
        }

        params = {
            "query": naver,
            "display": 10,
            "start": 1,
            "sort": "date"
        }

        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        news = []
        for i, item in enumerate(data["items"], start=1):
            news.append({
            "title": clean_html(item["title"]),
            "link": item["link"],
            })

        session['news_data'] = news 
        session['naver_query'] = naver

        return render_template("index.html", news=news, naver=naver)
    
    return render_template("index.html")

@app.route("/wordcloud", methods=['GET', 'POST'])
def wordcloud():
    if request.method == 'POST':
        
        """
왜 cloud = index() 방식은 안 될까요?
Flask에서 @app.route가 붙은 함수는 일반적인 파이썬 함수가 아니라 View Function입니다.

반환값의 차이: index()는 뉴스 데이터(list)를 돌려주는 게 아니라, 브라우저에 뿌려줄 **HTML 코드 뭉치(Response 객체)**를 반환합니다.

상태 비저장(Stateless): HTTP 통신은 한 번 응답을 보내면 서버는 이전 작업 내용을 잊어버립니다. index 페이지를 보여준 뒤, 사용자가 버튼을 눌러 /wordcloud로 넘어오면 서버는 "아까 검색했던 게 뭐였지?"라며 백지상태가 됩니다.
        """

        cloud = index()

        naver = cloud.naver

        text_sample = cloud.news['title'].lower()

        news = session.get('news_data', [])
        naver = session.get('naver_query', '')

        text_title = " ".join([item['title'] for item in news]).lower()
            
        text_title = re.sub(r'[^가-힣a-z\s]','',text_title)

        okt = Okt()
        words = okt.nouns(text_title)

        stopwords = ['은', '는', '이', '가', '에서', '등', '매우', '을', '에', '의', '와', '과']
        words = [word for word in words if word not in stopwords]

        word_count = Counter(words)

        wc = WordCloud(font_path = "C:/windows/Fonts/malgun.ttf", # 글꼴 패치 반드시 수행해야 함
                                    background_color="white",
                                    width=800,
                                    height=400)
        wc.generate_from_frequencies(word_count) # 워드 클라우드에서 단어별 빈도수를 이용하여 생성

        plt.imshow(wc)
        plt.axis("off") # 축 제거
        plt.show()

        return render_template("index.html", naver=naver, news=news)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)