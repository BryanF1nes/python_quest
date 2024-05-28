from Classes.Character import Character

class Elf(Character):
    def __init__(self):
        super().__init__(health=70, speed=12, strength=2, defense=5, mana=10)
        self.range = 5
        self.arrows = 10
        
    def shoot(self, targetDistance):
        if targetDistance > self.range:
            return print(f"Target is out of range...")
        if self.arrows <= 0:
            return print(f"Out of arrows..")
        self.arrows -= 1
        return print(f"shoots arrow")
    
    def get_arrows(self):
        return self.arrows
    
    def special_ability(self):
        return print("Special abilities are: Shoot")