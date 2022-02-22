# pass

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name # 유닛 이름
        self.hp = hp # 유닛 체력
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit): # Attackunit 은 Unit 을 상속받아 만들어짐
        def __init__(self, name, hp, speed, damage):
            Unit.__init__(self, name, hp, speed)
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

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location): # move 함수를 재정의
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass # 아무것도 안하고 일단 넘어감

# 서플라이 디폿 : 건물, 1개 건물 = 8 유닛
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시") # 오류 없이 프로그램 종료

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start() # [알림] 새로운 게임을 시작합니다.
game_over() # 