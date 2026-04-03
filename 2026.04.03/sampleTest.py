from bs4 import BeautifulSoup

# 파일 읽기
with open("C:/Users/1Class_015/Desktop/LEEHONGJUNE/Python/Git_Self_Python/2026.04.03/sample.html", "r", encoding="utf-8") as file:
    html = file.read()

# 파싱
soup = BeautifulSoup(html, "html.parser")

# 전체 상품 가져오기
items = soup.find_all("div", class_="item")

# 결과 출력
for item in items:
    name = item.find("p", class_="name").text
    price = item.find("p", class_="price").text

    print(f"상품명: {name}, 가격: {price}")