import tkinter as tk
from handledraw import Connect4Frontend
from board import Board
import ai

root = tk.Tk()
root.title("Connect 4")
app = Connect4Frontend(root)
root.mainloop()