from board import Board
from copy import deepcopy

class AI:
    def __init__(self, player):
        self.ownboard = deepcopy(Board())
        self.player = player



    def move(self):
        points = 0
        most_optimal = 1
        for i in range(7):
            self.ownboard.Input(i, self.player)
            self.ownboard.four_in_a_row()
            self.ownboard.board = self.ownboard.prev_board
            if self.ownboard.LargestStreak() > points:
                most_optimal = i+1
                points = self.ownboard.LargestStreak()
                self.ownboard.reset_ai_streaks()
                
            if self.ownboard.IsFull():
                points = 0

        print(points)
        return most_optimal
