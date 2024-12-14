from board import Board
import tkinter as tk
from time import sleep
import ai

class Connect4Frontend:
    def __init__(self, root, rows=6, cols=7):
        self.board = Board()
        self.ai = ai.AI(2)
        self.end = False
        self.two_player = True
        self.root = root
        self.rows = rows
        self.cols = cols
        self.cell_size = 80
        self.canvas_width = self.cols * self.cell_size
        self.canvas_height = self.rows * self.cell_size
        self.player = True

        # Create canvas
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg='blue')
        self.canvas.pack()

        self.win_label = tk.Label(root, text="", font=("Arial", 16), fg="green")
        self.win_label.pack()

        # Draw grid
        self.draw_grid()
        self.canvas.bind("<Button-1>", self.handle_click)

    def draw_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                self.canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill='white', tags=f'cell_{row}_{col}')

    def handle_click(self, event):
        if not self.end:
            col =  event.x // self.cell_size
            col += 1

            if self.two_player:
                if self.player:
                    if self.board.Input(col, 1):
                        self.player = not self.player
                elif not self.player:
                    if self.board.Input(col, 2):
                        self.player = not self.player
                self.draw_board_state(self.board.board)
                if self.board.four_in_a_row():
                    if self.player:
                        self.display_winner(1)
                    if not self.player:
                        self.display_winner(2)

                if self.board.IsFull():
                    self.display_winner(3)
            else:
                self.player = True
                if self.board.Input(col, 1): self.player = True

                self.draw_board_state(self.board.board)
                if self.board.four_in_a_row():
                    self.display_winner(1)
                if self.board.IsFull():
                    self.display_winner(3)

                move = self.ai.move()
                self.board.Input(move, 2)

                self.draw_board_state(self.board.board)
                if self.board.four_in_a_row():
                    self.display_winner(2)
                if self.board.IsFull():
                    self.display_winner(3)





            self.player = not self.player
        else:
            self.reset_game()
            self.end = False
            self.board.Reset()

    def draw_board_state(self, board):
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 1:
                    self.draw_piece(row, col, "red")
                elif board[row][col] == 2:
                    self.draw_piece(row, col, "yellow")

    def draw_piece(self, row, col, color):
        x1 = col * self.cell_size
        y1 = row * self.cell_size
        x2 = x1 + self.cell_size
        y2 = y1 + self.cell_size
        self.canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill=color)

    def display_winner(self, player):
        if self.two_player:
            if player == 1:
                self.win_label.config(text="Player 1 Wins!")
            elif player == 2:
                self.win_label.config(text="Player 2 Wins!")
            elif player == 3:
                self.win_label.config(text="You both lost L")
        self.end = True

    def reset_game(self):
        self.canvas.delete("all")
        self.draw_grid()
        self.win_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Connect 4")
    app = Connect4Frontend(root)
    root.mainloop()