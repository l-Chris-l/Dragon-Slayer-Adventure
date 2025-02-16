import random

#PLAYER CLASSES
class Knight:
    def __init__(self):
        self.health = 150
        self.attack = 25
        self.defense = 15
        self.magic = 0
        self.gold = 100
        self.name = "Knight"
    
    def attack_enemy(self):
        return random.randint(self.attack -5, self.attack +5)
    
    def defend (self):
        return random.randint(self.defense -3, self.defense +3)
    

class Archer:
    def __init__(self):
        self.health = 100
        self.attack = 35
        self.defense = 10
        self.magic = 0
        self.gold = 100
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
        self.gold = 100
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
           "Basic Health Potion": 20,
            "Greater Health Potion": 50,
            "Supreme Health Potion": 100,
            "Basic Armor": 50,
            "Enhanced Armor": 100,
            "Legendary Armor": 200,
            "Scroll of Strength": 50,
            "Scroll of Defense": 50,
            "Scroll of Magic": 50,
            "Scroll of Vitality": 75
        }

    def show_items(self):
        print('\nWelcome to the Shop!')
        print("Available items:")
        for item, price in self.items.items():
            print(f"{item}: {price} gold")

    def buy_items(self, player, item):
        if item == "Basic Health Potion" and player.gold >= self.items[item]:
            player.gold -= self.items[item]
            player.health += 30
            print(f"\nYou bought a Basic Health Potion! Your health is now {player.health}.")
        elif item == "Greater Health Potion" and player.gold >= self.items[item]:
            player.gold -= self.items[item]
            player.health += 60
            print(f"\nYou bought a Greater Health Potion! Your health is now {player.health}.")
        elif item == "Supreme Health Potion" and player.gold >= self.items[item]:
            player.gold -= self.items[item]
            player.health += 100
            print(f"\nYou bought a Supreme Health Potion! Your health is now {player.health}.")
        elif item == "Basic Armor" and player.gold >= self.items[item]:
            player.gold -= self.items[item]
            player.defense += 10
            print(f"\nYou bought Basic Armor! Your defense is now {player.defense}.")
        elif item == "Enhanced Armor" and player.gold >= self.items[item]:
            player.gold -= self.items[item]
            player.defense += 20
            print(f"\nYou bought Enhanced Armor! Your defense is now {player.defense}.")
        elif item == "Legendary Armor" and player.gold >= self.items[item]:
            player.gold -= self.items[item]
            player.defense += 40
            print(f"\nYou bought Legendary Armor! Your defense is now {player.defense}.")
        elif item == "Scroll of Strength" and player.gold >= self.items[item]:
            player.gold -= self.items[item]
            player.attack += 10
            print(f"\nYou bought a Scroll of Strength! Your attack is now {player.attack}.")
        elif item == "Scroll of Defense" and player.gold >= self.items[item]:
            player.gold -= self.items[item]
            player.defense += 10
            print(f"\nYou bought a Scroll of Defense! Your defense is now {player.defense}.")
        elif item == "Scroll of Magic" and player.gold >= self.items[item]:
            player.gold -= self.items[item]
            player.magic += 10
            print(f"\nYou bought a Scroll of Magic! Your magic is now {player.magic}.")
        elif item == "Scroll of Vitality" and player.gold >= self.items[item]:
            player.gold -= self.items[item]
            player.health += 50
            print(f"\nYou bought a Scroll of Vitality! Your health is now {player.health}.")
        else:
            print("\nYou don't have enough gold for that item.")


#DRAGON CLASS
class Dragon:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack