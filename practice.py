# __init__
# 파이썬에서 쓰이는 생성자
# __init__ 함수에 정의된 (self 를 제외한 나머지) 인자들의 수와 동일하게 해야함
# marine1,2 와 tank 는 unit 클래스의 '객체'

class unit:
    def __init__(self, name, hp, damage):
        self.name = name # 유닛 이름
        self.hp = hp # 유닛 체력
        self.damage = damage # 유닛 공격력
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp,self.damage))

# marine1 = unit("마린", 40, 5)
# marine2 = unit("마린", 40, 5)
# tank = unit("탱크", 150, 35)

marine1 = unit("마린", 40)
# TypeError: unit.__init__() missing 1 required positional argument: 'damage'