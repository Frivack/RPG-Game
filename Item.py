class Item:
    value = 0
    name = 0
    part = 0
    attack = 0
    defense = 0
    recovery = 0
    luck = 0

    def __init__(self, value, name, part, attack, defense=0, luck=0, recovery=0):
        self.value = value
        self.name = name
        self.part = part
        self.attack = attack
        self.defense = defense
        self.recovery = recovery
        self.luck = luck

    def showinfo(self):
        print("%s ㅣ" % self.name, "%s골드 ㅣ" % self.value, "분류: %s ㅣ" % self.part, end = "")
        if self.attack != 0:
            print("공격력:", self.attack, end = "| ")
        if self.defense != 0:
            print("방어력:", self.defense, end = "| ")
        if self.luck != 0:
            print("행운:", self.luck, end = "| ")
        if self.recovery != 0:
            print("회복:", self.recovery, end = "| ")
        print()


L = []
L.append(Item(10, "초보자의 검", "공격", 15))  # 0
L.append(Item(25, "징수의 총", "공격", 20))  # 1
L.append(Item(30, "무한의 대검", "공격", 25))  # 2
L.append(Item(50, "대천사의 지팡이", "공격", 40))  # 3
L.append(Item(65, "공허의 지팡이", "공격", 50))  # 4
L.append(Item(55, "만년서리", "공격", 55))  # 5
L.append(Item(65, "혹한의 손길", "공격", 60))  # 6
L.append(Item(65, "어둠의 능력자", "공격", 65))  # 7
L.append(Item(120, "악마의 포효", "공격", 100))  # 8
L.append(Item(175, "사건의 지평선", "공격", 15))  # 9

L.append(Item(10, "초보자의 옷", "방어", 0, 10))  # 10
L.append(Item(20, "태양불꽃", "방어", 0, 20))  # 11
L.append(Item(50, "저녁갑주", "방어", 0, 30))  # 12
L.append(Item(70, "창과 방패", "방어", 0, 50))  # 13
L.append(Item(75, "그림자불꽃", "방어", 0, 60))  # 14
L.append(Item(75, "광전사의 갑옷", "방어", 0, 70))  # 15
L.append(Item(60, "언데드의 방패", "방어", 0, 75))  # 16
L.append(Item(115, "교수님의 과제방패", "방어", 0, 100))  # 17
L.append(Item(75, "종말의 겨울", "방어", 20, 20, 10))  # 18

L.append(Item(15, "초보자의 장갑", "악세사리", 0, 10, 5))  # 19
L.append(Item(40, "무도의 가면", "악세사리", 0, 30))  # 20
L.append(Item(30, "워모그갑옷", "악세사리", 0, 0, 0, 40))  # 21
L.append(Item(40, "인피니트 건틀렛", "악세사리", 35))  # 22
L.append(Item(35, "공주귀걸이", "악세사리", 30))  # 23
L.append(Item(50, "덴탈마스크", "악세사리", 0, 40, 10))  # 24
L.append(Item(40, "마법사의 잃어버린 안경", "악세사리", 0, 0, 0, 50))  # 25
