#####
#
# Name: Matus Yaowvasrisuwan
# Student ID: 633040476-6
#
#####

from explore import explore  ##### DO NOT CHANGE THIS LINE #####    

from queue import PriorityQueue

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

    search_try = 0

    while True:
        print(f"Stack {queue}")
        state = queue.pop(-1)

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
    global magical_blade

    row_size, col_size, start_row, start_col, goal_row, goal_col, magical_blade = m, n, sr, sc, gr, gc, k
    pass  # TODO


def Astar():
    
    start = (start_row, start_col)
    neighbor = dict()
    cost_to_this = dict()
    added_neighbor = []

    right = (start[0], start[1] + 1)
    right_value = explore(right[0], right[1])
    if right_value.isdigit():
        added_neighbor.append(right)
        cost_to_this[right] = int(right_value)

    down = (start[0] + 1, start[1] )
    down_value = explore(down[0], down[1])
    if down_value.isdigit():
        added_neighbor.append(down)
        cost_to_this[down] = int(down_value)

    
    neighbor[start] = added_neighbor



    print(f"neighbor {neighbor}")
    print(f"cost_to_this {cost_to_this}")


graph = {(1, 1): [(1, 2), (2, 1)],
         (1, 2): [()]
         }