import pygame as pg
import random
from classes.game import Game
from classes.player import Player
from functions.csv_to_streets import csv_to_streets

# Monopoly game in python

# TODO:
# - implement chance and community chest cards
# - implement trading
# - fix rent calculation for houses and hotels
# - implement bankruptcy
# - implement user interface / prompting

global streets  

def startup():
    board = input("What board do you want to play on?\n\n[Q] Exit\n\n[1] Default\n[2] Hamburg\n\nAnswer: ")
    match board:
        case "1":
            streets = csv_to_streets()
        case "2":
            streets = csv_to_streets("./data/hamburg.csv")
        case _:
            print("Invalid input")
            startup()
    
    for street in streets:
        print(street)


players = [Player("Player 1", 1500), Player("Player 2", 1500), Player("Player 3", 1500), Player("Player 4", 1500)]

if __name__ == "__main__":
    startup()