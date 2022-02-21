# 지역변수와 전역변수

gun = 10

def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun)) # 전체 총 : 10
# checkpoint(2) # 2명이 경계 근무 나감 # [함수 내] 남은 총 : 8
# print("남은 총 : {0}".format(gun)) # 남은 총 : 8

# 가급적 전역변수 사용하지 않도록 한다. 관리가 힘들어짐

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun)) # 전체 총 : 10
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun)) # 남은 총 : 8