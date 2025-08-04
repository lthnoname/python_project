import random
import math

class Player:
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter

    def move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            Square = input(self.letter + "\'s turn. Input move (0 - 9): ")
            try:
                val = int(Square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again")
        
        return val