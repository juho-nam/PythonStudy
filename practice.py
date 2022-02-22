# 표준 입출력

# sep 는 쉼표로 문자열을 더할 때, 띄어쓰기 대신 그 사이에 들어갈 문자열을 말한다
print("Python","Java","Javascript", sep=",", end="?")
print("무엇이 더 재밌을까요?")
# Python,Java,Javascript?무엇이 더 재밌을까요?
# end는 문장의 끝을 줄바꿈 대신 문자로 처리하는 것

import sys
print("Python","Java", file=sys.stdout) # Python Java
print("Python","Java", file=sys.stderr) # Python Java
# VS code에서는 출력에 차이가 없어보이지만
# stdout은 표출 출력으로, stderr는 표준 에러로 처리됨

# 시험 성적
scores = {"수학":0, "영어":50,"코딩":100}
for subject, score in scores.items(): # .items는 key와 value가 같이 튜플로 나옴
    print(subject.ljust(8), str(score).rjust(4), sep=":")
# ljust(8) 는 8칸의 공간 확보 후 왼쪽정렬(left)
# rjust(4) 는 4칸의 공간 확보 후 오른쪽정렬(right)
# 수학      :   0
# 영어      :  50
# 코딩      : 100

# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 6):
    print("대기번호 : "+str(num).zfill(3))
# zfill(3) 은 3칸의 공간을 사용하는데, 값이 없는 부분은 0으로 채움
# 대기번호 : 001
# 대기번호 : 002
# 대기번호 : 003
# 대기번호 : 004
# 대기번호 : 005

# 표준입력
answer = input("아무 값이나 입력하세요 : ")
print(type(answer)) # <class 'str'>
print("입력하신 값은 "+answer+"입니다.")
# input 으로 입력받으면 항상 문자열 형태로 저장됨