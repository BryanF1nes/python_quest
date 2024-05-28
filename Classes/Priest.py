from Classes.Character import Character

class Priest(Character):
    def __init__(self):
        super().__init__(health=70, speed=10, strength=5, defense=3, mana=20)
        self.healingPower = 5
        
    def heal(self, target):
        if target == None:
            return print(f"Invalid target to heal.")
        target.health += self.healingPower
        return print(f"{target} has been healed {self.healingPower} health.")
    
    def special_ability(self):
        return print(f"Special abilities are: heal")