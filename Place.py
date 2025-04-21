import random
import Item


class place:
    placename = 0
    placec = 0
    placef = 0
    placeconnect = 0
    monster = 0
    items = []

    def __init__(self, placename, placelocation, placef, placeconnect, monster):
        self.placename = placename
        self.placelocation = placelocation
        self.placef = placef
        self.placeconnect = placeconnect
        self.monster = monster

    def sell(self, name):
        pass

    def buy(self):
        count = 1
        for i in self.items:
            print("%s." % count, end = " ")
            i.showinfo()
            count = count + 1
        itbuy = int(input("구매할 물건을 선택하시오."))
        if itbuy <= len(self.items) and itbuy > 0:
            print("%s 아이템을 선택하였습니다." % self.items[itbuy - 1].name)
            return self.items[itbuy - 1]

    def move(self, allcountry):
        print("현재 위치:", self.placename)
        k = 0
        for i in self.placeconnect:
            k = k + 1
            print("%s." % k, allcountry[i].placename)
        w = int(input("이동할 장소를 입력하시오:"))
        if 0 < w <= k:
            print("%s로 이동" % allcountry[self.placeconnect[w - 1]].placename)
            return self.placeconnect[w - 1]
        else:
            print("이동할 장소가 없습니다.")
            return self.placelocation

    def setitems(self, *it):
        self.items = it

    def monsterN(self):
        if 0 != self.monster:
            return random.choice(self.monster)

    def rest(self, max):
        print("집에서 휴식을 취하였습니다.")
        return max

    def trap(self, itemN):
        print("함정에 걸렸습니다.")
        return random.randrange(0, itemN)

    def hospital(self, max):
        print("병원에서 치료를 받아 회복되었습니다.")
        return max

    def placeAction(self):
        if self.placef == 0:
            print("마을 길을 걸으니 심신이 안정되었습니다.")
        elif self.placef == 1:
            print("집에서 휴식할 수 있습니다.")
        elif self.placef == 2:
            print("가게에서 물건을 사고팔수 있습니다.")
        elif self.placef == 3:
            print("시내에 도착하였습니다, 어디든 가볍게 둘러보세요.")
        elif self.placef == 4:
            print("공터에 도착하였습니다, 어디든 가볍게 걸어보세요.")
        elif self.placef == 5:
            print("던전입니다. 몬스터가 나올 수 있으니 '행동'에 주의하세요.")
        elif self.placef == 6:
            print("강력한 몬스터가 있는 던전입니다.")
        elif self.placef == 7:
            print("매우 강한 몬스터가 있는 던전입니다. 후퇴를 고려하세요.")
        elif self.placef == 8:
            print("함정에 빠지셨습니다, 주의를 기울이세요.")
        elif self.placef == 9:
            print("병원에서 휴식할 수 있습니다.")
        elif self.placef == 10:
            print("바다를 봤더니 심신이 안정되었습니다.")


p = []  # placef 마을=0 집=1 가게=2 시내=3 공터=4 던전=5 중간보스룸=6 최종보스룸=7 함정= 8 병원=9 바다=10
p.append(place("씨플마을", 0, 0, [1, 2, 3, 17], [0]))
p.append(place("이층집", 1, 1, [0, 2], [0]))
p.append(place("태초가게", 2, 2, [0, 15], [0]))
p.append(place("강남시내", 3, 3, [0, 4], [0]))
p.append(place("넓은 공터", 4, 4, [3, 5, 7], [0]))
p.append(place("가나던전", 5, 5, [4], [1, 2, 3]))  # 던전은 몬스터 숫자, 없으면 0
p.append(place("파이썬마을", 6, 0, [8], [0]))
p.append(place("대박가게", 7, 2, [4, 9], [5, 10]))
p.append(place("아파트", 8, 1, [6, 9, 13], [0]))
p.append(place("푸른바다", 9, 10, [7, 8, 10, 11], [0]))
p.append(place("좁은 공터", 10, 4, [9], [0]))
p.append(place("다라던전", 11, 5, [9, 12], [4, 5, 7]))
p.append(place("중간보스룸", 12, 6, [11], [6]))
p.append(place("청담시내", 13, 3, [8, 15], [0]))
p.append(place("함정", 14, 8, [15], [0]))
p.append(place("행운병원", 15, 9, [2, 13, 14, 16], [0]))
p.append(place("마바던전", 16, 5, [15], [8, 9, 10, 11]))
p.append(place("자바마을", 17, 0, [0, 18], [0]))
p.append(place("펜트하우스", 18, 1, [17, 19], [0]))
p.append(place("최종보스룸", 19, 7, [18], [13]))
