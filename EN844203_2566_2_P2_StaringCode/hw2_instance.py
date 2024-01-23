import random
from board import Board

print("ready")

# Debug input
num_rows = 6
num_col = 7
num_win_piece = 4
first_player = 1
time_limit = 0.2

#num_rows,num_col,first_player,num_win_piece,time_limit = input("").strip().split(" ")
num_rows = int(num_rows)
num_col = int(num_col)
first_player = int(first_player)
time_limit = float(time_limit)
count_list = [0] * num_col

debug_board = Board(num_rows, num_col)


if first_player == 0:
    oppo_move = int(input(""))
    debug_board.DropPiece(oppo_move, "X")
    count_list[oppo_move] +=1

while True:
    while True:
        my_move = random.randint(0,num_col-1)
        if count_list[my_move] != num_rows:
            count_list[my_move] += 1
            print(my_move)
            debug_board.DropPiece(my_move, "O")
            break
    oppo_move = int(input(""))
    debug_board.DropPiece(oppo_move, "X")
    count_list[oppo_move] +=1


