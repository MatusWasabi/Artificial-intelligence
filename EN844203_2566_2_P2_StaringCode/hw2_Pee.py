
"""

Name: Potsawat Lalitlakkanakul /
Student ID: 633040222-7

Name: Atcharanan Chotveeraphat / 
Student ID: 

"""

import time
import random
import math
import numpy as np


WIN_SCORE = 100000000000000
LOSE_SCORE = -10000000000000

"""Places a piece on the board at the specified row and column."""
def drop_piece(board, row, col, piece):
    board[row][col] = piece

"""Checks if a given column is a valid location to drop a piece."""
def is_valid_location(board, col):
    return board[0][col] == 0

"""
Finds the next available row in the specified column.
Returns -1 if the column is full.
"""
def find_next_open_row(board, col):
    
    for r in range(len(board) - 1, -1, -1):
        if board[r][col] == 0:
            return r
    return -1

"""Checks if the specified piece has won the game."""
def check_winning_move(board, piece):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if c + 3 < len(board[0]) and board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
            if r + 3 < len(board) and board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
            if r + 3 < len(board) and c + 3 < len(board[0]) and board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
            if r - 3 >= 0 and c + 3 < len(board[0]) and board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
    return False

"""Evaluates the score of a window of pieces."""
def evaluate_window(window, piece):
    opponent_piece = 1 if piece == 2 else 2
    if window.count(piece) == 4:
        return 100
    elif window.count(piece) == 3 and window.count(0) == 1:
        return 5
    elif window.count(piece) == 2 and window.count(0) == 2:
        return 2
    elif window.count(opponent_piece) == 3 and window.count(0) == 1:
        return -4
    return 0

"""Scores the position of the board for the specified piece."""
def score_position(board, piece):
    score = 0
    for r in range(len(board)):
        for c in range(len(board[0])):
            if c + 3 < len(board[0]):
                score += evaluate_window(board[r][c:c+4], piece)
            if r + 3 < len(board):
                score += evaluate_window([board[i][c] for i in range(r, r+4)], piece)
            if r + 3 < len(board) and c + 3 < len(board[0]):
                score += evaluate_window([board[r+i][c+i] for i in range(4)], piece)
            if r - 3 >= 0 and c + 3 < len(board[0]):
                score += evaluate_window([board[r-i][c+i] for i in range(4)], piece)
    return score

"""Checks if the current board state is a terminal node."""
def is_terminal_node(board):
    return check_winning_move(board, 1) or check_winning_move(board, 2) or len(find_valid_locations(board)) == 0

"""Performs the Minimax algorithm with alpha-beta pruning."""
def minimax(board, depth, alpha, beta, maximizing_player):
    
    valid_locations = find_valid_locations(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if check_winning_move(board, 2):
                return (None, WIN_SCORE)
            elif check_winning_move(board, 1):
                return (None, LOSE_SCORE)
            else:
                return (None, 0)
        else:
            return (None, score_position(board, 2))
    if maximizing_player:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = find_next_open_row(board, col)
            b_copy = [row[:] for row in board]
            drop_piece(b_copy, row, col, 2)
            new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value
    else:
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = find_next_open_row(board, col)
            b_copy = [row[:] for row in board]
            drop_piece(b_copy, row, col, 1)
            new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value
    
"""Finds the valid locations to drop a piece on the board."""
def find_valid_locations(board):
    return [col for col in range(len(board[0])) if is_valid_location(board, col)]


time.sleep(2)
print("ready")

N,M,F,X,T = input("").strip().split(" ")
N = int(N)
M = int(M)
F = int(F)
T = float(T)
count_list = [0] * M
oppo_moves = [2, 3, 4, 3, 4, 1, 4, 2, 5, 2]

board = np.zeros((N, M))

if F == 0:
    oppo_move = int(input(""))
    row_drop = find_next_open_row(board, oppo_move)
    count_list[oppo_move] += 1    

while True:
    while True:
        my_move, minimax_score = minimax(board, 5, -math.inf, math.inf, True)
        if count_list[my_move] != N:
            row_drop = find_next_open_row(board, my_move)
            drop_piece(board, row_drop, my_move, 2)
            count_list[my_move] += 1
            print(my_move)
            break
    oppo_move = int(input(""))
    row_drop = find_next_open_row(board, oppo_move)
    drop_piece(board, row_drop, oppo_move, 1) 
    count_list[oppo_move] += 1