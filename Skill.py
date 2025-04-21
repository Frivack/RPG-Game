import random


class Skill:
    def __init__(self, name, mindamage, maxdamage, sattack, effect):
        self.name = name
        self.mindamage = mindamage
        self.maxdamage = maxdamage
        self.sattack = sattack
        self.effect = effect

    def getDamage(self):
        return random.randrange(self.mindamage, self.maxdamage + 1)

    def showSkill(self):
            print("스킬: %s ㅣ"%self.name, "Min: %s ~"%self.mindamage, "MAX: %s |"%self.maxdamage, "성공율: %s%%"%self.sattack)
