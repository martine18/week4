#tic tac toe // ideas come from help of google and youtube

import random

def display_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Player 1: Choose X or O: ").upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[0] == mark and board[1] == mark and board[2] == mark) or
    (board[3] == mark and board[4] == mark and board[5] == mark) or
    (board[6] == mark and board[7] == mark and board[8] == mark) or
    (board[0] == mark and board[3] == mark and board[6] == mark) or
    (board[1] == mark and board[4] == mark and board[7] == mark) or
    (board[2] == mark and board[5] == mark and board[8] == mark) or
    (board[0] == mark and board[4] == mark and board[8] == mark) or
    (board[2] == mark and board[4] == mark and board[6] == mark))

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(0,9):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [0,1,2,3,4,5,6,7,8] or not space_check(board, position):
        position = int(input("Choose a position from 0-8: "))
    return position

def replay():
    choice = input("Play again? Enter Yes or No: ")
    return choice == 'Yes'

print("Welcome to Tic Tac Toe")
while True:

