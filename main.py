import random

# Player Classes
class Knight:
    def __init__(self):
        self.health = 150
        self.attack = 25
        self.defense = 15
        self.magic = 0
        self.gold = 100  # Starting gold
        self.name = "Knight"

    def attack_enemy(self):
        return random.randint(self.attack - 5, self.attack + 5)

    def defend(self):
        return random.randint(self.defense - 3, self.defense + 3)

class Archer:
    def __init__(self):
        self.health = 100
        self.attack = 35
        self.defense = 10
        self.magic = 0
        self.gold = 100  # Starting gold
        self.name = "Archer"

    def attack_enemy(self):
        return random.randint(self.attack - 10, self.attack + 10)

    def defend(self):
        return random.randint(self.defense - 2, self.defense + 2)

class Mage:
    def __init__(self):
        self.health = 80
        self.attack = 15
        self.defense = 5
        self.magic = 40
        self.gold = 100  # Starting gold
        self.name = "Mage"

    def attack_enemy(self):
        return random.randint(self.attack - 5, self.attack + 5)

    def defend(self):
        return random.randint(self.defense - 2, self.defense + 2)

    def magic_attack(self):
        return random.randint(self.magic - 10, self.magic + 10)

# Shop System with Potions, Armor, and Scrolls
class Shop:
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
        print("\nWelcome to the Shop!")
        print("Available items:")
        for item, price in self.items.items():
            print(f"{item}: {price} gold")

    def buy_item(self, player, item):
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

# Monster Class (Dragon, Goblin, etc.) with Tiers and Special Abilities
class Monster:
    def __init__(self, name, health, attack, tier):
        self.name = name
        self.health = health
        self.attack = attack
        self.tier = tier
        self.max_health = health  # Save the monster's maximum health for healing checks

    def monster_attack(self):
        return random.randint(self.attack - 5, self.attack + 5)

    def give_gold(self):
        if self.tier == 1:
            return random.randint(10, 20)  # Low-tier monsters
        elif self.tier == 2:
            return random.randint(30, 50)  # Medium-tier monsters
        elif self.tier == 3:
            return random.randint(70, 100)  # High-tier monsters

    def special_ability(self, player):
        if self.tier == 1:
            # Tier 1 monsters: Basic attack boost
            print(f"\n{self.name} performs a basic attack boost!")
            return self.monster_attack()
        elif self.tier == 2:
            # Tier 2 monsters: Poison or healing ability
            ability = random.choice(["Poison", "Heal"])
            if ability == "Poison":
                print(f"\n{self.name} poisons you! You take 10 damage over 3 turns.")
                return 10  # Poison damage
            elif ability == "Heal" and self.health < self.max_health * 0.5:  # Only heal if below 50% health
                heal = random.randint(15, 25)
                self.health += heal
                print(f"\n{self.name} heals itself for {heal} health!")
                return 0  # No damage but heals itself
            else:
                print(f"\n{self.name} attempts to heal, but is already at full health!")
                return 0
        elif self.tier == 3:
            # Tier 3 monsters: Powerful AoE or self-buff
            ability = random.choice(["AoE", "Self Buff"])
            if ability == "AoE":
                print(f"\n{self.name} casts a powerful AoE attack!")
                return self.monster_attack() * 2  # AoE attack
            elif ability == "Self Buff":
                buff = random.randint(10, 30)
                self.attack += buff
                print(f"\n{self.name} buffs its attack by {buff}!")
                return 0  # No damage but increases attack

    def ai_attack(self, player):
        return self.monster_attack()

# Grid-based World Class
class World:
    def __init__(self, player):
        self.grid_size = 12  # Updated to 12x12 grid
        self.grid = [[' ' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.player_x = 6  # Initial position in the middle of the grid (7th row, 7th column)
        self.player_y = 6
        self.player = player
        self.shop = Shop()

        # Add random monsters (dragons, goblins, etc.) to the grid
        self.place_monsters()
        self.place_shops()

        # Game Story Introduction
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
        # Monster data with different tiers (Tier 1: low, Tier 2: medium, Tier 3: high)
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
            self.grid[x][y] = 'S'  # S stands for Shop

    def show_map(self):
        print("\nCurrent Map:")
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if i == self.player_x and j == self.player_y:
                    print("P", end=" ")  # P represents Player's position
                elif isinstance(self.grid[i][j], Monster):
                    print("M", end=" ")  # M represents Monster
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
            self.fight_monster(tile)  # Fix: Corrected to use 'tile' (or 'monster') here
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
        while self.player.health > 0 and monster.health > 0:
            print(f"\nYour health: {self.player.health}")
            print(f"{monster.name}'s health: {monster.health}")
            print("What will you do?")
            print("1. Attack.")
            print("2. Defend.")
            if isinstance(self.player, Mage):
                print("3. Use Magic Attack.")
            
            choice = input("Enter 1, 2, or 3: ")

            if choice == "1":
                damage = self.player.attack_enemy()
                monster.health -= damage
                print(f"\nYou attacked {monster.name} and dealt {damage} damage!")
            elif choice == "2":
                defense = self.player.defend()
                print(f"\nYou defend with {defense} defense!")
            elif isinstance(self.player, Mage) and choice == "3":
                magic_damage = self.player.magic_attack()
                monster.health -= magic_damage
                print(f"\nYou used a Magic Attack on {monster.name} and dealt {magic_damage} damage!")
            else:
                print("\nInvalid choice! Please try again.")

            # Monster's turn to attack
            if monster.health > 0:
                special_ability_damage = monster.special_ability(self.player)
                if special_ability_damage > 0:
                    self.player.health -= special_ability_damage
                    print(f"\n{monster.name} dealt {special_ability_damage} damage!")
                else:
                    print(f"\n{monster.name} uses a special ability!")

            if self.player.health <= 0:
                print("\nYou have been defeated! Game Over.")
                break
            if monster.health <= 0:
                print(f"\nYou defeated the {monster.name}!")
                self.player.gold += monster.give_gold()
                print(f"\nYou received {monster.give_gold()} gold!")
                break

# Game Loop
def game_loop():
    # Choose Player Class
    print("Choose your character class:")
    print("1. Knight")
    print("2. Archer")
    print("3. Mage")
    class_choice = input("Enter 1, 2, or 3: ")

    if class_choice == "1":
        player = Knight()
    elif class_choice == "2":
        player = Archer()
    elif class_choice == "3":
        player = Mage()
    else:
        print("\nInvalid choice! Defaulting to Knight.")
        player = Knight()

    # Create World
    world = World(player)

    # Game loop
    while player.health > 0:
        world.show_map()
        print("\nWhat would you like to do?")
        print("1. Move")
        print("2. Explore")
        print("3. Visit Shop")
        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            direction = input("Which direction would you like to move? (north/south/east/west): ")
            world.move_player(direction)
        elif choice == "2":
            world.explore()
        elif choice == "3":
            world.visit_shop()
        else:
            print("Invalid choice!")

        if player.health <= 0:
            print("Game Over! You've been defeated.")
            break

# Start the Game
if __name__ == "__main__":
    game_loop()
