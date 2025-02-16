import random

#PLAYER CLASSES
class Knight:
    def __init__(self):
        self.health = 150
        self.attack = 25
        self.defense = 15
        self.magic = 0
        self.name = "Knight"
    
    def attack_enemy(self):
        return random.randint(self.attack -5, self.attack +5)
    
    def defend (self):
        return random.randint(self.defense -3, self.defense+3)
    

class Archer:
    def __init__(self):
        self.health = 100
        self.attack = 35
        self.defense = 10
        self.magic = 0
        self.name = "Archer"

    def attack_enemy(self):
        return random.randint(self.attack -10, self.attack +10)
    
    def defend(self):
        return random.randint(self.defense -2, self.defense +2)
    

class Mage:
    def __init__(self):
        self.health = 80
        self.attack = 15
        self.defense = 5
        self.magic = 40
        self.name = "Mage"

    def attack_enemy(self):
        return random.randint(self.attack -5, self.attack +5)
    
    def defend(self):
        return random.randint(self.defense -2 self.defense +2)
    
    def magic_attack(self):
        return random.randint(self.magic -10, self.magic +10)

    