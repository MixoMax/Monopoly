from functions.to_int import to_int
from classes.game import Game

class Player():
    def __init__(self, name, money):
        self.name = name
        self.money = to_int(money)
        self.position = 0
        self.owned_streets = []
        self.jail = False
        self.jail_turns = 0
        self.jail_card = False
        self.is_bankrupt = False
    
    def update_money(self, amount):
        self.money += amount
        if self.money < 0:
            self.is_bankrupt = True
    
    def can_afford(self, amount):
        return self.money >= amount
    
    def update_streets(self):
        self.owned_streets = [street for street in Game.streets if street.owner == self]
    
    def use_jail_card(self):
        #player can decide to use jail card
        player_choice = input("Do you want to use your get out of jail free card? (y/n): ")
        
        player_choice = player_choice.lower() == "y"
        
        if player_choice:
            self.jail_card = False
            self.jail = False
            self.jail_turns = 0
            return True
        else:
            return False