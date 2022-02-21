# while

customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비되었습니다. {1} 번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기되었습니다.")
# 토르, 커피가 준비되었습니다. 5 번 남았어요.
# 토르, 커피가 준비되었습니다. 4 번 남았어요.
# 토르, 커피가 준비되었습니다. 3 번 남았어요.
# 토르, 커피가 준비되었습니다. 2 번 남았어요.
# 토르, 커피가 준비되었습니다. 1 번 남았어요.
# 커피는 폐기되었습니다.

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. {1} 번 남았어요.".format(customer, index))
#     index += 1
# 무한루프. 종료하려면 ctrl + c

person = "Unknown"

while person != customer:
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")
# 이름이 토르가 나올때까지 반복