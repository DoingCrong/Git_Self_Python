from flask import Flask, render_template, request
from collections import Counter
from konlpy.tag import Okt
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import requests
import re
import os

app = Flask(__name__)

CLIENT_ID = "P1MyL7VuYDrHjbRS1eGL"
CLIENT_SECRET = "E2E1PlNNMG"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_FOLDER = os.path.join(BASE_DIR, "static")
os.makedirs(STATIC_FOLDER, exist_ok=True)

okt = Okt()


def clean_html(text):
    return re.sub(r"<.*?>", "", text)


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^가-힣a-z\s]", " ", text)
    return text


def extract_words(text):
    stopwords = [
        "기자", "뉴스", "연합뉴스", "뉴시스", "사진", "영상",
        "관련", "지난", "이번", "오늘", "오전", "오후",
        "때문", "정도", "통해", "현재", "이날", "대한",
        "에서", "으로", "했다", "있다", "없다"
    ]

    cleaned = clean_text(text)
    words = okt.nouns(cleaned)
    words = [word for word in words if len(word) >= 2 and word not in stopwords]
    return words


def get_news(query):
    url = "https://openapi.naver.com/v1/search/news.json"

    headers = {
        "X-Naver-Client-Id": CLIENT_ID,
        "X-Naver-Client-Secret": CLIENT_SECRET
    }

    params = {
        "query": query,
        "display": 20,
        "start": 1,
        "sort": "date"
    }

    response = requests.get(url, headers=headers, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    news_list = []
    for i, item in enumerate(data.get("items", []), start=1):
        news_list.append({
            "no": i,
            "title": clean_html(item.get("title", "")),
            "description": clean_html(item.get("description", "")),
            "link": item.get("link", ""),
            "pubDate": item.get("pubDate", "")
        })

    return news_list


def make_bar_plot(top_words):
    if not top_words:
        return None

    image_path = os.path.join(STATIC_FOLDER, "barplot.png")

    plt.rc("font", family="Malgun Gothic")
    plt.rcParams["axes.unicode_minus"] = False

    words = [word for word, count in top_words]
    counts = [count for word, count in top_words]

    plt.figure(figsize=(10, 5))
    plt.bar(words, counts, color="skyblue")
    plt.title("뉴스 키워드 빈도수")
    plt.xlabel("단어")
    plt.ylabel("빈도수")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(image_path)
    plt.close()

    return "barplot.png"


def make_wordcloud(word_count):
    if not word_count:
        return None

    image_path = os.path.join(STATIC_FOLDER, "wordcloud.png")

    wc = WordCloud(
        font_path="C:/Windows/Fonts/malgun.ttf",
        background_color="white",
        width=900,
        height=450
    )

    wc.generate_from_frequencies(word_count)

    plt.figure(figsize=(12, 6))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(image_path)
    plt.close()

    return "wordcloud.png"


@app.route("/", methods=["GET", "POST"])
def index():
    query = ""
    news_list = []
    top_words = []
    barplot_file = None
    wordcloud_file = None
    error = None

    if request.method == "POST":
        query = request.form.get("query", "").strip()

        if not query:
            error = "검색어를 입력하세요."
        else:
            try:
                news_list = get_news(query)

                if not news_list:
                    error = "검색 결과가 없습니다."
                else:
                    combined_text = " ".join(
                        news["title"] + " " + news["description"]
                        for news in news_list
                    )

                    words = extract_words(combined_text)
                    word_count = Counter(words)
                    top_words = word_count.most_common(10)

                    if word_count:
                        barplot_file = make_bar_plot(top_words)
                        wordcloud_file = make_wordcloud(word_count)

            except requests.RequestException as e:
                error = f"뉴스 검색 중 오류가 발생했습니다: {e}"

    return render_template(
        "index.html",
        query=query,
        news_list=news_list,
        top_words=top_words,
        barplot_file=barplot_file,
        wordcloud_file=wordcloud_file,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
