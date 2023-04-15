from functions.to_int import to_int

class Street():
    def __init__(self, name, price, rent, house_price, color):
        self.name = name
        self.color = color
        self.price = to_int(price)
        self.rent = to_int(rent)
        self.house_count = 0
        self.house_price = to_int(house_price)
        self.owner = None
        self.mortgaged = False
    
    def rent(self, player):
        if self.mortgaged == True or self.owner == None or self.owner.jail == True:
            return 0
        
        streets_in_group = [street for street in self.owner.owned_streets if street.color == self.color]
        
        if len(streets_in_group) == 2 and self.color in ["Brown", "Dark-Blue"] and self.house_count == 0:
            rent = self.rent * 2
        elif len(streets_in_group) == 3 and self.color in ["Light-Blue", "Pink", "Orange", "Red", "Yellow", "Green"] and self.house_count == 0:
            rent = self.rent * 2
        else:
            if self.house_count == 0:
                rent = self.rent
            else:
                match self.house_count:
                    #TODO Needs fixing
                    case 1: rent = self.rent * 5
                    case 2: rent = self.rent * 15
                    case 3: rent = self.rent * 45
                    case 4: rent = self.rent * 80
                    case 5: rent = self.rent * 125
                    case _: rent = self.rent
        
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