import cv2, easyocr, re #re : 숫자만 추출할 때 사용
import numpy as np

#1. OCR객체 생성
reader = easyocr.Reader(['ko', 'en'], gpu=True)
#2. img 읽기
img = cv2.imread("C:/Users/1Class_015/Desktop/LEEHONGJUNE/Python/Git_Self_Python/2026.04.14/ocr/c.png")
#3. 흑백 처리
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#4. OCR 수행
result = reader.readtext(gray)

#5. 출력
print("-"*10,"전체OCR","-"*10)

for r in result:
    print(r[1])

print("-"*10,"숫자만출력","-"*10)
for r in result:
    text = r[1]

    number = re.findall(r'\d+',text)
    #\d : 자료중에 숫자값을 나타냄
    #\s : 자료중에 문자열을 나타냄

    if number:
        print("숫자 : ", number)

    score=[]

    for i in number:
        score.append(int(i))

total = sum(score[:3])
avg = total/3

print(score)
print(total)
print(avg)
