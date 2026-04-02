testfile = open("test3.txt", "w", encoding="UTF-8")
name = input("이름 : ")
kor = int(input("국어 : "))
eng = int(input("영어 : "))
mat = int(input("수학 : "))

total = kor+eng+mat
average = round(total/3.0, 2)
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

#fill = [name, kor, eng, mat, total, average, grade]

testfile.write(f"{name} / {kor} / {eng} / {mat} / {total} / {average} / {grade}")
testfile.close()

testfile = open("test3.txt", "r", encoding="UTF-8")
kkk = testfile.read()
print(kkk)
testfile.close()