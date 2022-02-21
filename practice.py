# 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"}
print(menu) # {'우유', '주스', '커피'}
print(menu, type(menu)) # {'주스', '커피', '우유'} <class 'set'>

menu = list(menu)
print(menu, type(menu)) # ['우유', '커피', '주스'] <class 'list'>
# list로 클래스가 바뀜

menu = tuple(menu)
print(menu, type(menu)) # ('주스', '커피', '우유') <class 'tuple'>
# tuple로 클래스가 바뀜

# 자료구조에 따라서 괄호 모양이 바뀜을 확인하자

menu = set(menu)
print(menu, type(menu)) # {'커피', '주스', '우유'} <class 'set'>