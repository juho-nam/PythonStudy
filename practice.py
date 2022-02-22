# 멤버변수
# 클래스 내에서 정의된 변수
# self.name, self.hp, self.damage 등이 멤버변수
# 파이썬에서는 외부에서 객체에 추가로 변수를 만들어 쓸 수 있음
# 확장한 변수는 확장된 객체에서만 사용 가능
class unit:
    def __init__(self, name, hp, damage):
        self.name = name # 유닛 이름
        self.hp = hp # 유닛 체력
        self.damage = damage # 유닛 공격력
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))

# 레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
wraith1 = unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True # 외부에서 clocking 이라는 변수를 추가로 할당

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))