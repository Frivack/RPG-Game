import random
from Skill import *
from Creature import *

class gameclass(Creature):
    randomattack = random.randint(1, 2)
    randomgold = random.randint(1, 100)
    choosemaping = 0
    mapcliker = 1
    choosemonster = 0
    skillchoose = 3
    savemonster = 0
    skillattack = 0
    skilleffect = 0
    chooseskill = 0
    golddropmonster = 0
    chooseattack = 0
    totalgold = 0

    def __init__(self, choose):
        self.choosemonster = choose
        if self.choosemonster == 1:
            self.savemonster = "Darin"
            self.attack = 10
            self.defence = 10
            self.hp = 50
            self.chooseskill = "검 휘두르기"
            self.skillattack = 20
            self.skilleffect = 0
            self.golddropmonster = 10
            print("Darin몬스터가 나왔습니다.")
        elif self.choosemonster == 2:
            self.savemonster = "Scarlet"
            self.attack = 30
            self.defence = 5
            self.hp = 25
            self.chooseskill = "A motive force"
            self.skillattack = 60
            self.skilleffect = 0
            self.golddropmonster = 20
            print("Scarlet몬스터가 나왔습니다.")
        elif self.choosemonster == 3:
            self.savemonster = "Narin"
            self.attack = 50
            self.defence = 10
            self.hp = 70
            self.chooseskill = "최면술"
            self.skillattack = 0
            self.skilleffect = 1
            self.golddropmonster = 30
            print("Narin몬스터가 나왔습니다.")
        elif self.choosemonster == 4:
            self.savemonster = "Darong"
            self.attack = 10
            self.defence = 100
            self.hp = 200
            self.chooseskill = "방어"
            self.skillattack = 0
            self.skilleffect = 2
            self.golddropmonster = 40
            print("Darong몬스터가 나왔습니다.")
        elif self.choosemonster == 5:
            self.savemonster = "Arong"
            self.attack = 50
            self.defence = 20
            self.hp = 150
            self.chooseskill = "속임수"
            self.skillattack = 100
            self.skilleffect = 0
            self.golddropmonster = 50 + 50
            print("Arong몬스터가 나왔습니다.")
        elif self.choosemonster == 6:
            self.savemonster = "Scaramouche"
            self.attack = 100
            self.defence = 100
            self.hp = 500
            self.chooseskill = "지구 던지기"
            self.skillattack = 200
            self.skilleffect = 0
            self.golddropmonster = 60
            print("Scaramouche몬스터가 나왔습니다.")
        elif self.choosemonster == 7:
            self.savemonster = "Dongwon"
            self.attack = 30
            self.defence = 50
            self.hp = 250
            self.chooseskill = "검 휘두르기"
            self.skillattack = 60
            self.skilleffect = 0
            self.golddropmonster = 70
            print("Dongwon몬스터가 나왔습니다.")
        elif self.choosemonster == 8:
            self.savemonster = "Yaco"
            self.attack = 70
            self.defence = 20
            self.hp = 200
            self.chooseskill = "속임수"
            self.skillattack = 140
            self.skilleffect = 0
            self.golddropmonster = 80
            print("Yaco몬스터가 나왔습니다.")
        elif self.choosemonster == 9:
            self.savemonster = "Ganghoon"
            self.attack = 20
            self.defence = 100
            self.hp = 350
            self.chooseskill = "방어"
            self.skillattack = 0
            self.skilleffect = 2
            self.golddropmonster = 90
            print("Ganghoon몬스터가 나왔습니다.")
        elif self.choosemonster == 10:
            self.savemonster = "Sprigatito"
            self.attack = 70
            self.defence = 50
            self.hp = 200
            self.chooseskill = "A motive force"
            self.skillattack = 140
            self.skilleffect = 0
            self.golddropmonster = 100
            print("Sprigatito몬스터가 나왔습니다.")
        elif self.choosemonster == 11:
            self.savemonster = "Zoroark"
            self.attack = 80
            self.defence = 50
            self.hp = 300
            self.chooseskill = "속임수"
            self.skillattack = 160
            self.skilleffect = 0
            self.golddropmonster = 110
            print("Zoroark몬스터가 나왔습니다.")
        elif self.choosemonster == 12:
            self.savemonster = "Raiden Shogun"
            self.attack = 500
            self.defence = 500
            self.hp = 1000
            self.chooseskill = "A break of thought "
            self.skillattack = 9999
            self.skilleffect = 3
            self.golddropmonster = 10000
            print("Raiden Shogun몬스터가 나왔습니다.")
        else:
            print("숫자를 잘못 입력하였습니다.")

    def attackto(self):
        #print("몬스터의 체력은: ", self.hp)
        #print("몬스터의 공격력은: ", self.attack)
        if self.randomattack == 1:
            charskill = self.skillattack
            self.hp = self.hp
            print(self.savemonster, "(이)가 %s 스킬을 사용했습니다." % self.chooseskill)
        elif self.randomattack == 2:
            self.hp = self.hp
            print(self.savemonster, "(이)가 %s 데미지의 일반공격을 합니다." % self.attack)
        return self.attack

    def attacked(self, charattacked):
        damage = charattacked - self.defence
        if charattacked == 0:
            pass
        elif damage > 0:
            self.hp = self.hp - charattacked
            if self.hp <= 0:
                #print("몬스터는 사망하였습니다.")
                return 0
            else:
                print("몬스터에게 %s만큼의 데미지를 입힘"%damage)
                print("몬스터의 남은 피는: ", self.hp)
        else:
            print("몬스터가 공격을 막았습니다.")
        return 1

    def skilleffective(self):
        if self.skilleffect == 0:
            print("스킬 공격력: %s, 스킬 효과: 없음" % self.skillattack)
            print(self.savemonster, "(이)가 플레이어에게 ", self.skillattack, "의 데미지와 %s 효과를 입힘" % self.skilleffect)
        elif self.skilleffect == 1:
            print("스킬 공격력: %s, 스킬 효과: 잠듦" % self.skillattack)
        elif self.skilleffect == 2:
            print("스킬 공격력: %s, 스킬 효과: 공격 무시" % self.skillattack)
        elif self.skilleffect == 3:
            print("스킬 공격력: %s, 스킬 효과: 즉사" % self.skillattack)
        else:
            print("오류: 몬스터 스킬 이펙트 번호 잘못 지정됨")
        return self.skillattack, self.skilleffect

    # def attackdamage(self, charattack):
    #     if randomskill == 1:
    #         charskill = self.skillattack
    #         self.hp = self.hp - charskill
    #         print(self.savemonster, "(이)가 플레이어에게 %s 스킬이 나갔습니다." % self.chooseskill)
    #     elif randomskill == 2:
    #         self.hp = self.hp - charattack
    #         print(self.savemonster, "(이)가 플레이어에게 %s만큼의 데미지의 일반공격이 나갔습니다." % self.attack)

    def golddrop(self):
        self.totalgold = self.golddropmonster + self.randomgold
        print("몬스터 잡기 보상 %s골드 + 랜덤 골드 상자 %s골드로 총 %s골드가 인벤토리에 추가되었습니다." % (self.golddropmonster, self.randomgold, self.totalgold))
        print("=" * 100)
        print("몬스터가 사망하였습니다. 승리하셨습니다. 다음 몬스터를 학살하여 주십시오.")
        print("=" * 100)
        return self.totalgold
        #self.effect = effect

    def expdrop(self):
        return random.randrange(1, self.choosemonster * 2)
