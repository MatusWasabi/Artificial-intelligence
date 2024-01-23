import time
import random
from board import Board

time.sleep(2)
print("ready")

N,M,F,X,T = input("").strip().split(" ")
N = int(N)
M = int(M)
F = int(F)
T = float(T)
count_list = [0] * M

debug_board = Board(N, M)

if F == 0:
    oppo_move = int(input(""))
    count_list[oppo_move] +=1

while True:
    if T > 0.3:
        time.sleep(T-0.3)
    while True:
        my_move = random.randint(0,M-1)
        if count_list[my_move] != N:
            count_list[my_move] += 1
            print(my_move)
            #debug_board.DropPiece(my_move, "O")
            break
    oppo_move = int(input(""))
    #debug_board.DropPiece(oppo_move, "X")
    count_list[oppo_move] +=1
