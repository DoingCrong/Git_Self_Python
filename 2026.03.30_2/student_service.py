
import pymysql
import numpy as np
from db_config import db_connect


# ===============================
# 점수 입력 함수
# 숫자만 입력 가능하도록 예외처리
# 0~100 범위도 함께 검사
# ===============================
def input_score(subject):
    while True:
        try:
            score = int(input(f"{subject} 점수 입력 : "))

            if score < 0 or score > 100:
                print("점수는 0~100 사이만 입력하세요.")
                continue

            return score

        except ValueError:
            print("숫자만 입력 가능합니다.")


# ===============================
# 학점 계산 함수
# 평균 기준으로 학점 계산
# ===============================
def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


# ===============================
# 성적 입력 (Create)
# ===============================
def insert_student():
    conn = db_connect()
    cursor = conn.cursor()

    try:
        print("\n[성적 입력]")

        hakbun = input("학번 입력 : ").strip()
        name = input("이름 입력 : ").strip()

        # 점수 입력
        kor = input_score("국어")
        eng = input_score("영어")
        math = input_score("수학")

        # NumPy 배열 생성
        scores = np.array([kor, eng, math])

        # 집계함수 사용
        total = int(np.sum(scores))      # 총점
        average = float(np.mean(scores)) # 평균

        # 학점 계산
        grade = get_grade(average)

        sql = """
        insert into student(hakbun, name, kor, eng, math, total, average, grade)
        values(%s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (hakbun, name, kor, eng, math, total, average, grade))
        conn.commit()

        print("성적 입력 완료")

    except pymysql.err.IntegrityError:
        print("이미 존재하는 학번입니다.")

    except Exception as e:
        print("입력 중 오류 발생 :", e)

    finally:
        cursor.close()
        conn.close()


# ===============================
# 전체 조회 (Read All)
# ===============================
def select_all():
    conn = db_connect()
    cursor = conn.cursor()

    try:
        print("\n[전체 조회]")

        sql = "select * from student order by hakbun"
        cursor.execute(sql)

        rows = cursor.fetchall()

        if len(rows) == 0:
            print("저장된 데이터가 없습니다.")
            return

        print("-" * 80)
        print("학번\t이름\t국어\t영어\t수학\t총점\t평균\t학점")
        print("-" * 80)

        for row in rows:
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]:.2f}\t{row[7]}")

    except Exception as e:
        print("조회 중 오류 발생 :", e)

    finally:
        cursor.close()
        conn.close()


# ===============================
# 1명 조회 (Read One)
# 학번 기준 검색
# ===============================
def select_one():
    conn = db_connect()
    cursor = conn.cursor()

    try:
        print("\n[1명 조회]")

        hakbun = input("조회할 학번 입력 : ").strip()

        sql = "select * from student where hakbun=%s"
        cursor.execute(sql, (hakbun,))

        row = cursor.fetchone()

        if row is None:
            print("해당 학번의 학생이 없습니다.")
            return

        print("-" * 40)
        print("학번 :", row[0])
        print("이름 :", row[1])
        print("국어 :", row[2])
        print("영어 :", row[3])
        print("수학 :", row[4])
        print("총점 :", row[5])
        print("평균 :", round(row[6], 2))
        print("학점 :", row[7])
        print("-" * 40)

    except Exception as e:
        print("조회 중 오류 발생 :", e)

    finally:
        cursor.close()
        conn.close()


# ===============================
# 성적 수정 (Update)
# 학번 기준으로 수정
# ===============================
def update_student():
    conn = db_connect()
    cursor = conn.cursor()

    try:
        print("\n[성적 수정]")

        hakbun = input("수정할 학번 입력 : ").strip()

        # 먼저 해당 학번 존재 여부 확인
        check_sql = "select * from student where hakbun=%s"
        cursor.execute(check_sql, (hakbun,))
        row = cursor.fetchone()

        if row is None:
            print("해당 학번의 학생이 없습니다.")
            return

        print("새 점수를 입력하세요.")

        kor = input_score("국어")
        eng = input_score("영어")
        math = input_score("수학")

        # NumPy 집계함수 사용
        scores = np.array([kor, eng, math])
        total = int(np.sum(scores))
        average = float(np.mean(scores))
        grade = get_grade(average)

        sql = """
        update student
        set kor=%s, eng=%s, math=%s, total=%s, average=%s, grade=%s
        where hakbun=%s
        """

        cursor.execute(sql, (kor, eng, math, total, average, grade, hakbun))
        conn.commit()

        print("성적 수정 완료")

    except Exception as e:
        print("수정 중 오류 발생 :", e)

    finally:
        cursor.close()
        conn.close()


# ===============================
# 성적 삭제 (Delete)
# 학번 기준으로 삭제
# ===============================
def delete_student():
    conn = db_connect()
    cursor = conn.cursor()

    try:
        print("\n[성적 삭제]")

        hakbun = input("삭제할 학번 입력 : ").strip()
        #.strip() : 문자열 앞뒤 공백(스페이스, 엔터, 탭)등을 제거함
        #입력의 정확성을 보장해주는 함수임.

        # 존재 여부 확인
        check_sql = "select * from student where hakbun=%s"
        cursor.execute(check_sql, (hakbun,))
        row = cursor.fetchone()

        if row is None:
            print("해당 학번의 학생이 없습니다.")
            return

        answer = input("정말 삭제하시겠습니까? (y/n) : ").strip().lower()

        if answer != "y":
            print("삭제 취소")
            return

        sql = "delete from student where hakbun=%s"
        cursor.execute(sql, (hakbun,))
        conn.commit()

        print("성적 삭제 완료")

    except Exception as e:
        print("삭제 중 오류 발생 :", e)

    finally:
        cursor.close()
        conn.close()