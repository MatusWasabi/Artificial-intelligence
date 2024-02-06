import random
import numpy as np
import math


"""
Name: Matus Yaowvasrisuwan
ID: 633040476 - 6

Name: Nunnapat Srithong
"""

print("ready")

ROWS,COLS,F,WIN_NUM,T = input("").strip().split(" ")
ROWS = int(ROWS)
COLS = int(COLS)
WIN_NUM = int(WIN_NUM)
F = int(F)
T = float(T)
count_list = [0] * COLS 
board = np.zeros((ROWS, COLS))

PLAYER_PIECE = 1
AI_PIECE = 2


# TODO Integrate Minimax from connect 4


def minimax(board, depth, alpha, beta, maximizing_player):

    valid_locations = get_valid_locations(board)

    is_terminal = is_terminal_node(board)


    if depth == 0 or is_terminal:
        if is_terminal: 
            if winning_move(board, AI_PIECE):
                return (None, 10000000)
            elif winning_move(board, PLAYER_PIECE):
                return (None, -10000000)
            else:
                return (None, 0)
        else: 
            return (None, score_position(board, AI_PIECE))

    if maximizing_player:

        value = -math.inf

        column = random.choice(valid_locations)


        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, AI_PIECE)
            new_score = minimax(b_copy, depth - 1, alpha, beta, False)[1]

            if new_score > value:
                value = new_score
                column = col

            alpha = max(value, alpha) 

            if alpha >= beta:
                break

        return column, value
    
    else: 
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, PLAYER_PIECE)
            new_score = minimax(b_copy, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(value, beta) 
            if alpha >= beta:
                break
        return column, value

def get_valid_locations(board):
    valid_locations = []

    def is_valid_location(board, col):
        return board[0][col] == 0

    
    for column in range(COLS):
        if is_valid_location(board, column):
            valid_locations.append(column)

    return valid_locations

def is_terminal_node(board):
    return winning_move(board, PLAYER_PIECE) or winning_move(board, AI_PIECE) or len(get_valid_locations(board)) == 0

# DONE Can win with more piece rather than 4
def winning_move(board, piece):
    # checking horizontal 'windows' of 4 for win
    for c in range(COLS - (WIN_NUM - 1)):
        for r in range(ROWS):
            for i in range(WIN_NUM):
                if board[r][c + i] != piece:
                    return False
                
            return True
            
    # checking vertical 'windows' of 4 for win
    for c in range(COLS):
        for r in range(ROWS - (WIN_NUM - 1)):
            for i in range(WIN_NUM):

                if board[r + i][c] != piece:
                        return False
                    
                return True

    # checking positively sloped diagonals for win
    for c in range(COLS - (WIN_NUM - 1)):
        for r in range((WIN_NUM - 1), ROWS):
            for i in range(WIN_NUM):

                if board[r - i][c + i] != piece:
                        return False
                    
                return True

    # checking negatively sloped diagonals for win
    for c in range((WIN_NUM - 1), COLS):
        for r in range((WIN_NUM - 1), ROWS):
            for i in range(WIN_NUM):

                if board[r - i][c - i] != piece:
                        return False
                return True

# TODO Rework of score evaluation
def score_position(board, piece):

    def evaluate_window(window, piece):
        # by default the oponent is the player
        opponent_piece = PLAYER_PIECE

        # if we are checking from the player's perspective, then the oponent is AI
        if piece == PLAYER_PIECE:
            opponent_piece = AI_PIECE

        # initial score of a window is 0
        score = 0

        # based on how many friendly pieces there are in the window, we increase the score
        if window.count(piece) == WIN_NUM:
            score += math.fabs(window.count(piece))

        else:
            hueristic = (window.count(piece) - window.count(0)) + 2 # I want it to start from 1 and go for 2, 3, 5, 8 and so on.
            score += math.fabs(hueristic)


        # or decrese it if the oponent has X-1 in a row
        if window.count(opponent_piece) == (WIN_NUM - 1) and window.count(0) == 1:
            score -= math.fabs(window.count(opponent_piece)) 

        return score    


    score = 0

    # score center column --> we are prioritizing the central column because it provides more potential winning windows
    center_array = [int(i) for i in list(board[COLS//2])]
    center_count = center_array.count(piece)
    score += (math.fabs(center_count))

    # below we go over every single window in different directions and adding up their values to the score
    # score horizontal
    for r in range(ROWS):
        row_array = [int(i) for i in list(board[r,:])]
        for c in range(COLS - (WIN_NUM - 1)):
            window = row_array[c:c + WIN_NUM]
            score += evaluate_window(window, piece)

    # score vertical
    for c in range(COLS):
        col_array = [int(i) for i in list(board[:,c])]
        for r in range(ROWS - (WIN_NUM - 1)):
            window = col_array[r:r + WIN_NUM]
            score += evaluate_window(window, piece)

    # score positively sloped diagonals
    for r in range((WIN_NUM - 1), ROWS):
        for c in range(COLS - (WIN_NUM - 1)):
            window = [board[r - i][c + i] for i in range(WIN_NUM)]
            score += evaluate_window(window, piece)

    # score negatively sloped diagonals
    for r in range((WIN_NUM - 1), ROWS):
        for c in range((WIN_NUM - 1), COLS):
            window = [board[r-i][c-i] for i in range(WIN_NUM)]
            score += evaluate_window(window, piece)

    return score

def get_next_open_row(board, col):
    for r in range(ROWS - 1, -1, -1):
        if board[r][col] == 0:
            return r

def drop_piece(board, row, col, piece):
    board[row][col] = piece



# Testing Unit. DONE
if F == 0:
    oppo_move = int(input(""))
    board[ROWS - 1 - count_list[oppo_move]][oppo_move] = PLAYER_PIECE
    count_list[oppo_move] +=1
	

while True:
    while True:
        my_move, minimax_score = minimax(board, 5, -math.inf, math.inf, True)
        if count_list[my_move] != ROWS:
            board[ROWS - 1 - count_list[my_move]][my_move] = AI_PIECE
            count_list[my_move] += 1
            print(my_move)
            break

    oppo_move = int(input(""))
    board[ROWS - 1 - count_list[oppo_move]][oppo_move] = PLAYER_PIECE
    count_list[oppo_move] +=1
	


