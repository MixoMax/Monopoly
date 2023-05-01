from functions.functions import *
from classes import Player, Street
import random

players = [Player("Player 1"), Player("Player 2")]

streets = csv_to_streets()


# main game loop

print(len(streets))

while True:
    #player 1 move
    player = players[0]
    
    dice = (random.randint(1, 6), random.randint(1, 6))
    
    player.move(sum(dice))
    
    street = streets[player.position]
    
    if street.owner != player and street.owner != None:
        player.pay_player(street.owner, street.get_rent())
    elif street.owner == None:
        decision = input(f"Would you like to buy {street.name} for {street.price}? (y/n)")
        if decision in ["y", "yes"]:
            player.buy_street(street)