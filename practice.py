# 집합 (set)
# 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set) # {1, 2, 3}

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"]) # List로 먼저 만들고 set으로 감싸줌

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python) # {'유재석'}
print(java.intersection(python)) # {'유재석'}

# 합집합 (java 도 할 수 있거나 python 할 수 있는 개발자)
print(java | python) # {'유재석', '박명수', '김태호', '양세형'}
print(java.union(python)) # {'유재석', '박명수', '김태호', '양세형'}
# 순서는 보장되지 않음

# 차집합 (java 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python) # {'김태호', '양세형'}
print(java.difference(python)) # {'김태호', '양세형'}

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python) # {'김태호', '박명수', '유재석'}

# java 를 잊어버림
java.remove("김태호")
print(java) # {'양세형', '유재석'}