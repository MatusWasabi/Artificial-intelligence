import random
import numpy as np
import math
from connect4_with_AI import minimax

print("ready")
N,M,F,X,T = input("").strip().split(" ")
N = int(N)
M = int(M)
F = int(F)
T = float(T)
count_list = [0] * M 
board = np.zeros((N, M))

if F == 0:
    oppo_move = int(input(""))

    board[N - 1 - count_list[oppo_move]][oppo_move] = 1
    count_list[oppo_move] +=1
	

while True:
    while True:
        my_move, minimax_score = minimax(board, 5, -math.inf, math.inf, True)
        if count_list[my_move] != N:
            board[N - 1 - count_list[my_move]][my_move] = 2
            count_list[my_move] += 1
            print(my_move)
            break

    oppo_move = int(input(""))
    board[N - 1 - count_list[oppo_move]][oppo_move] = 1
    count_list[oppo_move] +=1
	


