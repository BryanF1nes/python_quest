from Classes.Character import Character

class Priest(Character):
    def __init__(self):
        super().__init__(health=70, speed=10, strength=5, defense=3, mana=20)
        self.healing_power = 5
        
    def heal(self, target):
        if target == None:
            return print(f"Invalid target to heal.")
        target.health += self.healing_power
        return print(f"{target} has been healed {self.healing_power} health.")
    
    def get_healing_power(self):
        return self.healing_power
    
    def special_ability(self):
        return print(f"Special abilities are: Heal")