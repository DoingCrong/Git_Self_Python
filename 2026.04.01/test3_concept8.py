import pandas as pd

# 빈 리스트 생성
data = []

count = int(input("몇 명 : "))


for i in range(count):
    print(f"\n=== {i+1}번째 사람 입력 ===")
    name = input("이름 입력 : ")
    kor = int(input("국어 점수 입력 : "))
    eng = int(input("영어 점수 입력 : "))
    math = int(input("수학 점수 입력 : "))

    # total = kor+eng+math
    # average = total / 3.0

    # if average >= 90:
    #     grade = "A"
    # elif average >= 80:
    #     grade = "B"
    # elif average >= 70:
    #     grade = "C"
    # elif average >= 60:
    #     grade = "D"
    # else:
    #     grade = "F"

    # 리스트에 저장
    data.append([name, kor, eng, math])

    # 판다스 데이터프레임 생성
    df = pd.DataFrame(data, columns=["이름", "국어", "영어", "수학"])
    df["총점"] = df[["국어","영어","수학"]].sum(axis=1)
    df["평균"] = df[["국어","영어","수학"]].mean(axis=1).round(2)

    def grade(avg):
        if(avg) >= 90:
            return "A"
        elif(avg) >= 80:
            return "B"
        elif(avg) >= 70:
            return "C"
        elif(avg) >= 60:
            return "D"
        else:
            return "F"
        
    df["학점"] = df["평균"].apply(grade)

    print(df)