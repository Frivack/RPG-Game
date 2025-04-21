from Character import *
from Skill import *
from Item import *


class SaveManager:
    address = "RPGsave.txt"
    saveFile = 0

    def __init__(self):
        self.saveFile = open(self.address, "a")
        self.saveFile.close()

    def saveCharacter(self, ch, p):
        self.saveFile = open(self.address, "w")
        l = []

        l.append(ch.name)
        l.append(ch.hp)
        l.append(ch.maxhp)
        l.append(ch.maxattack)
        l.append(ch.minattack)
        l.append(ch.defence)
        l.append(ch.evasion)
        l.append(ch.critical)
        l.append(ch.critical2)
        l.append(ch.lucky)
        l.append(ch.level)
        l.append(ch.exp)
        l.append(ch.gold)
        l.append(p)

        l.append('\n')

        for i in ch.skills:
            l.append(i.name)
            l.append(i.mindamage)
            l.append(i.maxdamage)
            l.append(i.sattack)
            l.append(i.effect)

        l.append('\n')

        l2 = [ch.weapon, ch.armor, ch.accessory]
        for i in l2:
            if i != 0:
                l.append(i.value)
                l.append(i.name)
                l.append(i.part)
                l.append(i.attack)
                l.append(i.defense)
                l.append(i.recovery)
                l.append(i.luck)
            else:
                l.append('0')
            l.append('\n')

        for i in ch.inventory:
                l.append(i.value)
                l.append(i.name)
                l.append(i.part)
                l.append(i.attack)
                l.append(i.defense)
                l.append(i.recovery)
                l.append(i.luck)
                l.append('\n')

        for i in range(0, len(l)):
            if type(l[i]) != "str":
                l[i] = str(l[i])
            if l[i] != '\n':
                l[i] = l[i] + ","
        self.saveFile.writelines(l)

        self.saveFile.close()

    def loadCharacter(self):
        c = character(0)
        p = 0

        # 스텟 불러오기
        self.saveFile = open(self.address, "rt")
        l = self.saveFile.readline().split(',')
        for i in range(0, len(l)):
            if l[i].isdigit():
                l[i] = int(l[i])
        c.name = l[0]
        c.hp = l[1]
        c.maxhp = l[2]
        c.maxattack = l[3]
        c.minattack = l[4]
        c.defence = l[5]
        c.evasion = l[6]
        c.critical = l[7]
        c.critical2 = l[8]
        c.lucky = l[9]
        c.level = l[10]
        c.exp = l[11]
        c.gold = l[12]
        p = l[13]

        # 스킬 불러오기
        l = self.saveFile.readline().split(',')
        s = []
        for i in range(0, int(len(l)) - 5, 5):
            s.append(Skill(l[i], l[i + 1], l[i + 2], l[i + 3], l[i + 4]))
        c.skills = s

        # 장착 아이템 불러오기
        l = self.saveFile.readline().split(',')
        if l[0] != '0':
            for i in range(0, len(l)):
                if l[i].isdigit():
                    l[i] = int(l[i])
            it = Item(l[0], l[1], l[2], l[3], l[4], l[5], l[6])
            c.weapon = it

        l = self.saveFile.readline().split(',')
        if l[0] != '0':
            for i in range(0, len(l)):
                if l[i].isdigit():
                    l[i] = int(l[i])
            it = Item(l[0], l[1], l[2], l[3], l[4], l[5], l[6])
            c.armor = it

        l = self.saveFile.readline().split(',')
        if l[0] != '0':
            for i in range(0, len(l)):
                if l[i].isdigit():
                    l[i] = int(l[i])
            it = Item(l[0], l[1], l[2], l[3], l[4], l[5], l[6])
            c.accessory = it

        # 인벤토리 불러오기
        while 1:
            l = self.saveFile.readline().split(',')
            if l[0] == '':
                break
            it = Item(l[0], l[1], l[2], l[3], l[4], l[5], l[6])
            c.inventory.append(it)

        return c, p
