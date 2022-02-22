# 클래스

class unit:
    def __init__(self, name, hp, damage):
        self.name = name # 유닛 이름
        self.hp = hp # 유닛 체력
        self.damage = damage # 유닛 공격력
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp,self.damage))

marine1 = unit("마린", 40, 5)
marine2 = unit("마린", 40, 5)
tank = unit("탱크", 150, 35)

# 마린 유닛이 생성 되었습니다.
# 체력 40, 공격력 5

# 마린 유닛이 생성 되었습니다.
# 체력 40, 공격력 5

# 탱크 유닛이 생성 되었습니다.
# 체력 150, 공격력 35