import random
import os
import time

ROWS = 50
COLS = 50
board = []

def print_board(board):
    os.system('cls')
    for rows in board:
        for col in rows:
            print(str(col)+' ', end='')
        print('')
def game_step():
    board_copy = [row[:] for row in board]
    for row in range(ROWS):
        for col in range(COLS):
            neighbours = return_neighbours(row,col, board_copy)
            dead = neighbours.count('.')
            alive = neighbours.count('O')
            update_state(row,col,dead,alive)
            
def update_state(row,col,dead,alive):
    is_dead = board[row][col] == '.'
    if (is_dead):
        if alive == 3:
            board[row][col] = 'O'
    else: 
        if alive == 2 or alive == 3:
            return
        if alive < 2 or alive > 3:
            board[row][col] = '.'



def return_neighbours(row,col, board_cp):
    neighbours = []
    for x in range(row-1, row+2):
        for y in range(col-1, col+2):
            if x == row and y == col:
                continue
            if x >= 0 and x < ROWS and y >= 0 and y < COLS:
                neighbours.append(board_cp[x][y]) 
    return neighbours

for i in range(0, ROWS):
    board.append([])
    for j in range (0, COLS):
        state = random.choice(['.', 'O'])
        board[i].append(state)

while(True):
    print_board(board)
    game_step()

    time.sleep(1)
