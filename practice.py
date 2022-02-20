# 변수
animal = "고양이"
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >= 3 # 나이가 3살 이상이면 어른으로 본다

print("우리집 " + animal + "의 이름은 " + name + "예요.")
hobby = "공놀이" # 취미가 바뀌었으므로 공놀이 출력
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요.")
# '+' 대신 ',' 사용가능. 이 경우 정수 바로 사용가능. 단, ',' 이후엔 반드시 빈칸 포함됨
print(name + "는 어른일까요? " + str(is_adult))