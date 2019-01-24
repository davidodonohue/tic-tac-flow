from tkinter import *
from PIL import Image, ImageTk

root = Tk()

blank = ImageTk.PhotoImage(Image.open("circle.png"))
#nought = "nought.jpg"
#cross = "cross.jpg"
cross = ImageTk.PhotoImage(Image.open("cross.png"))

board = [[' ',' ',' ',],
        [' ',' ',' ',],
        [' ',' ',' ']]

turn = 1

difficulty = 0


def initialise():
    for row_num in range(3):
        for col_num in range(3):
            sq = Label(root, image=blank)
            #sq.image = blank
            sq.bind("<Button-1>", change)
            sq.grid(row=row_num, column = col_num)

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
    for row in board:
        if all(item == 'X' for item in row):
            return 'X'
        elif all (item == 'O' for item in row):
            return 'O'
    for column in range(3):
        if all(row[column] =='X' for row in board):
            return 'X'
        elif all(row[column] =='O' for row in board):
            return 'O'
    middle = board[1][1]
    if middle == board[0][0] and middle == board[2][2] or middle == board[0][2] and middle == board[2][0]:
        return middle
    return ' '

def switch(turn):
    state = check_win()
    if state == ' ':
        if turn == 1:
            AI_move(board)
    elif state == 'X':
    
    elif state == 'O':
    

def AI_move(state)

initialise()
root.mainloop()
