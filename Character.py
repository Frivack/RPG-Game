from Skill import *
from Creature import *


class character(Creature):
    critical = 60  # 크리티컬 성공 기준
    critical2 = 10  # 크리티컬 성공시, 공격력 대비 레벨 2마다 20%/40%/60%/80%/100%
    lucky = 0
    evasion = 0
    level = 1
    exp = 0
    maxlevel = 10
    maxhp = 0
    gold = 0
    inventory = []
    weapon = 0
    armor = 0
    accessory = 0
    skills = []

    def __init__(self, pick, show = 0):
        self.skills = []
        if pick == 0:
            pass
        elif pick == 1:
            self.name = "전사"
            self.hp = 100
            self.maxhp = self.hp
            self.maxattack = 13
            self.minattack = 15
            self.defence = 7
            self.evasion = 65 # 100%기준
            self.critical = 60
            self.critical2 = 20
            self.lucky = 40
            self.skills.append(Skill("대검격", 13, 13, 80, 0))
            self.skills.append(Skill("쾌속 검격", 13, 14, 75, 0))
            self.skills.append(Skill("불사베기", 15, 15, 70, 0))
            self.skills.append(Skill("염계대도행", 20, 20, 60, 1))
        elif pick == 2:
            self.name = "마법사"
            self.hp = 70
            self.maxhp = self.hp
            self.maxattack = 14
            self.minattack = 17
            self.defence = 5
            self.evasion = 70 # 100%기준
            self.critical = 60 # 100%기준
            self.critical2 = 20
            self.lucky = 40
            self.skills.append(Skill("얼음 가시", 14, 14, 80, 0))
            self.skills.append(Skill("파괴 광선", 14, 16, 75, 0))
            self.skills.append(Skill("체인 라이트닝", 17, 17, 70, 0))
            self.skills.append(Skill("아케인 에임", 21, 21, 60, 1))
        elif pick == 3:
            self.name = "궁수"
            self.hp = 80
            self.maxhp = self.hp
            self.maxattack = 18
            self.minattack = 17
            self.defence = 5
            self.evasion = 70 # 100%기준
            self.critical = 60 # 100%기준
            self.critical2 = 20
            self.lucky = 40
            self.skills.append(Skill("그림자 화살", 17, 17, 80, 0))
            self.skills.append(Skill("맹독 화살", 17, 18, 75, 0))
            self.skills.append(Skill("뇌격 화살", 18, 18, 70, 0))
            self.skills.append(Skill("파멸의 화살", 22, 22, 60, 1))
        elif pick == 4:
            self.name = "창기사"
            self.hp = 120
            self.maxhp = self.hp
            self.maxattack = 17
            self.minattack = 15
            self.defence = 6
            self.evasion = 65 # 100%기준
            self.critical = 60 # 100%기준
            self.critical2 = 20
            self.lucky = 40
            self.skills.append(Skill("비룡", 16, 16, 80, 0))
            self.skills.append(Skill("용후", 16, 17, 75, 0))
            self.skills.append(Skill("고통의 천류", 17, 17, 70, 0))
            self.skills.append(Skill("성스러운 창", 21, 21, 60, 1))
        elif pick == 5:
            self.name = "격투사"
            self.hp = 100
            self.maxhp = self.hp
            self.maxattack = 18
            self.minattack = 17
            self.defence = 6
            self.evasion = 60 # 100%기준
            self.critical = 60 # 100%기준
            self.critical2 = 20
            self.lucky = 40
            self.skills.append(Skill("천둥 주먹", 17, 17, 80, 0))
            self.skills.append(Skill("기상 충격파", 17, 18, 75, 0))
            self.skills.append(Skill("광문", 0, 0, 70, 1)) #데미지가 아닌 효과 +1 광문:공격력 증가 + 1 (성공율: 80%) // 적을 쓰러뜨리면 다시 처음으로 초기화
            self.skills.append(Skill("최후의 일격", 22, 22, 60, 1))
        elif pick == 6:
            self.name = "언데드"
            self.hp = 80
            self.maxhp = self.hp
            self.maxattack = 18
            self.minattack = 17
            self.defence = 5
            self.evasion = 80 # 100%기준
            self.critical = 60 # 100%기준
            self.critical2 = 20
            self.lucky = 40
            self.skills.append(Skill("악마의 손", 17, 17, 80, 0))
            self.skills.append(Skill("망자의 부활", 17, 18, 75, 0))
            self.skills.append(Skill("어둠의 서약", 18, 18, 70, 0))
            self.skills.append(Skill("파멸의 군주", 24, 24, 60, 1))

        if show == 1:
            print("="*20)
            print("이름:", self.name)
            print("체력:", self.hp)
            print("공격력:", self.minattack, "~", self.maxattack)
            print("방어력:", self.defence)
            print("회피율:", self.evasion)
            for i in self.skills:
                i.showSkill()
            print("="*20)

    def buy(self, myitem):
        if self.gold >= myitem.value:
            self.gold = self.gold - myitem.value  # 아이템 추가 추후에
            self.inventory.append(myitem)
            print("%s 아이템을 구매하셨습니다. " %myitem.name)
        else:
            print("아이템을 구매할 수 없습니다.\n돈이 부족합니다.")

    def sell(self):
        self.inventorycheck()
        si = int(input("판매할 아이템을 고르세요. 입력:"))
        if si > 0 and len(self.inventory) >= si:
            si2 = input("정말 파시겠습니까? \n 1. Yes or 2. No 입력: ")
            if si2 == "Yes" or si2 == "1" or si2 == "Y" or si2 == "y":
                self.gold = self.gold + self.inventory[si - 1].value
                print("%s을 팔았습니다. " % self.inventory[si - 1].name)
                del self.inventory[si - 1]
            else:
                print("판매를 취소했습니다. ")
        else:
            print("없는 아이템입니다. ")

    def attackto(self):
        itematk = 0
        if self.weapon != 0:
            itematk = itematk + self.weapon.attack
        if self.armor != 0:
            itematk = itematk + self.armor.attack
        if self.accessory != 0:
            itematk = itematk + self.accessory.attack

        print("-"*20)
        print("스킬을 선택하십시오. ")
        count = 1
        for K in self.skills:
            print("%s." %count, "스킬: %s ㅣ"%K.name, "Min: %s +"%K.mindamage, "(%s)"%itematk, "MAX: %s +"%K.maxdamage, "(%s)"%itematk, "성공율: %s%%"%K.sattack,)
            count = count + 1
        print("-"*20)
        u = int(input("입력: "))
        dmg = self.skills[u - 1].getDamage() + itematk
        if random.randrange(0, 100) < self.skills[u - 1].sattack:
            print("%s 데미지의"%dmg, self.skills[u - 1].name, "(으)로 몬스터를 공격")
        else:
            print("공격 실패!")
            dmg = 0
        return dmg

    def attacked(self, dmg):
        d = dmg - self.defence
        if random.randrange(0, 100) < self.evasion:
            print("몬스터의 공격 회피!")
        elif d > 0:
            self.hp = self.hp - d
            print("%s"%d, "의 피해를 입음!")
            print("남은 체력: %s"%self.hp)
        else:
            print("몬스터의 공격을 막아냄!")

    def inventorycheck(self):
        count = 1
        print("="*20)
        for i in self.inventory:
            print("%s."%count,end=" ")
            i.showinfo()
            count = count+1
        print("="*20)

    def playercheck(self):
        print("="*20)
        print("이름: %s"%self.name)
        print("레벨: %s /"%self.level, self.maxlevel)
        print("경험치: %s / 5"%self.exp)
        print("체력: %s /"%self.hp, self.maxhp)
        print("방어력:", self.defence)
        print("회피율: %s%%"%self.evasion)
        print("크리티컬 확률: %s%%"%self.critical)
        print("크리티컬 배수: 1.", int(self.critical2/10), sep="")
        print("="*20)

    def goldcheck(self):
        print("="*20)
        print("내가 보유하고 있는 골드: %s골드"%self.gold)
        print("="*20)

    def equipcheck(self):
        k = 0
        if self.weapon == 0:
            print("1. 없음 (무기)")
            k = k + 1
        else:
            print("1. ", end="")
            self.weapon.showinfo()

        if self.armor == 0:
            print("2. 없음 (방어구)")
            k = k + 1
        else:
            print("2. ", end="")
            self.armor.showinfo()

        if self.accessory == 0:
            print("3. 없음 (악세사리)")
            k = k + 1
        else:
            print("3. ", end="")
            self.accessory.showinfo()

        return k

    def showCharacter(self):
        print("1. 상태창")
        print("2. 인벤토리")
        print("3. 보유골드")
        print("4. 장착 확인")
        print("5. 아이템 장착")
        print("6. 아이템 해제")
        s = int(input("선택: "))
        if s == 1:
            self.playercheck()
        elif s == 2:
            self.inventorycheck()
        elif s == 3:
            self.goldcheck()
        elif s == 4:
            self.equipcheck()
        elif s == 5:
            self.iteminstallation()
        elif s == 6:
            self.itemlift()
        else:
            print("잘못된 입력")

    def iteminstallation(self):
        self.inventorycheck()

        s = int(input("장착할 아이템 선택:"))
        if 0 <= s <= len(self.inventory):
            p = self.inventory[s - 1].part
            if p == "공격":
                if self.weapon == 0:
                    self.weapon = self.inventory[s - 1]
                    del self.inventory[s - 1]
                else:
                    self.inventory.append(self.weapon)
                    self.weapon = self.inventory[s - 1]
                    del self.inventory[s - 1]
            elif p == "방어":
                if self.armor == 0:
                    self.armor = self.inventory[s - 1]
                    del self.inventory[s - 1]
                else:
                    self.inventory.append(self.armor)
                    self.armor = self.inventory[s - 1]
                    del self.inventory[s - 1]
            elif p == "악세사리":
                if self.accessory == 0:
                    self.accessory = self.inventory[s - 1]
                    del self.inventory[s - 1]
                else:
                    self.inventory.append(self.accessory)
                    self.accessory = self.inventory[s - 1]
                    del self.inventory[s - 1]
            else:
                print("에러: 올바른 아이템 유형이 아님")
            print("장착 완료")
        else:
            print("잘못된 입력")

    def itemlift(self):
        k = self.equipcheck()

        if k == 3:
            print("장착중인 아이템 없음")
        else:
            s = input("해제할 이이템 선택: ")
            if s == 1 and self.weapon != 0:
                self.inventory.append(self.weapon)
                self.weapon = 0
            elif s == 2 and self.armor != 0:
                self.inventory.append(self.armor)
                self.armor = 0
            elif s == 3 and self.accessory != 0:
                self.inventory.append(self.accessory)
                self.accessory = 0

    def addexp(self, ex):
        if self.level < self.maxlevel:
            self.exp = self.exp + ex
            if self.exp >= 5:
                self.exp = self.exp - 5
                print("레벨 업!")
                self.levelup()
        else:
            print("")

    def levelup(self):
        self.level = self.level + 1
        if self.level == 2:
            self.critical2 = 20
        elif self.level % 2 == 0:
            self.critical2 = self.critical2 + 20

        self.maxhp = int(self.maxhp * 1.2)
        self.hp = self.maxhp

        self.defence = self.defence + 2
        self.minattack = self.minattack + 5
        self.maxattack = self.maxattack + 6
        for i in self.skills:
            i.mindamage = i.mindamage + 5
            i.maxdamage = i.maxdamage + 5

    def charactersave(self):
        pass

    def characterload(self, c):
        self = c