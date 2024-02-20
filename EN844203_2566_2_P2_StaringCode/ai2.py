#####
#
# Name: Akapohn Sriyam
# Student ID: 633040584-3
#
#####

import random
import time
import math
import sys
sys.setrecursionlimit(10**6)

print("ready")

N, M, F, X, T = input("").strip().split(" ")
N = int(N)  # Row
M = int(M)  # Column
F = int(F)  # First turn 1 player, 0 opponent
X = int(X)  # Goal connecting
T = float(T)  # Time limit
count_list = [0] * M
# R, L, TR, TL, BR, BL, B
# [(0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1), (-1, 0)]
# Horizon, Vertical, Di-UpR, Di-UpL
direction_list = [(0, 1), (1, 0), (1, 1), (-1, 1)]
# Location data is (row, col)
p_Locations = set()
o_Locations = set()


def SearchArea(node, player_moves):
    row, col = node
    # Right, Up, Diagonal (Right-Up), Diagonal (Left-Up)
    directions = [(1, 0), (0, 1), (1, 1), (-1, 1)]
    score = 0
    getWinner = False
    for dx, dy in directions:
        count = 1
        for direction in [-1, 1]:
            x, y = col + direction * dx, row + direction * dy
            while 0 <= x < M and 0 <= y < N and (y, x) in player_moves:
                count += 1
                x += direction * dx
                y += direction * dy
        if count >= X:
            getWinner = True
            score += 1

    return score, getWinner


def MinimaxABP(node, board, plrMoved, oppMoved, isMax, depth, startTime, timeout, alpha, beta):
    pScore, isWin = SearchArea(node, plrMoved, True)
    oScore, isLose = SearchArea(node, oppMoved, False)

    if depth == 0 or time.time() - startTime >= timeout or isWin or isLose:
        return (node[0], pScore + oScore)

    if isMax:
        value = -math.inf
        column = random.randint(0, M-1)
        for col in board:
            currNode = (board[col], col)
            if currNode[0] < N:
                copyBoard = board.copy()
                copyPlrMoved = plrMoved.copy()

                copyBoard[col] += 1
                copyPlrMoved.add(currNode)
                score = MinimaxABP(currNode, copyBoard, copyPlrMoved, oppMoved,
                                   False, startTime, depth-1, timeout-0.001, alpha, beta)[1]
                if score > value:
                    value = score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
        return column, value

    else:
        value = math.inf
        column = random.randint(0, M-1)
        for col in board:
            currNode = (board[col], col)
            if currNode[0] < N:
                min_copyBoard = board.copy()
                min_copyOppMoved = oppMoved.copy()

                min_copyBoard[col] += 1
                min_copyOppMoved.add(currNode)
                score = MinimaxABP(currNode, min_copyBoard, plrMoved, min_copyOppMoved,
                                   True, startTime, depth-1, timeout-0.001, alpha, beta)[1]
                if score < value:
                    value = score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
        return column, value


# ======== mAiN ======== #
playerTurn = False
if F == 0:
    oppo_move = int(input(""))
    count_list[oppo_move] += 1
    o_Locations.add((count_list[oppo_move], oppo_move))
    playerTurn = True
else:
    my_move = random.randint(0, M-1)
    print(my_move)
    count_list[my_move] += 1
    p_Locations.add((count_list[my_move], my_move))

while True:
    if playerTurn:
        node = random.randint(0, M-1)
        my_move = MinimaxABP((count_list[node], node), count_list, p_Locations,
                             o_Locations, True, 99, time.time(), T, -math.inf, math.inf)[0]
        print(my_move)
        count_list[my_move] += 1
        p_Locations.add((count_list[my_move], my_move))

    oppo_move = int(input(""))
    count_list[oppo_move] += 1
    o_Locations.add((count_list[oppo_move], oppo_move))
    playerTurn = True
