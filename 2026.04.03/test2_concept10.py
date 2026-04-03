from bs4 import BeautifulSoup

# 파일 읽기
with open("C:/Users/1Class_015/Desktop/LEEHONGJUNE/Python/Git_Self_Python/2026.04.03/test2_concept10.html", "r", encoding="utf-8") as file:
    html = file.read()

# 파싱
soup = BeautifulSoup(html, "html.parser")

# 전체 상품 가져오기
items = soup.find_all("table", class_="join")

# 결과 출력
for item in items:
    test1 = item.find("option", id="select").text
    test2 = item.find("input", id="name").text
    test3 = item.find("input", id="password").text
    test4 = item.find("option", id="codding").text
    test5 = item.find("option", id="music").text

    if not (test2): #값이 진짜 없는지 있는지 사용
        test2 = "비어있습니다."

    if test3 is None: #null체크용도로 사용해야함 : null도값이다
        test3 = "비어있습니다."
    else:
        test3 = "null도 값이다."

    print(f"문구1: {test1}\n문구2: {test2}\n문구3: {test3}\n문구4: {test4}\n문구5: {test5}")