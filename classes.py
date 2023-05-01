class Player():
    def __init__(self, name, money=1500):
        self.name = name
        self.money = money	
        
        self.position = 0
        self.is_in_jail = False
        self.jail_card_counter = 0
        self.jail_turn_counter = 0
    
    def has_jail_card(self):
        return self.jail_card_counter > 0
    
    def buy_street(self, street):
        street_price = street.price
        if self.money >= street_price:
            self.money -= street_price
            street.owner = self
            return True
        else:
            return False
    
    def pay_player(self, player, amount):
        if self.money >= amount:
            self.money -= amount
            player.money += amount
            return True
        else:
            return False
    
    def buy_house(self, street):
        house_price = street.house_price
        if self.money >= house_price:
            self.money -= house_price
            street.houses += 1
            return True
        else:
            return False
        
    def move(self, amount):
        self.position += amount
        if self.position >= 28:
            self.position -= 28
            self.money += 200



class Street():
    def __init__(self, name, price, rent, house_price, color):
        self.name = name
        self.price = price
        self.rent = rent
        self.house_price = house_price
        self.color = color
        self.owner = None
        self.houses = 0
        self.is_mortgaged = False
    
    def __str__(self):
        return self.name
    
    def get_rent(self):
        return self.rent * (2 ** self.houses)
    
    def set_mortgage(self, is_mortgaged):
        self.is_mortgaged = is_mortgaged
        if is_mortgaged:
            self.owner.money += self.price / 2
            return True
        else:
            if self.owner.money >= self.price * 0.6:
                self.owner.money -= self.price * 0.6
                return True
            else:
                return False