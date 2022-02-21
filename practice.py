# 키워드값

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬",age=20) # 유재석 20 파이썬
profile(main_lang="자바",age=25,name="김태호") # 김태호 25 자바
# 키워드를 이용하면 호출시 순서가 뒤바뀌어도 함수 선언대로 출력됨