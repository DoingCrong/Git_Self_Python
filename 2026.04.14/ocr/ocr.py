import cv2, easyocr

import torch
print(torch.cuda.is_available())

#1. orc리더 생성/ 한국어, 영어를 읽기
reader = easyocr.Reader(['ko', 'en'], gpu=True)
#2. 이미지 읽기(같은 프로젝트 안에 img파일) #파일 못읽어오면 걍 경로 때려박기
img = cv2.imread("C:/Users/1Class_015/Desktop/LEEHONGJUNE/Python/Git_Self_Python/2026.04.14/ocr/a.png")
#3. 흑백으로 처리(단색으로 처리)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# OCR 실행
result = reader.readtext(gray)
print("-"*10)
for item in result:
    text = item[1] #인식한 문자열을 출력
    conf = item[2] #인식율(신뢰도)
    print("문자 : ", text, "/ 신뢰도", conf)