#####
#
# Name: Matus Yaowvasrisuwan
# Student ID: 633040476-6
#
#####

from explore import explore  ##### DO NOT CHANGE THIS LINE #####    

import math

def initialize_dfs(m, n, sr, sc, gr, gc):
    global row_size
    global col_size
    global start_row
    global start_col

    row_size, col_size, start_row, start_col = m, n, sr, sc
    


    pass  # TODO


def dfs():
    
    stack = []
    start = (start_row, start_col)
    visited = [start]

    stack.append(start)

    search_try = 0

    while True:
        print(f"Stack {stack}")
        state = stack.pop()

        right = (state[0], state[1] + 1)
        up = (state[0] - 1, state[1])
        left = (state[0], state[1] - 1)
        down = (state[0] + 1, state[1])
       
        directions = [right, up, left, down]
        stack_queue = []
        
        for direction in directions:
            if(1 <= direction[0] < (row_size - 1) and 1 <= direction[1] < (col_size - 1)) and direction not in visited:
                direction_val = explore(direction[0], direction[1])
                visited.append(direction)
                if direction_val == "G":
                    return
                elif direction_val != "X":
                    stack_queue.append(direction)

        stack_queue.reverse()
        stack.extend(stack_queue)
        search_try += 1

    pass



def initialize_bfs(m, n, sr, sc, gr, gc):
    global row_size
    global col_size
    global start_row
    global start_col
    row_size, col_size, start_row, start_col = m, n, sr, sc
    pass  # TODO


def bfs():

    queue = []
    start = (start_row, start_col)
    visited = [start]

    queue.append(start)


    while True:
        print(f"Stack {queue}")
        state = queue.pop(0)

        right = (state[0], state[1] + 1)
        up = (state[0] - 1, state[1])
        left = (state[0], state[1] - 1)
        down = (state[0] + 1, state[1])
       
        directions = [right, up, left, down]
        queue_queue = []
        
        for direction in directions:
            if(1 <= direction[0] < (row_size - 1) and 1 <= direction[1] < (col_size - 1)) and direction not in visited:
                direction_val = explore(direction[0], direction[1])
                visited.append(direction)
                if direction_val == "G":
                    return
                elif direction_val != "X":
                    queue.append(direction)







def initialize_Astar(m, n, sr, sc, gr, gc, k):
    global row_size
    global col_size
    global start_row
    global start_col
    global goal_row
    global goal_col
    global MAGIC_BLADE

    row_size, col_size, start_row, start_col, goal_row, goal_col, MAGIC_BLADE = m, n, sr, sc, gr, gc, k
    pass  # TODO


def Astar():
    magical_blade = MAGIC_BLADE
    priority_queue = []
    visited = []

    start_grid = ((start_row, start_col), magical_blade, 0, 0)
    goal = (goal_row, goal_col)

    priority_queue.append(start_grid)

    while True:
        current = min(priority_queue, key=lambda node: node[2])
        print(f"Current node {current}")
        magical_blade = current[1]
        
        priority_queue.remove(current)

        if current[0] == (goal_row, goal_col):
            return current[3]
        
        if (current[0], magical_blade) not in visited:
            visited.append((current[0], magical_blade))
            
            directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

            for direction in directions:
                checking = tuple(map(sum, zip(direction, current[0])))
                if(CheckInBound(checking)):
                    value = explore(checking[0], checking[1])

                    if(value == "X"):
                        if(magical_blade > 0):
                            value = "0"
                            magical_blade -= 1

                    if(value == "S" or value == "G"):
                        value = "0"

                    if(value.isdigit()):
                        value = int(value)
                    
                    if(value != "X"):
                        gn = value + current[3]
                        hn = EuclideanDistance(checking, goal)
                        fn = gn + hn
                        priority_queue.append((checking, magical_blade, fn, gn))


def CheckInBound(grid: tuple[int, int]):
    if ((1 <= grid[0] < (row_size - 1)) and (1 <= grid[1] < (col_size - 1))):
        return True
    else:
        return False
    
def EuclideanDistance(start, goal):
    return ((goal[0] - start[0])**2 + (goal[1] - start[1])**2 ) ** 0.5
