# continue 와 break
# 반복문 내에서 사용

absent = [2, 5] # 결석
no_book = [7] # 책 없음
for student in range(1, 11): # 1~10
    print("{0}, 책을 일어봐".format(student))
    if student in absent:
        continue # 다음 문장을 실행시키지 않고 바로 반복문 조건 확인
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break # 반복문 종료