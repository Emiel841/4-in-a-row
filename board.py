class Board():

    def __init__(self):
        self.rows, self.cols = (6, 7)
        self.board = [[0 for i in range(self.cols)] for j in range(self.rows)]
        self.streaks = [0, 0]
        self.rowstreaks = [0, 0]
        self.colstreaks = [0, 0]
        self.diastreakstop = [0, 0]
        self.diastreaksbot = [0, 0]
        self.prev_board = [[0 for i in range(self.cols)] for j in range(self.rows)]



    def Input(self, target, player):
        target -= 1
        row = 5
        self.prev_board = self.board

        for i in range(self.rows):
            if self.board[i][target] != 0:
                row -= 1

        if row == -1:
            return True
        self.board[row][target] = player

    def four_in_a_row(self):
        if self.diagonal_check():
            return True
        if self.row_check():
            return True
        if self.col_check():
            return True

    def row_check(self):
        for i in range(self.rows):
            self.streaks = [0, 0]
            prev = 0
            for point in self.board[i]:
                if point!= 0:
                    if point == prev:
                        self.streaks[point-1] += 1
                        self.set_row_streak(self.streaks[point-1], point-1)
                        if self.streaks[0] == 3:
                            return True
                        if self.streaks[1] == 3:
                            return True
                    else:
                        self.streaks = [0, 0]

                prev = point
        return False

    def diagonal_check(self):
        for x in range(self.rows - 3):
            for y in range(3, self.cols):
                if self.board[x][y] != 0:
                    chip = self.board[x][y]
                    if self.board[x][y] == chip and self.board[x + 1][y - 1] == chip and self.board[x + 2][y - 2] == chip and self.board[x + 3][y - 3] == chip:
                        return  True

        for x in range(self.rows - 3):
            for y in range(self.cols-3):
                if self.board[x][y] != 0:
                    chip = self.board[x][y]
                    if self.board[x][y] == chip and self.board[x + 1][y + 1] == chip and self.board[x + 2][y + 2] == chip and self.board[x + 3][y + 3] == chip:
                        return  True

    def col_check(self):
        for i in range(self.cols):
            self.streaks = [0, 0]
            prev = 0
            for row in self.board:
                if row[i] != 0:
                    if row[i] == prev:
                        self.streaks[row[i]-1] += 1
                        self.set_col_streak(self.streaks[row[i]-1], row[i]-1)
                        if self.streaks[row[i]-1] == 3:
                            return True
                    else:
                        self.streaks = [0, 0]


                prev = row[i]

        return False

    def Reset(self):
        self.board = [[0 for i in range(self.cols)] for j in range(self.rows)]
        self.reset_streaks()

    def Print(self):
        for i in range(self.rows):
            print(self.board[i])
        print("\n")

    def IsFull(self):
        notfull = False
        for i in range(len(self.board)):
            for j in self.board[i]:
                if j == 0:
                    notfull = True
                    return False
        if not notfull:
            return True

    def set_row_streak(self, value, pos):
        if self.rowstreaks[pos] <= value:
            self.rowstreaks[pos] = value
    def set_col_streak(self, value, pos):
        if self.colstreaks[pos] <= value:
            self.colstreaks[pos] = value
    def set_dia_streak_top(self):
        pass
    def set_dia_streak_bot(self):
        pass
    def reset_streaks(self):
        self.colstreaks = [0, 0]
        self.rowstreaks = [0, 0]
        self.diastreaksbot = [0, 0]
        self.diastreakstop = [0, 0]

    def reset_ai_streaks(self):
        self.rowstreaks[1] = 0
        self.colstreaks[1] = 0
        self.diastreakstop[1] = 0
        self.diastreaksbot[1] = 0

    def LargestStreak(self):
        streaks = []
        streaks.append(self.rowstreaks[1])
        streaks.append(self.colstreaks[1])
        streaks.append(self.diastreaksbot[1])
        streaks.append(self.diastreakstop[1])
        return max(streaks)
