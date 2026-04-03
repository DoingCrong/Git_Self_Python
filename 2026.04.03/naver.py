import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)