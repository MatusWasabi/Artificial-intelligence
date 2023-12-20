#####
#
# Name: POTSAWAT LALITLAKKANAKUL
# Student ID: 633040222-7
#
#####

from explore import explore  ##### DO NOT CHANGE THIS LINE #####


def initialize_bfs(m, n, sr, sc, gr, gc):
    global maze_size, start_pos, goal_pos
    maze_size = (m - 2, n - 2)
    start_pos = (sr, sc)
    goal_pos = (gr, gc)


def bfs():
    visited = set()
    visited.add(start_pos)
    queue = [(start_pos[0], start_pos[1])]

    while queue:
        current_cell = queue.pop(0)

        # Explore Right
        if current_cell[1] < maze_size[1]:
            right_cell = (current_cell[0], current_cell[1] + 1)
            if right_cell == goal_pos:
                visited.add(right_cell)
                right_val = explore(right_cell[0], right_cell[1])
                if right_val == "G":
                    return
            elif right_cell not in visited:
                visited.add(right_cell)
                right_val = explore(right_cell[0], right_cell[1])
                if right_val != "X":
                    queue.append(right_cell)
                    
        # Explore Top       
        if current_cell[0] > 1:
            top_cell = (current_cell[0] - 1, current_cell[1])
            if top_cell == goal_pos:
                visited.add(top_cell)
                top_val = explore(top_cell[0], top_cell[1])
                if top_val == "G":
                    return
            elif top_cell not in visited:
                visited.add(top_cell)
                top_val = explore(top_cell[0], top_cell[1])
                if top_val != "X":
                    queue.append(top_cell)

        # Explore Left
        if current_cell[1] > 1:
            left_cell = (current_cell[0], current_cell[1] - 1)
            if left_cell == goal_pos:
                visited.add(left_cell)
                left_val = explore(left_cell[0], left_cell[1])
                if left_val == "G":
                    return
            elif left_cell not in visited:
                visited.add(left_cell)
                left_val = explore(left_cell[0], left_cell[1])
                if left_val != "X":
                    queue.append(left_cell)

        # Explore Bottom
        if current_cell[0] < maze_size[0]:
            bottom_cell = (current_cell[0] + 1, current_cell[1])
            if bottom_cell == goal_pos:
                visited.add(bottom_cell)
                bottom_val = explore(bottom_cell[0], bottom_cell[1])
                if bottom_val == "G":
                    return
            elif bottom_cell not in visited:
                visited.add(bottom_cell)
                bottom_val = explore(bottom_cell[0], bottom_cell[1])
                if bottom_val != "X":
                    queue.append(bottom_cell)


def initialize_dfs(m, n, sr, sc, gr, gc):
    global maze_size, start_pos, goal_pos
    maze_size = (m - 2, n - 2)
    start_pos = (sr, sc)
    goal_pos = (gr, gc)


def dfs():
    visited = set()
    visited.add(start_pos)
    stack = [(start_pos[0], start_pos[1])]
    
    while stack:
        current_cell = stack.pop()
        reverse_stack = []

        # Explore Right
        if current_cell[1] < maze_size[1]:
            right_cell = (current_cell[0], current_cell[1] + 1)
            if right_cell == goal_pos:
                visited.add(right_cell)
                right_val = explore(right_cell[0], right_cell[1])
                if right_val == "G":
                    return
            elif right_cell not in visited:
                visited.add(right_cell)
                right_val = explore(right_cell[0], right_cell[1])
                if right_val != "X":
                    reverse_stack.append(right_cell)
                    
        # Explore Top       
        if current_cell[0] > 1:
            top_cell = (current_cell[0] - 1, current_cell[1])
            if top_cell == goal_pos:
                visited.add(top_cell)
                top_val = explore(top_cell[0], top_cell[1])
                if top_val == "G":
                    return
            elif top_cell not in visited:
                visited.add(top_cell)
                top_val = explore(top_cell[0], top_cell[1])
                if top_val != "X":
                    reverse_stack.append(top_cell)

        # Explore Left
        if current_cell[1] > 1:
            left_cell = (current_cell[0], current_cell[1] - 1)
            if left_cell == goal_pos:
                visited.add(left_cell)
                left_val = explore(left_cell[0], left_cell[1])
                if left_val == "G":
                    return
            elif left_cell not in visited:
                visited.add(left_cell)
                left_val = explore(left_cell[0], left_cell[1])
                if left_val != "X":
                    reverse_stack.append(left_cell)

        # Explore Bottom
        if current_cell[0] < maze_size[0]:
            bottom_cell = (current_cell[0] + 1, current_cell[1])
            if bottom_cell == goal_pos:
                visited.add(bottom_cell)
                bottom_val = explore(bottom_cell[0], bottom_cell[1])
                if bottom_val == "G":
                    return
            elif bottom_cell not in visited:
                visited.add(bottom_cell)
                bottom_val = explore(bottom_cell[0], bottom_cell[1])
                if bottom_val != "X":
                    reverse_stack.append(bottom_cell)
        
        # Reverse the order of exploration
        while reverse_stack:
            stack.append(reverse_stack.pop())
        

def initialize_Astar(m, n, sr, sc, gr, gc, k):
    global maze_size, start_pos, goal_pos, magic_blade
    maze_size = (m - 2, n - 2)
    start_pos = (sr, sc)
    goal_pos = (gr, gc)
    magic_blade = k


def Astar():
    def heuristic(position):
        return abs(position[0] - goal_pos[0]) + abs(position[1] - goal_pos[1])

    visited = set()
    visited.add(start_pos)
    priority_queue = [(heuristic(start_pos), 0, start_pos)]
    magic_blade_val = magic_blade

    while priority_queue:
        _, cost, current_cell = min(priority_queue)
        priority_queue.remove((heuristic(current_cell) + cost, cost, current_cell))

        # Explore Right
        if current_cell[1] < maze_size[1]:
            right_cell = (current_cell[0], current_cell[1] + 1)
            if right_cell == goal_pos:
                visited.add(right_cell)
                right_val = explore(right_cell[0], right_cell[1])
                if right_val == "G":
                    return cost
            elif right_cell not in visited:
                visited.add(right_cell)
                right_val = explore(right_cell[0], right_cell[1])
                if magic_blade_val > 0 and right_val == "X":
                    right_val = "0"
                    magic_blade_val -= 1
                if right_val != "X":
                    new_cost = cost + int(right_val)
                    priority_queue.append((new_cost + heuristic(right_cell), new_cost, right_cell))

        # Explore Top
        if current_cell[0] > 1:
            top_cell = (current_cell[0] - 1, current_cell[1])
            if top_cell == goal_pos:
                visited.add(top_cell)
                top_val = explore(top_cell[0], top_cell[1])
                if top_val == "G":
                    return cost
            elif top_cell not in visited:
                visited.add(top_cell)
                top_val = explore(top_cell[0], top_cell[1])
                if magic_blade_val > 0 and top_val == "X":
                    top_val = "0"
                    magic_blade_val -= 1
                if top_val != "X":
                    new_cost = cost + int(top_val)
                    priority_queue.append((new_cost + heuristic(top_cell), new_cost, top_cell))

        # Explore Left
        if current_cell[1] > 1:
            left_cell = (current_cell[0], current_cell[1] - 1)
            if left_cell == goal_pos:
                visited.add(left_cell)
                left_val = explore(left_cell[0], left_cell[1])
                if left_val == "G":
                    return cost
            elif left_cell not in visited:
                visited.add(left_cell)
                left_val = explore(left_cell[0], left_cell[1])
                if magic_blade_val > 0 and left_val == "X":
                    left_val = "0"
                    magic_blade_val -= 1
                if left_val != "X":
                    new_cost = cost + int(left_val)
                    priority_queue.append((new_cost + heuristic(left_cell), new_cost, left_cell))

        # Explore Bottom
        if current_cell[0] < maze_size[0]:
            bottom_cell = (current_cell[0] + 1, current_cell[1])
            if bottom_cell == goal_pos:
                visited.add(bottom_cell)
                bottom_val = explore(bottom_cell[0], bottom_cell[1])
                if bottom_val == "G":
                    return cost
            elif bottom_cell not in visited:
                visited.add(bottom_cell)
                bottom_val = explore(bottom_cell[0], bottom_cell[1])
                if magic_blade_val > 0 and bottom_val == "X":
                    bottom_val = "0"
                    magic_blade_val -= 1
                if bottom_val != "X":
                    new_cost = cost + int(bottom_val)
                    priority_queue.append((new_cost + heuristic(bottom_cell), new_cost, bottom_cell))

    return 0

