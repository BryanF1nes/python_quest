from Classes.Character import Character

class Warrior(Character):
    def __init__(self):
        super().__init__(health=150, speed=4, strength=5, defense=7, mana=10)
        self.stamina = 10
        
    def shield_bash(self):
        if self.stamina < 2:
            return print("I can't use that my stamina is too low.")
        print("Charging!!")
        self.stamina -= 2
        return print("Bashes shield into the enemy!")
    
    def get_stamina(self):
        return self.stamina
    
    def special_ability(self):
        return print("Special abilities are: Shield bash")