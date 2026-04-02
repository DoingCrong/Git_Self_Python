#학생성적 (국어, 영어, 수학)
"""
import numpy as np

scores = np.array([
    [90,80,70],
    [85,88,92],
    [70,75,80]
])

print("학생의총점:", np.sum(scores, axis=1))
print("학생의평균:", np.mean(scores, axis=1))
print("과목별평균", np.mean(scores, axis=0))


import numpy as np
n = int(input("개수 입력 : "))

arr = []

for i in range(n):
    num = int(input(f"{i+1}번째 값 입력 : "))
    arr.append(num)

print("결과 :", arr)

score = np.array(arr)
print(score)
"""

"""
함수와 NumPy를 이용한 학생 성적 관리 프로그램

조건

학생들의 성적 정보를 입력받아 개인별 성적 처리와 함께 반별 통계도 구하는 프로그램을 작성하시오.

입력 항목

각 학생에 대해 다음 정보를 입력한다.

반
이름
국어
영어
수학

처리 내용
1. 학생별 처리

각 학생에 대해 다음 항목을 계산한다.

총점
평균
학점
석차

학점 기준은 아래와 같다.

평균 90 이상 : A
평균 80 이상 : B
평균 70 이상 : C
평균 60 이상 : D
그 외 : F

석차는 전체 학생 기준 총점(평균)으로 계산한다.

2. 반별 처리

입력된 학생 자료를 이용하여 각 반에 대해 다음을 계산한다.

반별 국어 합계
반별 영어 합계
반별 수학 합계
반별 총점 합계
반별 국어 평균
반별 영어 평균
반별 수학 평균
반별 전체 평균
출력 내용
1. 학생별 성적표 출력

다음 형식으로 출력한다.

반
이름
국어
영어
수학
총점
평균
학점
석차
2. 반별 집계표 출력

다음 형식으로 출력한다.

반
학생수
국어합
영어합
수학합
총점합
국어평균
영어평균
수학평균
반평균
"""

import numpy as np

# 1. 입력 함수
def input_data():
    n = int(input("학생 수 입력: "))

    classes = []
    names = []
    scores = []

    for i in range(n):
        print(f"\n{i+1}번째 학생 입력")

        # 반 입력 (문자 검사)
        while True:
            ban = input("반: ")
            if ban.strip() == "":
                print("반은 비워둘 수 없습니다.")
            else:
                break

        # 이름 입력 (문자만 허용)
        while True:
            name = input("이름: ")
            if name.isalpha():   # 문자만 허용
                break
            else:
                print("이름은 문자만 입력하세요.")

        # 국어 점수 입력
        while True:
            try:
                kor = int(input("국어: "))
                if 0 <= kor <= 100:
                    break
                else:
                    print("점수는 0~100 사이만 입력하세요.")
            except:
                print("숫자만 입력하세요.")

        # 영어 점수 입력
        while True:
            try:
                eng = int(input("영어: "))
                if 0 <= eng <= 100:
                    break
                else:
                    print("점수는 0~100 사이만 입력하세요.")
            except:
                print("숫자만 입력하세요.")

        # 수학 점수 입력
        while True:
            try:
                math = int(input("수학: "))
                if 0 <= math <= 100:
                    break
                else:
                    print("점수는 0~100 사이만 입력하세요.")
            except:
                print("숫자만 입력하세요.")

        # 저장
        classes.append(ban)
        names.append(name)
        scores.append([kor, eng, math])

    return classes, names, np.array(scores)


# 2. 총점, 평균 계산
def calc_total_avg(scores):
    total = np.sum(scores, axis=1)
    avg = np.mean(scores, axis=1)
    return total, avg


# 3. 학점 계산
def calc_grade(avg):
    grade = []

    for a in avg:
        if a >= 90:
            grade.append("A")
        elif a >= 80:
            grade.append("B")
        elif a >= 70:
            grade.append("C")
        elif a >= 60:
            grade.append("D")
        else:
            grade.append("F")

    return grade


# 4. 석차 계산
def calc_rank(total):
    n = len(total)
    rank = []

    for i in range(n):
        r = 1
        for j in range(n):
            if total[i] < total[j]:
                r += 1
        rank.append(r)

    return rank


# 5. 학생별 결과 출력
def print_student_result(classes, names, scores, total, avg, grade, rank):
    print("\n================ 학생별 성적 결과 ================")
    print("반\t이름\t국어\t영어\t수학\t총점\t평균\t학점\t석차")

    for i in range(len(names)):
        print(f"{classes[i]}\t{names[i]}\t{scores[i][0]}\t{scores[i][1]}\t{scores[i][2]}\t"
              f"{total[i]}\t{avg[i]:.2f}\t{grade[i]}\t{rank[i]}")

#6. 반별 계산
def calc_class_summary(classes, scores, total):

    # 반 이름 중복 제거
    unique_classes = []

    for c in classes:
        if c not in unique_classes:
            unique_classes.append(c)

    summary = []

    # 반별 처리
    for ban in unique_classes:

        # 현재 반에 해당하는 학생 위치 찾기
        idx = []

        for i in range(len(classes)):
            if classes[i] == ban:
                idx.append(i)

        # 현재 반 학생들의 점수와 총점 저장
        class_scores = scores[idx]
        class_total = total[idx]

        # 학생 수
        student_count = len(idx)

        # 과목별 합계
        kor_sum = np.sum(class_scores[:, 0])
        eng_sum = np.sum(class_scores[:, 1])
        math_sum = np.sum(class_scores[:, 2])
        total_sum = np.sum(class_total)

        # 과목별 평균
        kor_avg = np.mean(class_scores[:, 0])
        eng_avg = np.mean(class_scores[:, 1])
        math_avg = np.mean(class_scores[:, 2])
        class_avg = np.mean(class_total / 3)

        # 결과 저장
        summary.append([
            ban,
            student_count,
            kor_sum, eng_sum, math_sum, total_sum,
            kor_avg, eng_avg, math_avg, class_avg
        ])

    return summary


# 7. 반별 집계 출력
def print_class_summary(summary):
    print("\n================ 반별 집계 결과 ================")
    print("반\t학생수\t국어합\t영어합\t수학합\t총점합\t국어평균\t영어평균\t수학평균\t반평균")

    for row in summary:
        print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t"
              f"{row[6]:.2f}\t\t{row[7]:.2f}\t\t{row[8]:.2f}\t\t{row[9]:.2f}")


# ================= 실행 =================
classes, names, scores = input_data()

total, avg = calc_total_avg(scores)

grade = calc_grade(avg)

rank = calc_rank(total)

print_student_result(classes, names, scores, total, avg, grade, rank)

summary = calc_class_summary(classes, scores, total)

print_class_summary(summary)