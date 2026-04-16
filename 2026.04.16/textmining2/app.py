from flask import Flask, render_template, request
import requests
import re

CLIENT_ID = "9P4eBdcCbjqH2GZiejPI"
CLIENT_SECRET = "DTYBghdO7a"

def clean_html(text):
    return re.sub(r"<.*?>", "", text)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# positive_words =['상승','기대','호재','실적개선','회복','성장'] #긍정적인
# negative_words = ['하락','악재','적자','감소','위기','손실']    #부정적인

positive_words =[] #긍정적인
negative_words = [] #부정적인

@app.route("/index", methods=['POST', 'GET'])
def index():
    if request.method=='POST':
        naver = request.form.get('naver')
        positive = request.form.getlist('positive')
        negative = request.form.get('negative')

        positive_words = positive
        negative_words = [negative]

        url = "https://openapi.naver.com/v1/search/news.json"
        
        headers = {
            "X-Naver-Client-Id": CLIENT_ID,
            "X-Naver-Client-Secret": CLIENT_SECRET
        }

        params = {
            "query": naver,
            "display": 50,
            "start": 1,
            "sort": "date"
        }

        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        score=0
        use=[]
        news = []
        for i, item in enumerate(data["items"], start=1):
            clean_title = clean_html(item["title"])
            news.append({
            "title": clean_title,
            "link": item["link"],
            })

            words = re.findall(r'\w+', clean_title)

            for word in words:
                if word in positive_words:
                    score+=1
                elif word in negative_words:
                    score-=1

        if score>0:
            result = "상승"
        elif score<0:
            result = "하락"
        else:
            result = "중립"

        use = {
            "result":result,
            "score":score
        }
        
        return render_template("index.html", news=news, naver=naver, use=use)
    
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)