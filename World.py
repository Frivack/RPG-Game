from Monster import *
from Character import *
from Item import *
from Place import *
from SaveManager import *

class World:
    player = 0
    money = 0
    inventory = []
    map = []
    locate = 0  # current location
    savemanager = SaveManager()

    def __init__(self):
        p[2].setitems(L[0], L[1], L[2], L[3], L[4], L[5], L[10], L[11], L[12], L[13], L[14], L[19], L[20], L[21], L[22], L[23])
        p[7].setitems(L[5], L[6], L[7], L[8], L[9], L[10], L[15], L[16], L[17], L[18], L[22], L[23], L[24], L[25])

    def start(self):
        while 1:
            print("1. 전사")
            print("2. 마법사")
            print("3. 궁수")
            print("4. 창기사")
            print("5. 격투사")
            print("6. 언데드")
            s = int(input("캐릭터 선택:"))
            if 0 < s <= 6:
                self.player = character(s, 1)
                s = int(input("선택하시겠습니까? (1. 확인, 2. 취소)"))
                if s == 1:
                    self.player.gold = 100
                    self.player.inventory.append(L[0])
                    self.player.inventory.append(L[11])
                    self.player.inventory.append(L[19])
                    break
                else:
                    print("다시 입력하세요.")
            else:
                print("다시 입력하세요.")

    def play(self):
        t = self.action()
        if t == 0:
            return 0
        return 1


    def action(self):
        print("-"*20)
        print("행동을 선택하세요.")
        print("1. 캐릭터 정보 확인")
        print("2. 이동")
        print("3. 행동")
        f = p[self.locate].placef
        if f == 1 or f == 9:
            print("4. 회복")
        elif f == 2:
            print("4. 아이템 구매")
            print("5. 아이템 판매")
        print("9. 메뉴")
        print("-"*20)

        s = int(input("선택: "))
        if s == 1:
            self.player.showCharacter()
        elif s == 2:
            self.locate = p[self.locate].move(p)
            if p[self.locate].placef == 8:  # 함정일 경우, 이동했을 때 한번만 작동
                ran = p[self.locate].trap(len(self.player.inventory))
                self.player.inventory[ran].showinfo()
                print("해당 아이템이 파괴되었습니다!")
                del self.player.inventory[ran]
        elif s == 3:
            p[self.locate].placeAction()
        elif s == 4:
            if f == 1:#집일 경우
                self.player.hp = p[self.locate].rest(self.player.maxhp)
            elif f == 2:#가게일 경우
                self.player.buy(p[self.locate].buy())
            elif f == 9:#병원일 경우
                self.player.hp = p[self.locate].hospital(self.player.maxhp)
        elif s == 5:
            if f == 2:#가게일 경우
                self.player.sell()
        elif s == 9:  # 메뉴
            print("-"*20)
            print("1. 저장")
            print("2. 불러오기")
            print("3. 종료")
            print("-"*20)
            s = int(input("선택: "))
            if s == 1:
                self.save()
            elif s == 2:
                self.load()
            elif s == 3:
                print("프로그램 종료")
                return 0

        if p[self.locate].placef == 5 and random.randrange(0, 10) < 9:#던전에서 90% 확률로 몬스터 등장
            self.battle(gameclass(p[self.locate].monsterN()))

        return 1

    def battle(self, mob):
        while True:
            survived = mob.attacked(self.player.attackto())
            if survived == 0:
                self.player.gold = self.player.gold + mob.golddrop()
                self.player.addexp(mob.expdrop())
                break
            self.player.attacked(mob.attackto())
            if self.player.hp <= 0:
                self.playerdead()
                break

    def playerdead(self):
        self.locate = 15
        self.player.gold = int(self.player.gold * 0.5)
        print("패배하였습니다!\n보유 골드의 반을잃었습니다.\n지나가던 모험자가 당신을 구출하여 행운병원으로 이송하였습니다.")
        self.player.hp = p[self.locate].hospital(self.player.maxhp)
        self.player.addexp(1)

    def save(self):
        self.savemanager.saveCharacter(self.player, self.locate)
        print("저장 완료")

    def load(self):
        self.player, self.locate = self.savemanager.loadCharacter()
        print("불러오기 완료")
