import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

students = []

while True:
    print("\n1. 입력  2. 전체출력  3. 그래프  4. 종료")
    menu = input("선택: ")

    if menu == "1":
        name = input("이름: ")

        try:
            kor = int(input("국어: "))
            eng = int(input("영어: "))
            math = int(input("수학: "))
        except:
            print("점수는 숫자만 입력!")
            continue

        total = kor + eng + math
        avg = round(total / 3, 2)

        # 학점
        if avg >= 90:
            grade = "A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 70:
            grade = "C"
        else:
            grade = "F"

        students.append([name, kor, eng, math, total, avg, grade])

    elif menu == "2":
        print("\n이름 국어 영어 수학 총점 평균 학점")
        for s in students:
            print(s)

    elif menu == "3":
        if not students:
            print("데이터 없음")
            continue

        names = [s[0] for s in students] #리스트를 반복하여 원하는 값만 뽑아서 새로운 리스트에 
                                         #(즉, s[0]에 들어있는 이름을 names변수에(리스트로) 넣기)
        avgs = [s[5] for s in students] #(즉, s[5]에 들어있는 평균을 avgs변수에(리스트로) 넣기)

        plt.bar(names, avgs)
        plt.title("학생 평균 그래프")
        plt.xlabel("이름")
        plt.ylabel("평균")
        plt.show()

    elif menu == "4":
        break