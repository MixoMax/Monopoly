import pygame as pg

# Monopoly game in python

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
        self

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


