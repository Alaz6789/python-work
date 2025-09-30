from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, nameV, healthV, powerV):
        self.name = nameV
        self.health = healthV
        self.power = powerV

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defend(self):
        pass

class Warrior(Character):
    def __init__(self, nameV, healthV, powerV):
        super().__init__(nameV, healthV, powerV)
        power = 10

    def attack(self):
        print(f"Warrior {self.name} attacks with a mighty sword slash")

    def defend(self):
        print(f"Warrior {self.name} defends with a heavy shield")

class Wizard(Character):
    def __init__(self, nameV, healthV, powerV):
        super().__init__(nameV, healthV, powerV)
        power = 5

    def attack(self):
        print(f"Wizard {self.name} attacks with a blazing fireball")

    def defend(self):
        print(f"Wizard {self.name} defends with a magic barrier")

class Archer(Character):
    def __init__(self, nameV, healthV, powerV):
        super().__init__(nameV, healthV, powerV)
        power = 7

    def attack(self):
        print(f"Archer {self.name} attacks with a swift sharp arrow")

    def defend(self):
        print(f"Archer {self.name} defends by dodging quickly")

Wr1 = Warrior("Han Islat", 100, 10)
Wd1 = Wizard("Eolka Rivel Strashur", 80, 7)
Ar1 = Archer("Nihaku Gastfel", 90, 5)

print(f"Creating characters... \n \nWarrior - Health: {Wr1.health} \nWizard - Health: {Wd1.health} \nArcher - Health: {Ar1.health} \n \nBattle Begins! \n")

Wr1.attack()
Wd1.health = Wd1.health - Wr1.power
Wd1.attack()
Ar1.health = Ar1.health - Wd1.power
Ar1.attack()
Wr1.health = Wr1.health - Ar1.power

print("")

Wr1.defend()
Wr1.defend()
Ar1.defend()

print("")
print(f"After Round 1: \nWarrior - Health: {Wr1.health} \nWizard - Health: {Wd1.health} \nArcher - Health: {Ar1.health} ")