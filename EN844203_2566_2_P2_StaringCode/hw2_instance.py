import random
from connect4_with_AI import get_valid_locations, is_terminal_node, winning_move
from connect4_with_AI import score_position, get_next_open_row, drop_piece, create_board, minimax
import math
import numpy as np

print("ready")


#num_rows,num_col,num_win_piece,first_player,time_limit = input("").strip().split(" ")
num_rows = 6#int(num_rows)
num_col = 7#int(num_col)
first_player = 1#int(first_player)
time_limit = 2#float(time_limit)
count_list = [0] * num_col # Number of time dropping in that column


PLAYER_PIECE = 1
AI_PIECE = 2

# Create the board
# Drop piece
# Update the board 

board = create_board(num_rows, num_col)

if first_player == 0:
    print("Oppo Move")
    oppo_move = int(input(""))
    row_drop = get_next_open_row(board, oppo_move)
    board[row_drop][oppo_move] = PLAYER_PIECE

    count_list[oppo_move] +=1    

    print(board)

while True:
    while True:
        print("My move")
        my_move, minimax_score = minimax(board, 5, math.inf, -math.inf, True)
        row_drop = get_next_open_row(board, my_move)
        board[row_drop][my_move] = AI_PIECE
        print(board)

        if my_move == None:
            break

        if count_list[my_move] != num_rows:
            count_list[my_move] += 1
            print(my_move)
            
            break
        
    print("Oppo Move")
    oppo_move = int(input(""))
    row_drop = get_next_open_row(board, oppo_move)
    board[row_drop][oppo_move] = PLAYER_PIECE
    print(board)

    count_list[oppo_move] +=1

