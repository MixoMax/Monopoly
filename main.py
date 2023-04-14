import pygame as pg
import random

# Monopoly game in python

global streets

def to_int(s):
    try:
        return int(s)
    except ValueError:
        int_str =""
        for char in str(s):
            if char == ".":
                break
            int_str += str(char)
        
        return int(int_str)
            

class Player():
    def __init__(self, name, money):
        self.name = name
        self.money = to_int(money)
        self.position = 0
        self.owned_streets = []
        self.jail = False
        self.jail_turns = 0
        self.jail_card = False
    
    def update_money(self, amount):
        self.money += amount
    
    def can_afford(self, amount):
        return self.money >= amount
    
    def update_streets(self):
        self.owned_streets = [street for street in streets if street.owner == self]



class Street():
    def __init__(self, name, price, rent, house_price):
        self.name = name
        self.price = to_int(price)
        self.rent = to_int(rent)
        self.house_count = 0
        self.house_price = to_int(house_price)
        self.owner = None
        self.mortgaged = False
    
    def __str__(self):
        return str(self.name)
    
    def new_owner(self, player):
        if self.owner != None:
            self.owner.update_streets()
        if player.can_afford(self.price):
            self.owner = player
            self.owner.update_streets()
            self.owner.update_money(-self.price)
            return True
        else:
            return False
    
    def mortage(self):
        self.mortgaged = True
        self.owner.update_money(self.price // 2)
        return True
    
    def unmortage(self):
        umortage_price = int(self.price * 1.1) // 2
        if self.owner.can_afford(umortage_price):
            self.owner.update_money(-umortage_price)
            self.mortgaged = False
            return True
        else:
            return False
    


class Dice():
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll(self, num_rols=1):
        rolls = []
        for i in range(num_rols):
            rolls.append(random.randint(1, self.sides))
        return rolls

    def roll_sum(self, num_rols=1):
        return sum(self.roll(num_rols))



class Game():
    def __init__(self, players, streets):
        self.players = players
        self.player_count = len(players)
        self.streets = streets
        self.dice = Dice(6)
        self.current_player = 0
        self.doubles = {} # {player: num_doubles}
        for player in self.players:
            self.doubles[player] = 0
    
    def next_player(self):
        self.current_player = (self.current_player + 1) % self.player_count
    
    def current_move(self):
        player = self.players[self.current_player]
        if player.jail == True:
            self._jail_move(player)
    
    def _turn_jail(self):
        player = self.players[self.current_player]
        player.jail_turns += 1
        if player.jail_turns == 3:
            if player.can_afford(50):
                player.update_money(-50)
                player.jail = False
                player.jail_turns = 0
                return True
        
        if player.jail_card == True:
            
        
                

def csv_to_streets(file_path = "./data/streets.csv"):
    streets = []
    with open(file_path, "r") as f:
        f = f.readlines()
        for line in f:
            line = line.split(",")
            if line[0] == "name":
                continue
            streets.append(Street(line[0], line[1], line[2], line[3]))
    return streets

streets = csv_to_streets()


players = [Player("Player 1", 1500), Player("Player 2", 1500), Player("Player 3", 1500), Player("Player 4", 1500)]

