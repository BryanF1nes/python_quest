from Classes.Character import Character

class Dwarf(Character):
    def __init__(self):
        super().__init__(health=100, speed=3, strength=7, defense=10, mana=10)
        self.engineering = 10
        
    def repair(self):
        if self.engineering < 4:
            return print("I can't repair this... I need to recharge")
        print("Repairing in progress!")
        self.engineering -= 4
        return print("All repaired!")
        
    def getEngineering(self):
        return self.engineering
    
    def special_ability(self):
        return print(f"Special abilities are: repair")