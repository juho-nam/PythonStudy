# 상속

# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name # 유닛 이름
        self.hp = hp # 유닛 체력

# 공격 유닛
class Attackunit(Unit): # Attackunit 은 Unit 을 상속받아 만들어짐
        def __init__(self, name, hp, damage):
            Unit.__init__(self, name, hp)
            self.damage = damage

        def attack(self, location):
            print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
                .format(self.name, location, self.damage)) # location은 전달받은 값을 사용

        def damaged(self, damage):
            print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
            self.hp -= damage
            print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
            if self.hp <= 0:
                print("{0} : 파괴되었습니다.".format(self.name))

# 메딕 : 의무병

# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = Attackunit("파이어뱃", 50, 16)
firebat1.attack("5시")
# 파이어뱃 : 5시 방향으로 적군을 공격 합니다. [공격력 16]

# 공격 2번 받는다고 가정
firebat1.damaged(25)
# 파이어뱃 : 25 데미지를 입었습니다.
# 파이어뱃 : 현재 체력은 25 입니다.
firebat1.damaged(25)
# 파이어뱃 : 25 데미지를 입었습니다.
# 파이어뱃 : 현재 체력은 0 입니다.
# 파이어뱃 : 파괴되었습니다.