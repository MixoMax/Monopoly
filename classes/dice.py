import random

class Dice():
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll(self, num_roles=1):
        rolls = []
        for _ in range(num_roles):
            rolls.append(random.randint(1, self.sides))
        return rolls

    def roll_sum(self, num_roles=1):
        return sum(self.roll(num_roles))