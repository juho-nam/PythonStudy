# if (분기)
# if 조건:
#     실행 명령문

weather = input("오늘 날씨는 어떄요? ")
# 사용자의 입력 받음. input안의 문장 출력 후 입력 받음
# input은 string 형태로 저장함
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")