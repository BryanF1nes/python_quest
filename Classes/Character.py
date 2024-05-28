class Character:
    def __init__(self, health, speed, strength, defense, mana):
        self.health = health
        self.speed = speed
        self.strength = strength
        self.defense = defense
        self.mana = mana
        self.level = 1
        self.maxLevel = 20
        
    def getHealth(self):
        return self.health
    
    def getStrength(self):
        return self.strength
    
    def getSpeed(self):
        return self.speed
    
    def getDefense(self):
        return self.defense
    
    def getMana(self):
        return self.mana
    
    def getLevel(self):
        return self.level
    
    def levelUp(self):
        if self.level != self.maxLevel:
            self.level += 1
            self.strength += 1
            self.health += 10
            self.speed += 1
            self.defense += 2
            self.mana += 10
        return print(f"{self.maxLevel} has been reached. You can not level up anymore.")
    
    def special_ability(self):
        pass