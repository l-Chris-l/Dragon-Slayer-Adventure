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


 #SHOP SYSTEM
class shop:
    def __init__(self):
        self.items = {
            "Health Potions": 20,
            "Armor": 50,
            "Magic Scroll": 70,
            "Ice Sword": 100,
            "Fire Sword": 100
        }

    def show_items(self):
        print('\nWelcome to the Shop!')
        print("Available items:")
        for item, price in self.items.items():
            print(f"{item}: {price} gold")

    def buy_items(self, player, item):
        if item == "Health Potion" and player.gold >= self.items[item]:
            player.gold -= self.items[item]
            player.health += 50
            print(f"\nYou bought a Health Potion! Your health is now {player.health}.")
        elif item =="Armor" and player.gold >= self.items[item]:
            player.gold -= self.items[item]
            player.defense += 10
            print(f'\nYou bought Armor! Your defense is now {player.defense}')
        elif item == "Magic Scroll" and player.gold >= self.items[item]:
            player.gold -= self.items[item]
            player.magic += 20
            print(f'\nYou bought a Magic Scroll! Your magic power is now {player.magic}.')
        else:
            print("\nYou don't have enough gold for that item.")
   