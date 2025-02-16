import random

# PLAYER CLASSES
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


 # SHOP SYSTEM
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


# MONSTER CLASS CLASSES WITH TIERS
class Monster:
    def __init__(self, name, health, attack, tier):
        self.name = name
        self.health = health
        self.attack = attack
        self.tier = tier

    def monster_attack(self):
        return random.randint(self.attack - 10, self.attack + 10)

    def give_gold(self):
        if self.tier == 1:
            return random.randint(10, 20)  # LOW-TIER MONSTERS
        elif self.tier == 2:
            return random.randint(30, 50)  # MEDIUM TIER MONSTERS
        elif self.tier == 3:
            return random.randint(70, 100)  # HIGH TIER MONSTERS
# GRID-BASED WORLD CLASS
class World:
    def __init__(self, player):
        self.grid_size = 10 # 10X10 GRID
        self.grid = [[' ' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.player_x = 6  # INITIAL POSITION IN THE MIDDLE OF THE GRID (7TH ROW, 7TH COLUM)
        self.player_y = 6
        self.player = player
        self.shop = shop()

        # ADD RANDOM MONSTERS TO THE GRID
        self.place_monsters()
        self.place_shops()

        # GAME STORY INTRODUCTION
        self.story_introduction()

    def story_introduction(self):
        print("\n--- Welcome to the Kingdom of Eldora ---\n")
        print("A dark and dangerous force has begun to invade the peaceful lands of Eldora.")
        print("Dragons, goblins, and other monstrous creatures roam freely, terrorizing villages.")
        print("The kingdom's only hope lies with you, a brave adventurer, who must journey across the land,")
        print("defeat these creatures, and ultimately confront the evil dragon king who leads them.")
        print("Gather strength, make wise choices, and choose your path carefully.\n")
        print("Your adventure begins now.\n")

    def place_monsters(self):
        # MONSTER DATA WITH DIFFERENT TIERS
        monster_data = [
            ("Goblin", 50, 10, 1),
            ("Zombie", 60, 8, 1),
            ("Dragon Hatchling", 60, 15, 1),
            ("Troll", 150, 20, 2),
            ("Griffin", 90, 40, 2),
            ("Phoenix", 110, 30, 2),
            ("Vampire", 85, 22, 2),
            ("Fire Dragon", 120, 25, 3),
            ("Ice Dragon", 100, 30, 3),
            ("Lightning Dragon", 80, 35, 3),
            ("Dark Dragon", 130, 28, 3),
            ("Dragon King", 200, 50, 3),
            ("Werewolf", 95, 25, 2),
            ("Dragon Slayer", 150, 40, 3),
            ("Earth Elemental", 100, 20, 2)
        ]
        
        monster_positions = random.sample([(x, y) for x in range(self.grid_size) for y in range(self.grid_size)], 15)
        
        for i, (x, y) in enumerate(monster_positions):
            monster_name, health, attack, tier = monster_data[i]
            self.grid[x][y] = Monster(monster_name, health, attack, tier)

    def place_shops(self):
        shop_positions = random.sample([(random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)) for _ in range(3)], 3)
        for x, y in shop_positions:
            self.grid[x][y] = 'S'  # S STANDS FOR SHOP

    def show_map(self):
        print("\nCurrent Map:")
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if i == self.player_x and j == self.player_y:
                    print("P", end=" ")  # P REPRESENTS PLAYER'S POSITION
                elif isinstance(self.grid[i][j], Monster):
                    print("M", end=" ")  # M REPRESENTS MONSTER
                else:
                    print(self.grid[i][j], end=" ")
            print()

    def move_player(self, direction):
        if direction == "north" and self.player_x > 0:
            self.player_x -= 1
        elif direction == "south" and self.player_x < self.grid_size - 1:
            self.player_x += 1
        elif direction == "east" and self.player_y < self.grid_size - 1:
            self.player_y += 1
        elif direction == "west" and self.player_y > 0:
            self.player_y -= 1
        else:
            print("You can't move in that direction!")

    def explore(self):
        tile = self.grid[self.player_x][self.player_y]
        if isinstance(tile, Monster):
            print(f"\nYou've encountered a {tile.name}!")
            self.fight_monster(tile)
        elif tile == 'S':
            self.visit_shop()
        else:
            print("\nThe area is empty. Move to another tile to find something!")

    def visit_shop(self):
        print("\nYou find a shop. Would you like to buy something?")
        self.shop.show_items()
        item_choice = input("Enter the name of the item you want to buy: ")
        self.shop.buy_item(self.player, item_choice)

    def fight_monster(self, monster):
        print(f"\nA fierce battle begins against the {monster.name}!")
        player_health = self.player.health
        monster_health = monster.health

        while player_health > 0 and monster_health > 0:
            print(f"\nYour health: {player_health}")
            print(f"{monster.name}'s health: {monster_health}")
            print("What will you do?")
            print("1. Attack.")
            print("2. Defend.")
            if isinstance(self.player, Mage):
                print("3. Use Magic Attack.")
            
            choice = input("Enter 1, 2, or 3: ")

            if choice == "1":
                damage = self.player.attack_enemy()
                monster_health -= damage
                print(f"\nYou attack the {monster.name} and deal {damage} damage!")
            elif choice == "2":
                defense = self.player.defend()
                monster_attack = monster.monster_attack() - defense
                if monster_attack > 0:
                    player_health -= monster_attack
                    print(f"\nYou defend! The {monster.name} deals {monster_attack} damage.")
                else:
                    print("\nYour defense was strong enough to block the attack!")
            elif choice == "3" and isinstance(self.player, Mage):
                magic_damage = self.player.magic_attack()
                monster_health -= magic_damage
                print(f"\nYou cast a magic spell and deal {magic_damage} magic damage!")
            else:
                print("\nInvalid choice! Try again.")
            
            if monster_health <= 0:
                print(f"\nYou defeated the {monster.name}!")
                self.player.gold += monster.give_gold()
                print(f"You earned {monster.give_gold()} gold!")
            elif player_health <= 0:
                print("\nYou have been defeated!")
                break


# MAIN GAME LOOP
def main():
    print("Choose your character class:")
    print("1. Knight")
    print("2. Archer")
    print("3. Mage")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        player = Knight()
    elif choice == "2":
        player = Archer()
    elif choice == "3":
        player = Mage()
    else:
        print("Invalid choice. Defaulting to Knight.")
        player = Knight()

    world = World(player)

    while True:
        world.show_map()
        print(f"\nYour current gold: {player.gold}")
        print(f"Your current health: {player.health}")
        print(f"Your current attack: {player.attack}")
        print(f"Your current defense: {player.defense}")
        print(f"Your current magic: {player.magic}")

        print("\nWhat would you like to do?")
        print("1. Move")
        print("2. Explore")
        print("3. Quit Game")

        action = input("Enter 1, 2, or 3: ")

        if action == "1":
            direction = input("Which direction would you like to move? (north, south, east, west): ")
            world.move_player(direction)
        elif action == "2":
            world.explore()
        elif action == "3":
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# START THE GAME
if __name__ == "__main__":
    main()