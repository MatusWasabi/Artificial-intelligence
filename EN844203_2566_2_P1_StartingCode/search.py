#####
#
# Name: Matus Yaowvasrisuwan
# Student ID: 633040476-6
#
#####

from explore import explore  ##### DO NOT CHANGE THIS LINE #####


def initialize_dfs(m, n, sr, sc, gr, gc):
    global row_size
    global col_size
    global start_row
    global start_col

    row_size, col_size, start_row, start_col = m, n, sr, sc

    pass  # TODO


def dfs():

    start_location = (start_row, start_col)
    visited_order = []
    stack = [start_location]
    search_values = [""]
    search_try = 0
    right_value = ""
    down_value = ""

    while "G" not in search_values:

        current_location = stack.pop()
        #Check right can go
        if current_location[1] < col_size - 2:
            right = (current_location[0], current_location[1] + 1)
            right_value = explore(right[0], right[1])
            visited_order.append(right)

        #Check down can go
        if current_location[0] < row_size - 2:
            down = (current_location[0] + 1, current_location[1])
            down_value = explore(down[0], down[1])
            visited_order.append(down)

        #Check if what we have now won't be dup with value of visited grid
        if(current_location != down and down_value != "X"):
            search_values.append(down_value)
            stack.append(down)
        
        if(current_location != right and right_value != "X"):
            search_values.append(right_value)
            stack.append(right)

        search_try += 1
            
    print(visited_order)

    pass  # TODO


def initialize_bfs(m, n, sr, sc, gr, gc):
    global row_size
    global col_size
    global start_row
    global start_col
    row_size, col_size, start_row, start_col = m, n, sr, sc
    pass  # TODO


def bfs():

    start_location = (start_row, start_col)
    visited_order = []
    queue = [start_location]
    search_values = [""]
    search_try = 0
    right_value = ""
    down_value = ""

    # May need refactoring

    while "G" not in search_values:
        current_location = queue.pop(0)

        print(f"Pop out {current_location}", end=" ")
        
        #Check if right can go
        if (current_location[1] < col_size - 2) and (current_location[0], current_location[1] + 1) not in visited_order:
            right = (current_location[0], current_location[1] + 1)
            right_value = explore(right[0], right[1])
            visited_order.append(right)
            


        #Check down can go
        if (current_location[0] < row_size - 2) and (current_location[0] + 1, current_location[1]) not in visited_order:
            down = (current_location[0] + 1, current_location[1])
            down_value = explore(down[0], down[1])
            visited_order.append(down)

        #Check if what we have now won't be dup with value of visited grid
        if(current_location != right and right not in queue and right_value != "X"):
            search_values.append(right_value)
            queue.append(right)

        if(current_location != down and down not in queue and down_value != "X"):
            search_values.append(down_value)
            queue.append(down)


        print(f"This is queue after search {queue}")
        search_try += 1

    print(visited_order)
    pass  # TODO




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

    f_cost = 0
    search_try = 0
    current_location = (start_row, start_col)
    goal_location = (goal_row, goal_col)

    f_cost += int(explore(1, 2))



    print(f"This is {f_cost}")
    return f_cost  # TODO
