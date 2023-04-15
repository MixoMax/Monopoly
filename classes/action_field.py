from classes.player import Player
from classes.dice import Dice

class Chance_card():
    def __init__(self, name, action):
        self.name = name
        self.action = action


class Station():
    def __init__(self, name, price, rent_mult = 25, owner=None):
        self.name = name
        self.price = price
        self.rent_mult = rent_mult
        self.owner = owner
        self.mortgaged = False
    
    def rent(self, player):
        self.rent_mult = 25 * len([street for street in self.owner.streets if isinstance(street, Station)])
        rent = self.rent_mult
        
        player.update_money(-rent)
        self.owner.update_money(rent)
    
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
    
    def mortgage(self):
        self.mortgaged = True
        self.owner.update_money(self.price // 2)
        return True
    
    def unmortgage(self):
        unmortgage_price = int(self.price * 1.1) // 2
        if self.owner.can_afford(unmortgage_price):
            self.owner.update_money(-unmortgage_price)
            self.mortgaged = False
            return True
        else:
            return False



class Utility():
    def __init__(self, name, price, rent_mult = 4, owner=None):
        self.name = name
        self.price = price
        self.rent_mult = rent_mult
        self.owner = owner
        self.mortgaged = False
    
    def rent(self, player):
        dice_roll = Dice(6).roll_sum()
        
        rent = dice_roll * self.rent_mult
        
        player.update_money(-rent)
        self.owner.update_money(rent)
    
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
    
    def mortgage(self):
        self.mortgaged = True
        self.owner.update_money(self.price // 2)
        return True
    
    def unmortgage(self):
        unmortgage_price = int(self.price * 1.1) // 2
        if self.owner.can_afford(unmortgage_price):
            self.owner.update_money(-unmortgage_price)
            self.mortgaged = False
            return True
        else:
            return False