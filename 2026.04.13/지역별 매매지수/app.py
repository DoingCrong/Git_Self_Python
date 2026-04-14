# Flask에서 필요한 기능 불러오기
# Flask           : 웹 프로그램을 만들기 위한 기본 클래스
# render_template : HTML 파일을 화면에 출력할 때 사용
# request         : 사용자가 form으로 보낸 값을 받아올 때 사용
from flask import Flask, render_template, request

# Flask 객체 생성
# __name__ 은 현재 실행 중인 파이썬 파일 이름을 의미
app = Flask(__name__)

# 읽어올 CSV 파일 이름
CSV_FILE = "아파트.csv"


def load_data():
    """
    CSV 파일을 읽어서
    지역명과 월별 가격 정보를 리스트 형태로 만들어 반환하는 함수

    반환값 예시:
    data_list = [
        {
            "region": "강남구",
            "months": {
                "2025년 1월": 1000.0,
                "2025년 2월": 1100.0
            }
        },
        ...
    ]

    month_cols = ["2025년 1월", "2025년 2월", ...]
    """

    # CSV의 모든 데이터를 저장할 리스트
    data_list = []

    # CSV 파일 열기
    # "r" : 읽기 모드
    # encoding="cp949" : 한글 CSV 파일 인코딩
    with open(CSV_FILE, "r", encoding="cp949") as file:

        # 파일의 각 줄을 읽어서
        # 양쪽 공백/줄바꿈 제거 후
        # 쉼표(,) 기준으로 잘라서 리스트로 만듦
        #
        # 예:
        # "1,서울,강남구,1000,1100"
        # ->
        # ["1", "서울", "강남구", "1000", "1100"]
        rows = [line.strip().split(",") for line in file]

    # 첫 번째 줄은 컬럼명(헤더)이므로 따로 저장
    header = rows[0]

    # 실제 데이터는 3번째 줄부터 시작
    # rows[0] : 헤더
    # rows[1] : 불필요한 중복/설명 행
    # rows[2]부터 실제 데이터
    rows = rows[2:]

    # 월 이름들을 저장할 리스트
    # 예: ["2025년 1월", "2025년 2월", ...]
    month_cols = []

    # 위 월 이름들이 CSV에서 몇 번째 칼럼인지 저장할 리스트
    # 예: [3, 4, 5, 6, ...]
    month_idx = []

    # 헤더를 하나씩 검사하면서
    # "년" 과 "월" 이 들어간 칼럼만 찾아냄
    for i in range(len(header)):
        if "년" in header[i] and "월" in header[i]:
            month_cols.append(header[i].strip())  # 월 이름 저장
            month_idx.append(i)                   # 그 월의 칼럼 위치 저장

    # 실제 데이터 행들을 하나씩 처리
    for row in rows:

        # 데이터 칼럼 수가 너무 적으면 정상 행이 아니므로 건너뜀
        if len(row) < 3:
            continue

        # 3번째 칼럼(row[2])을 지역명으로 사용
        # 지역명이 비어 있으면 제외
        if row[2].strip() == "":
            continue

        # 한 지역의 월별 데이터를 저장할 딕셔너리
        months = {}

        # 찾아낸 월 칼럼들을 하나씩 처리
        for i in range(len(month_cols)):

            # 월 이름
            col_name = month_cols[i]

            # 해당 월이 들어있는 CSV 칼럼 번호
            col_index = month_idx[i]

            # 현재 행에 그 칼럼이 존재하는지 확인
            if col_index < len(row):
                try:
                    # 숫자 문자열을 실수(float)로 변환
                    # 예: "12,345" -> "12345" -> 12345.0
                    months[col_name] = float(row[col_index].replace(",", "").strip())
                except:
                    # 숫자로 바꿀 수 없으면 0으로 저장
                    months[col_name] = 0
            else:
                # 칼럼이 없으면 역시 0으로 저장
                months[col_name] = 0

        # 한 지역의 정보를 딕셔너리로 만들어 data_list에 추가
        data_list.append({
            "region": row[2].strip(),  # 지역명
            "months": months           # 월별 가격 정보
        })

    # 최종적으로
    # 지역별 데이터 리스트, 월 칼럼 리스트를 반환
    return data_list, month_cols


def get_value(x):
    """
    정렬할 때 사용할 함수
    딕셔너리에서 value 값만 꺼내서 반환

    예:
    x = {"region": "강남구", "value": 12345}
    return 12345
    """
    return x["value"]


# 기본 페이지 주소
@app.route("/")
def home():
    """
    첫 화면 출력
    home.html 파일을 화면에 보여줌
    """
    return render_template("home.html")


# 전체 지역의 최신월 가격 그래프
@app.route("/all_chart")
def all_chart():
    """
    전체 지역 최신월 그래프

    동작 과정:
    1. CSV 파일 읽기
    2. 가장 마지막 월(최신월) 찾기
    3. 모든 지역의 최신월 가격만 꺼내기
    4. 가격 기준으로 내림차순 정렬
    5. 차트용 labels, values 만들기
    """

    # CSV 데이터 읽기
    data_list, month_cols = load_data()

    # 마지막 월을 최신월로 사용
    # 예: ["2025년 1월", "2025년 2월", "2025년 3월"]
    # month_cols[-1] -> "2025년 3월"
    latest_month = month_cols[-1]

    # 차트에 사용할 임시 리스트
    chart_data = []

    # 모든 지역에 대해 최신월 값만 꺼내기
    for item in data_list:
        chart_data.append({
            "region": item["region"],                 # 지역명
            "value": item["months"][latest_month]    # 최신월 가격
        })

    # value 값을 기준으로 내림차순 정렬
    # reverse=True 이므로 큰 값부터 정렬
    chart_data.sort(key=get_value, reverse=True)

    # Chart.js에서 사용할 x축 라벨 리스트
    labels = []

    # Chart.js에서 사용할 y축 값 리스트
    values = []

    # chart_data에서 지역명과 가격을 각각 분리해서 저장
    for item in chart_data:
        labels.append(item["region"])
        values.append(item["value"])

    # HTML로 데이터 전달
    return render_template(
        "all_chart.html",
        labels=labels,             # 지역명 목록
        values=values,             # 가격 목록
        latest_month=latest_month  # 최신월 제목 표시용
    )


# 특정 지역의 월별 추이 그래프
@app.route("/region_chart", methods=["GET", "POST"])
def region_chart():
    """
    지역별 월별 추이 그래프

    동작 과정:
    1. CSV 읽기
    2. 지역 목록 만들기
    3. 처음 접속하면 첫 번째 지역 선택
    4. 사용자가 POST로 지역 선택하면 그 지역으로 변경
    5. 선택한 지역의 월별 가격을 values에 저장
    """

    # CSV 데이터 읽기
    data_list, month_cols = load_data()

    # 중복 없는 지역 목록 저장용 리스트
    region_list = []

    # 모든 데이터를 돌면서 지역명만 하나씩 수집
    for item in data_list:
        if item["region"] not in region_list:
            region_list.append(item["region"])

    # 처음 화면에 들어오면 첫 번째 지역을 기본 선택
    selected_region = region_list[0]

    # 사용자가 form으로 지역을 선택해서 전송했다면
    if request.method == "POST":
        selected_region = request.form["region"]

    # 선택한 지역의 월별 가격을 저장할 리스트
    values = []

    # 전체 데이터 중 선택한 지역 찾기
    for item in data_list:
        if item["region"] == selected_region:

            # 월 순서대로 가격을 values에 저장
            for month in month_cols:
                values.append(item["months"][month])

            # 찾았으면 더 이상 반복할 필요 없으므로 종료
            break

    # HTML로 데이터 전달
    return render_template(
        "region_chart.html",
        region_list=region_list,         # select 박스에 넣을 지역 목록
        selected_region=selected_region, # 현재 선택된 지역
        labels=month_cols,               # x축: 월 목록
        values=values                    # y축: 월별 가격
    )


# 최신월 기준 상위 10개 지역 그래프
@app.route("/rank_chart")
def rank_chart():
    """
    최신월 기준 상위 10개 지역 그래프

    동작 과정:
    1. CSV 읽기
    2. 최신월 찾기
    3. 모든 지역의 최신월 값 추출
    4. 내림차순 정렬
    5. 상위 10개만 자르기
    6. 차트용 labels, values 만들기
    """

    # CSV 데이터 읽기
    data_list, month_cols = load_data()

    # 마지막 월 = 최신월
    latest_month = month_cols[-1]

    # 순위 계산용 리스트
    rank_data = []

    # 모든 지역의 최신월 값 저장
    for item in data_list:
        rank_data.append({
            "region": item["region"],                 # 지역명
            "value": item["months"][latest_month]    # 최신월 가격
        })

    # 최신월 가격 기준 내림차순 정렬
    rank_data.sort(key=get_value, reverse=True)

    # 상위 10개만 남김
    rank_data = rank_data[:10]

    # Chart.js용 지역명 리스트
    labels = []

    # Chart.js용 값 리스트
    values = []

    # rank_data에서 지역명/값 분리
    for item in rank_data:
        labels.append(item["region"])
        values.append(item["value"])

    # HTML로 전달
    return render_template(
        "rank_chart.html",
        labels=labels,
        values=values,
        latest_month=latest_month
    )


# 현재 파일을 직접 실행했을 때만 Flask 서버 실행
if __name__ == "__main__":
    # debug=True
    # 코드 수정 후 자동 반영되고
    # 오류가 나면 상세 에러 화면이 보임
    app.run(debug=True)