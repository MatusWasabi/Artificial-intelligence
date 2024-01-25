import random
from connect4_with_AI import get_valid_locations, is_terminal_node, winning_move
from connect4_with_AI import score_position, get_next_open_row, drop_piece
import math

print("ready")


num_rows,num_col,first_player,num_win_piece,time_limit = input("").strip().split(" ")
num_rows = int(num_rows)
num_col = int(num_col)
first_player = int(first_player)
time_limit = float(time_limit)
count_list = [0] * num_col # Number of time dropping in that column


PLAYER_PIECE = 0
AI_PIECE = 1


# Create Board
board = [[None] * num_col for _ in range(num_rows)]

def minimax(board: list[list], depth, alpha, beta, maximizing_player):

    valid_locations = get_valid_locations(board)

    is_terminal = is_terminal_node(board)

    """if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, AI_PIECE):
                # It was none but change it to 0 for debugging
                return (0, 1000000)
            elif winning_move(board, PLAYER_PIECE):
                return (0, -1000000)
            else:
                return (0, 0)
            
        else:
            return (None, score_position(board, AI_PIECE))"""
        
    if maximizing_player:

        value = -math.inf

        column = random.randint(0, num_col - 1)

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
        column = random.randint(0, num_col - 1)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, PLAYER_PIECE)
            new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(value, beta) 
            if alpha >= beta:
                break
        return column, value



# first player = 0 means this code won't be the first to move: AKA false
if first_player == 0:
    oppo_move = int(input(""))
    count_list[oppo_move] +=1

# First player = 1 means this code will be the first to move 
# Oppo will be set as 1 and our code will be so call 0:
# This code will be maximizer and opponent will minimizer

while True:
    while True:
        my_move, minimax_score = minimax(board, 5, -math.inf, math.inf, True)

        if my_move == None:
            break

        if count_list[my_move] != num_rows:
            count_list[my_move] += 1
            print(my_move)
            break

        
        
    oppo_move = int(input(""))
    count_list[oppo_move] +=1

#TODO Problem is the terminal won't print anything out 