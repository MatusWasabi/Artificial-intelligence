#####
#
# Name: Matus Yaowvasrisuwan
# Student ID: 633040476-6
#
#####

from explore import explore  ##### DO NOT CHANGE THIS LINE #####


def initialize_dfs(m, n, sr, sc, gr, gc):
    # Here I do global variables for 
    # m for number of rows
    # n for number of columns
    # sr for row of starting point
    # sc for column of starting point

    global row_size
    global column_size
    global start_row
    global start_col

    row_size = m
    column_size = n
    start_row = sr
    start_col = sc

    # I do not use gr and gc here. No need, I discussed with prof.

    pass  # TODO


def dfs():

    # Right here I set up my values that will be used for the looping later
    # DFS is stack. This means first in, last out. You will need this for the location of searching 
    # I recommend you have an array to take record where you "EXPLORE" so that it is easy for you to debug

    my_stack = [(start_row, start_col)]
    explored_grid = []

    # Before going to code using while loop I do recommend you to loop it with limited time first
    # Personally, I set a time where the loop will run and keep going if it goes correctly.
    # When you can reached the goal, you can find another way to run this looping
    search_time = 0

    # Looping
    # grid_where_you_will_start_expand = stack.pop()
    # You check if you can go to that direction
    # For right, it will be grid_where_you_will_start_expand[0], grid_where_you_will_start_expand[1] + 1
    # Then you check if the explored grid can go or not
    # If yes, then put it in stack. If no ignore it
    # Then keep exploring

    while search_time < 1:
        print(f"Stack before poping {my_stack}")
        expand_from_this = my_stack.pop()
        print(f"Stack after poping {my_stack}")
        print(f"This is where you will start as reference point for each loop {expand_from_this}")
        

        if((expand_from_this[1] + 1) != row_size):
            result_from_exploring_right = explore(expand_from_this[0], expand_from_this[1] + 1)
            explored_grid.append((expand_from_this[0], expand_from_this[1] + 1))

        if(result_from_exploring_right != "X"):
            my_stack.append((expand_from_this[0], expand_from_this[1] + 1))

        print(f"Explored Grid {explored_grid}")
        search_time += 1
        print()

    # For this dfs(), you explore right, down, left, up
    # But you stack.append up, left, down, right
    # In example_dfs, you need to implement only right and up
    


    pass  # TODO


def initialize_bfs(m, n, sr, sc, gr, gc):
    pass  # TODO


def bfs():


    # BFS is queue. This means first in, first out. You will need this for the location of searching 


    # Looping
    # grid_where_you_will_start_expand = queue.pop(0)

    # You check if you can go to that direction
    # For right, it will be grid_where_you_will_start_expand[0], grid_where_you_will_start_expand[1] + 1
    # Then you check if the explored grid can go or not
    # If yes, then put it in stack. If no ignore it
    # Then keep exploring

    # For this bfs(), you explore right, down, left, up
    # And lucky for you, just queue.append() right, down, left, up
    # In example_bfs, you need to implement only right and up

    pass  # TODO




def initialize_Astar(m, n, sr, sc, gr, gc, k):
    pass  # TODO


def Astar():
    f_cost = 0
    return f_cost  # TODO
