from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import copy

root = Tk()

blank = ImageTk.PhotoImage(Image.open("blank.png"))
cross = ImageTk.PhotoImage(Image.open("cross.png"))
nought = ImageTk.PhotoImage(Image.open("nought.png"))

board = [[' ',' ',' ',],
        [' ',' ',' ',],
        [' ',' ',' ']]
dict = {}

players = ['X', 'O']

difficulty = 0


def initialise():
    for row_num in range(3):
        for col_num in range(3):
            sq = Label(root, image=blank)
            #sq.image = blank
            sq.bind("<Button-1>", change)
            sq.grid(row=row_num, column = col_num)
            dict[(row_num,col_num)] = sq
            global board
            board = [[' ',' ',' ',],
                    [' ',' ',' ',],
                    [' ',' ',' ']]

def change(event):
    sq = event.widget
    info = sq.grid_info()
    sq.destroy()
    sq = Label(root, image=cross)
    #sq.image = cross
    sq.grid(row=info["row"], column=info["column"])
    board[info["row"]][info["column"]] = 'X'
    finish_play()

def check_win():
    for row in board:
        if all(item == 'X' for item in row):
            print("One")
            return 'X'
        elif all (item == 'O' for item in row):
            print("Two")
            return 'O'
    for column in range(3):
        if all(row[column] =='X' for row in board):
            print("Three")
            return 'X'
        elif all(row[column] =='O' for row in board):
            print("Four")
            return 'O'
    middle = board[1][1]
    if middle != ' ':
        if middle == board[0][0] and middle == board[2][2] or middle == board[0][2] and middle == board[2][0]:
            print("Five")
            return middle
    return ' '

def get_moves(b):
    empty = []
    for row in range(3):
        for column in range(3):
            if b[row][column] == ' ':
                empty.append((row, column))
    return empty

def finish_play():
    state = check_win()
    if state == ' ':
        move = AI_move(board)
        sq = dict[move]
        info = sq.grid_info()
        sq.destroy()
        sq = Label(root, image=nought)
        #sq.image = nought
        sq.grid(row=info["row"], column=info["column"])
        board[info["row"]][info["column"]] = 'O'
    else:
        reset_game(state)

def reset_game(winner):
    if winner == 'X':
        messagebox.showwarning("Congratulations!", "You win!")
    else:
        messagebox.showinfo("Comiserations!","Better luck next time!")
    for child in root.winfo_children():
        child.destroy()
    initialise()

def get_children(b, player, moves):
    rtn = []
    for move in moves:
        b_cp = copy.deepcopy(b)
        b_cp[move[0]][move[1]] = players[player]
        rtn.append((move, b_cp))
    return rtn
        
    
def AI_move(b):
    possible_moves = get_moves(b)
    possible_boards = get_children(b, 1, possible_moves)
    draw = possible_moves[0]
    for (move, bd) in possible_boards:
        result = minimax(bd, 0)
        if result == -1:
            return move
        elif result == 0:
            draw = move
    return draw    #always return

def minimax(b, player):
    state = check_win()
    if state == players[(player + 1) %2]:
        return (-1)
    elif state == players[player]:
        return 1
    else:
        possible_moves = get_moves(b)
        if possible_moves == []:
            return 0
        possible_boards = get_children(b,player,possible_moves)
        for (move, bd) in possible_boards:
            opponent_wins = minimax(bd,(player + 1) % 2)
            if opponent_wins == -1:
                return 1
        return 0

initialise()
root.mainloop()
