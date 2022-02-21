# 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤틀르 진행하기로 합니다.
# 댓글 작성자들 중에 추츰을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건3: random 모듈의 shuffle 과 sample 을 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

# (활용 예제)
# from random import *
# 1st - [1,2,3,4,5]
# print(1st)
# shuffle(1st)
# print(1st)
# print(sample(1st, 1)) # lst의 인자 중에서 1개 만큼 샘플로 뽑음

from random import *
users = range(1,21) # 1부터 20까지 숫자 생성
# print(type(users)) # <class 'range'>
users = list(users)
# print(type(users)) # <class 'list'>

print(users)
shuffle(users)
# 한 번 섞고 뽑고 또 섞고 뽑으면 중복당첨 가능성 있으므로 바로 또 뽑는다

winners = sample(users, 4)
print(" -- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print(" -- 축하합니다 --")