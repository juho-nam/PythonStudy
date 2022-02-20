<<<<<<< .merge_file_a07004
# 랜덤함수
from random import *

print(random()) # 0.0 이상 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성

print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성

print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성

print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성
=======
# 숫자처리함수
print(abs(-5)) # -5의 절대값
print(pow(4,2)) # 4^2 = 16
print(max(5, 12)) # 5와 12 중 최대값. 12
print(min(5, 12)) # 5와 12 중 최소값.  5
print(round(3.14)) # 반올림. 3
print(round(4.99)) # 5

from math import *
print(floor(4.99)) # 내림. 4
print(ceil(3.14)) # 올림. 4
print(sqrt(16)) # 제곱근. 4.0
>>>>>>> .merge_file_a02708
