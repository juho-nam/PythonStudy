# 연산자
print(1+1) #2
print(3-2) #1
print(5*2) #10
print(6/3) #2.0

print(2**3) # 2^3 = 8
print(5%3) # 5/3의 나머지 = 2
print(10%3) # 1
print(5//3) # 5/3 의 몫 = 1
print(10//3) # 3

print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True

print(3 == 3) # 3과 3이 같다 = True
print(4 == 2) # False
print(3 + 4 == 7) # True

print(1 != 3) # 1과 3이 같지 않다 = True
print(not(1 != 3)) # False

print((3 > 0) and (3 < 5)) # 3이 0보다 크고 3이 5보다 작다 = True
print((3 > 0) & (3 < 5)) # True

print((3 > 0) or (3 > 5)) #  3이 0보다 크거나 3이 5보다 크다 = Ture
print((3 > 0) | (3 > 5)) # True

print(5 > 4 > 3) # 연속으로 사용할 땐 AND가 기본. True
print(5 > 4 > 7) # False