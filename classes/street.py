from functions.to_int import to_int

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