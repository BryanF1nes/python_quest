from Classes.Goblin import Goblin
from Classes.Dwarf import Dwarf
from Classes.Elf import Elf
from Classes.Priest import Priest

def main():
    print("EverQuest loading....")
    print("It's time!")
    name = input("What is your name adventurer? ")
    race = input("Select a race, ('Goblin', 'Dwarf', 'Elf', 'Priest', 'Warrior'): ")
    startAdventure(name, race)

def startAdventure(name, race):
    race_classes = {
        'Goblin': Goblin,
        'Dwarf': Dwarf,
        'Elf': Elf,
        'Priest': Priest,
    }
    
    if race in race_classes:
        character_class = race_classes[race]
        character = character_class()
        print(f"Hello {name}... Welcome to EverQuest.")
        print(f"A {race} I see... well lets begin!")
        print(f"Your stats are: Health: {character.health} Strength: {character.strength} Speed: {character.speed} Defense: {character.defense} Level: {character.level}")
        character.special_ability()
    else:
        print(f"Unknown race: {race}. Please select a valid race.")
    return

main()
