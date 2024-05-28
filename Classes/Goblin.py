from Classes.Character import Character

class Goblin(Character):
    def __init__(self):
        super().__init__(health=50, speed=10, strength=3, defense=1, mana=10)
        self.currency = 0
        
    def castSleep(self):
        if self.mana < 5:
            return print("I don't have enough mana to cast that spell.")
        print("I cast a sleep spell!")
        self.mana -= 5
        return
    
    def pick_pocket(self, amountPickPocketed):
        self.currency += amountPickPocketed
        return self.currency
    
    def get_currency(self):
        return self.currency
    
    def special_ability(self):
        return print("Special abilities are: Pickpocket, and Cast Sleep")