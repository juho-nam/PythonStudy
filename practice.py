# 함수의 기본값

# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
#         .format(name, age, main_lang)) # 줄바꿈 한 때 \ 를 입력하면 한 줄로 인식

# profile("유재석", 20, "파이썬") # 이름 : 유재석   나이 : 20       주 사용 언어 : 파이썬
# profile("김태호", 25, "자바") # 이름 : 김태호   나이 : 25       주 사용 언어 : 자바

# 같은 학교 같은 학년 같은 반 같은 수업

def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
        .format(name, age, main_lang))

profile("유재석") # 이름 : 유재석   나이 : 17       주 사용 언어 : 파이썬
profile("김태호") # 이름 : 김태호   나이 : 17       주 사용 언어 : 파이썬