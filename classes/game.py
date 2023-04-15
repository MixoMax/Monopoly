from classes.dice import Dice
from classes.board import Board

class Game():
    def __init__(self, players, streets):
        self.players = players
        self.player_count = len(players)
        self.streets = streets
        self.board = Board(streets)
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
        else:
            self._normal_move(player)
    
    def _normal_move(self, player):
        board_pos = player.position
        if self.board.fields[board_pos].owner != player:
            self.board.fields[board_pos].rent(player)
        else:
            if self.board.fields[board_pos].owner == None:
                self.board.fields[board_pos].new_owner(player)
            else:
                self.board.fields[board_pos].action(player)
        
        
        
    
    def _turn_jail(self):
        player = self.players[self.current_player]
        player.jail_turns += 1
        if player.jail_turns == 3:
            if player.can_afford(50):
                player.update_money(-50)
                player.jail = False
                player.jail_turns = 0
                return True
            else:
                player.is_bankrupt = True
        
        if player.jail_card == True:
            # player can use card to get out of jail
            player.jail_card = False
            player.jail = False
            player.jail_turns = 0
            return True
        
        for _ in range(3):
            dice_roll = self.dice.roll()
            if dice_roll[0] == dice_roll[1]:
                player.jail = False
                player.jail_turns = 0
                return True
        return False
        
        