from flask import Flask, render_template, request
import cv2
import easyocr
import os
import re

app = Flask(__name__)

# 현재 파일 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 업로드 폴더
UPLOAD_FOLDER = os.path.join(BASE_DIR, "static")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# static 폴더가 없으면 생성
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# OCR 객체 생성
reader = easyocr.Reader(['ko', 'en'])


@app.route("/", methods=["GET", "POST"])
def home():
    # 화면에 보낼 기본값
    data = {
        "store_name": "",
        "pay_date": "",
        "card_number": "",
        "approve_number": "",
        "amount": ""
    }

    ocr_texts = []
    image_url = None
    message = ""

    if request.method == "POST":
        file = request.files.get("file")

        # 파일 선택 안 한 경우
        if not file or file.filename == "":
            message = "파일을 선택해주세요."
            return render_template(
                "index.html",
                data=data,
                ocr_texts=ocr_texts,
                image_url=image_url,
                message=message
            )

        # 업로드 파일 저장
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], "upload.png")
        file.save(filepath)

        # 화면 출력용 이미지 경로
        image_url = "/static/upload.png"

        # 이미지 읽기
        img = cv2.imread(filepath)

        if img is None:
            message = "이미지를 읽을 수 없습니다."
            return render_template(
                "index.html",
                data=data,
                ocr_texts=ocr_texts,
                image_url=image_url,
                message=message
            )

        # 흑백 변환
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # OCR 수행
        results = reader.readtext(gray)

        # OCR 결과에서 문자만 추출
        texts = [r[1] for r in results]
        ocr_texts = texts

        # 저장 변수
        store_name = ""
        pay_date = ""
        card_number = ""
        approve_number = ""
        amount = ""

        # 카드사 목록
        card_company_words = [
            "신한카드", "국민카드", "삼성카드", "현대카드",
            "롯데카드", "하나카드", "비씨카드", "우리카드", "농협카드"
        ]

        # 가맹점명 찾기
        for text in texts[:5]:
            if text not in card_company_words and "카드" not in text and len(text.strip()) >= 2:
                store_name = text
                break

        # 주요 정보 찾기
        for text in texts:
            line = text.replace(" ", "")

            # 승인일시
            if "승인일시" in line:
                pay_date = text

            # 카드번호
            elif "카드번호" in line:
                card_number = text

            # 승인번호
            elif "승인번호" in line:
                approve_number = text

            # 금액
            elif "금액" in line or "합계" in line or "결제금액" in line:
                amount = text

        # 혹시 OCR이 한 줄로 정확히 못 읽을 수 있으므로 정규식 보조 사용
        full_text = " ".join(texts)

        if pay_date == "":
            m = re.search(r"\d{4}[-./]\d{2}[-./]\d{2}\s*\d{2}:\d{2}", full_text)
            if m:
                pay_date = m.group()

        if card_number == "":
            m = re.search(r"\d{4}[-*]\d{4}[-*]\d{4}[-*]\d{4}", full_text)
            if m:
                card_number = m.group()

        if approve_number == "":
            m = re.search(r"승인번호[:\s]*([0-9]{4,})", full_text)
            if m:
                approve_number = m.group(1)

        if amount == "":
            m = re.search(r"([0-9,]+)원", full_text)
            if m:
                amount = m.group(1) + "원"

        # 결과 저장
        data["store_name"] = store_name
        data["pay_date"] = pay_date
        data["card_number"] = card_number
        data["approve_number"] = approve_number
        data["amount"] = amount
        message = "OCR 처리가 완료되었습니다."

    return render_template(
        "card.html",
        data=data,
        ocr_texts=ocr_texts,
        image_url=image_url,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)