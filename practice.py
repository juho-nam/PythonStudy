# 사전
cabinet = {3: "유재석", 100:"김태호"} # ket:value
print(cabinet[3]) # 유재석
print(cabinet[100]) # 김태호

print(cabinet.get(3)) # 유재석
# print(cabinet[5]) # KeyError : 5

# .get()을 이용하면 None을 반환하고 다음 줄로 넘어간다.
print(cabinet.get(5)) # None

# key 5 에 값이 있으면 값을 불러옴.
print(cabinet.get(5, "사용가능")) # 사용가능

# 사전 자료 안에 값이 있는지를 확인
print(3 in cabinet) # True
print(5 in cabinet) # False

# 정수가 아닌 string 형으로 선언도 가능
cabinet = {"A-3":"유재석","B-100":"김태호"}
print(cabinet["A-3"]) # 유재석
print(cabinet["B-100"]) # 김태호

# 새 손님
print(cabinet) # {'A-3': '유재석', 'B-100': '김태호'}
# C-20 이라는 key를 만들고 조세호 라는 value를 넣음
# C-20에 이미 값이 있으면 업데이트 됨
cabinet["C-20"] = "조세호"
cabinet["A-3"] = "김종국"
print(cabinet) # {'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}

# 손님 퇴장
del cabinet["A-3"]
print(cabinet) # {'B-100': '김태호', 'C-20': '조세호'}

# key 들만 출력
print(cabinet.keys()) # dict_keys(['B-100', 'C-20'])

# value 들만 출력
print(cabinet.values()) # dict_values(['김태호', '조세호'])

# key, value 쌍으로 출력
print(cabinet.items()) # dict_items([('B-100', '김태호'), ('C-20', '조세호')])

# 목용탕 영업 종료
cabinet.clear()
print(cabinet) # {}