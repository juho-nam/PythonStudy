# 가변 인자

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     # end=" " 는 문장 출력이 끝나고 그 문장 뒤에 이어서 출력하겠다는 의미
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
# # 이름 : 유재석   나이 : 20        Python Java C C++ C#

# profile("김태호", 25, "Kotlin", "Swift", "", "", "")
# # 이름 : 김태호   나이 : 25 

def profile(name, age, *language): # *은 내가 원하는 만큼 값을 추가하겠다는 의미
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
# 이름 : 유재석   나이 : 20        Python Java C C++ C# JavaScript

profile("김태호", 25, "Kotlin", "Swift")
# 이름 : 김태호   나이 : 25        Kotlin Swift