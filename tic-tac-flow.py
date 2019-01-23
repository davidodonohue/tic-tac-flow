from tkinter import *
from PIL import Image, ImageTk

root = Tk()

blank = ImageTk.PhotoImage(Image.open("circle.png"))
#nought = "nought.jpg"
#cross = "cross.jpg"
cross = ImageTk.PhotoImage(Image.open("cross.png"))

board = [[' ',' ',' ',],
        [' ',' ',' ',],
        [' ',' ',' ']] # Remembers the state of the board

turn = 1 #whose turn it is

difficulty = 0 # difficulty of AI


def initialise():
    for row_num in range(3):
        ap = []
        for col_num in range(3):
            sq = Label(root, image=blank)
            #sq.image = blank
            sq.bind("<Button-1>", change)
            sq.grid(row=row_num, column = col_num)
            ap.append(sq)
        board.append(ap)

def change(event):
    print("Event!")
    sq = event.widget
    info = sq.grid_info()
    sq.destroy()
    sq = Label(root, image=cross)
    #sq.image = cross
    sq.grid(row=info["row"], column=info["column"])
    turn = 0
    board[info["row"]][info["column"]] = 'X'
    switch(1)

def check_win():
    

def switch(turn):
    check_win()
    if turn == 1:
        AI_move()

def AI_move()

initialise()
root.mainloop()
