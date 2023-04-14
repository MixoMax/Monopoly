from classes.dice import Dice

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
            # player can use card to get out of jail
            pass