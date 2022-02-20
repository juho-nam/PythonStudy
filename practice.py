# 문자열 처리 함수

python = "Python is Amazing"
print(python.lower()) # 문자열 모두 소문자로 출력
print(python.upper()) # 문자열 모두 대문자로 출력
print(python[0].isupper()) # 해당 문자가 대문자인지 판별(True / False).
print(len(python)) # 문자열의 길이
print(python.replace("Python", "Java")) # 원하는 문자열의 부분을 다른 문자열로 바꿈

index = python.index("n")
print(index) # 5
index = python.index("n", index + 1) # 앞에서 찾은 위치+1부터 다음 n을 찾음
print(index) # 15

print(python.find("n")) # 5
print(python.find("Java")) # Java가 문자열에 없으므로 -1
# print(python.index("Java"))
# index는 찾는 문자열이 없으면 오류를 낸다.

print(python.count("n")) # n 이 문자열에서 몇번 나오는지 카운트