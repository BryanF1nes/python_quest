from Classes.Goblin import Goblin
from Classes.Dwarf import Dwarf
from Classes.Elf import Elf
from Classes.Priest import Priest
from Classes.Warrior import Warrior

# Modules
from Modules.Leftstory import Left_story

name = input("What is your name adventurer? ")

def main():
    print("EverQuest loading....")
    print("It's time!")
    race = input("Select a race, ('Goblin', 'Dwarf', 'Elf', 'Priest', 'Warrior'): ")
    startAdventure(race)

def startAdventure(race):
    race_classes = {
        'Goblin': Goblin,
        'Dwarf': Dwarf,
        'Elf': Elf,
        'Priest': Priest,
        'Warrior': Warrior,
    }
    
    if race in race_classes:
        character_class = race_classes[race]
        character = character_class()
        print(f"Hello {name}... Welcome to EverQuest.")
        print(f"A {race} I see... well lets begin!")
        print(f"Your stats are: Health: {character.health} Strength: {character.strength} Speed: {character.speed} Defense: {character.defense} Level: {character.level}")
        character.special_ability()
        print("The sun begins to rise and two paths show themselves..to the left a narrow road that leads to what appears to be a dense and tall forest.")
        print("To the right a road that appears to lead to a healthy and thriving city encased in crystal.")
        print(f"Where would you would like to go {name}.")
        my_input = input(f"{name} chooses to go (left) or (right): ")
        Options(my_input)
    else:
        print(f"Unknown race: {race}. Please select a valid race.")
    return

def Options(input):
    if input == 'left':
        return Left_story()


main()
