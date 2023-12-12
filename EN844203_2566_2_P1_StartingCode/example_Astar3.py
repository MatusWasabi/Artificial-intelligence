import sys
from search import initialize_Astar, Astar
import myglobal

secret_map_file = "map2.txt"
K = 3
solution = 0

with open(secret_map_file, 'r') as file:
    m, n = map(int, file.readline().split())
    sr, sc = map(int, file.readline().split())
    gr, gc = map(int, file.readline().split())
    myglobal.secret_map = [file.readline().strip() for _ in range(m)]
    myglobal.secret_map = [[myglobal.secret_map[i][j] for j in range(n)] for i in range(m)]

myglobal.explore_calls = []
initialize_Astar(m, n, sr, sc, gr, gc, K)
answer = Astar()

if solution == answer:
    print("Correct shortest distance!!!")
    print("You have called the explore() function", len(myglobal.explore_calls), "times")
else:
    print("Incorrect shortest distance :(")
