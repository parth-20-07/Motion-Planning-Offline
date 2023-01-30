import queue
# Basic searching algorithms
# Class for each node in the grid


class Node:
    def __init__(self, row, col, is_obs, h):
        self.row = row        # coordinate
        self.col = col        # coordinate
        self.is_obs = is_obs  # obstacle?
        self.cost = None      # total cost (depend on the algorithm)
        self.parent = None    # previous node


# --------------------------- CHECK FOR EMPTY CELLS -------------------------- #
"""Check if the cell on around is empty
    Mark as Visited if empty

Args:
    grid (list(int,int)): 2D Grid to scan
    y (int): y coordinate of object
    x (int): x coordinate of object
    data_type (string): "queue" -> BFS
                            "stack" -> DFS
    x_data (x_data_structure): Data Structure to hold info of next x to visit
    y_data (y_data_structure): Data Structure to hold info of next y to visit

Returns:
    bool: True -> Cell is empty
            False -> Cell is visited/obstacle
"""


def is_left_empty(grid, y, x, data_type, x_data, y_data):
    if x == 0:
        return False
    else:
        if grid[y][x-1] == 0:
            if (data_type == 'queue'):
                x_data.put(x-1)
                y_data.put(y)
            elif (data_type == 'stack'):
                x_data.append(x-1)
                y_data.append(y)
            grid[y][x-1] = 2
            return True
        else:
            return False


def is_right_empty(grid, y, x, data_type, x_data, y_data):
    grid_height = len(grid)-1
    grid_width = len(grid[0]) - 1
    if x == grid_width:
        return False
    else:
        if grid[y][x+1] == 0:
            if (data_type == 'queue'):
                x_data.put(x+1)
                y_data.put(y)
            elif (data_type == 'stack'):
                x_data.append(x+1)
                y_data.append(y)
            grid[y][x+1] = 2
            return True
        else:
            return False


def is_up_empty(grid, y, x, data_type, x_data, y_data):
    if y == 0:
        return False
    else:
        if grid[y-1][x] == 0:
            if (data_type == 'queue'):
                x_data.put(x)
                y_data.put(y-1)
            elif (data_type == 'stack'):
                x_data.append(x)
                y_data.append(y-1)
            grid[y-1][x] = 2
            return True
        else:
            return False


def is_down_empty(grid, y, x, data_type, x_data, y_data):
    grid_height = len(grid)-1
    grid_width = len(grid[0]) - 1
    if y == grid_height:
        return False
    else:
        if grid[y+1][x] == 0:
            if (data_type == 'queue'):
                x_data.put(x)
                y_data.put(y+1)
            elif (data_type == 'stack'):
                x_data.append(x)
                y_data.append(y+1)
            grid[y+1][x] = 2
            return True
        else:
            return False


def clear_grid(grid):
    """Change all the visited grid marks from '2' to '0'

    Args:
        grid (list(int,int)): Grid to plan path
    """
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (grid[y][x] == 2):
                grid[y][x] = 0


def list_path(start, final_path):
    """Convert the string of path into coordinates to visit

    Args:
        start ([int,int]): Starting Coordinates of the grid
        final_path (String): String of path found

    Returns:
        _type_: _description_
    """
    # print(f"Steps for BFS: {final_path}")
    y, x = start
    path = []
    path.append([y, x])
    steps = 1
    for step in final_path:
        if (step == 'D'):
            y = y+1
            steps += 1
        elif (step == 'R'):
            x = x+1
            steps += 1
        elif (step == 'U'):
            y = y-1
            steps += 1
        elif (step == 'L'):
            x = x-1
            steps += 1
        path.append([y, x])
    return steps, path


def bfs(grid, start, goal):
    '''Return a path found by BFS alogirhm
       and the number of steps it takes to find it.

    arguments:
    grid - A nested list with datatype int. 0 represents free space while 1 is obstacle.
           e.g. a 3x3 2D map: [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    start - The start node in the map. e.g. [0, 0]
    goal -  The goal node in the map. e.g. [2, 2]

    return:
    path -  A nested list that represents coordinates of each step (including start and goal node),
            with data type int. e.g. [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2]]
    steps - Number of steps it takes to find the final solution,
            i.e. the number of nodes visited before finding a path (including start and goal node)

    >>> from main import load_map
    >>> grid, start, goal = load_map('test_map.csv')
    >>> bfs_path, bfs_steps = bfs(grid, start, goal)
    It takes 10 steps to find a path using BFS
    >>> bfs_path
    [[0, 0], [1, 0], [2, 0], [3, 0], [3, 1]]
    '''
    ### YOUR CODE HERE ###
    path = []
    steps = 0
    found = False
    x_queue = queue.Queue()
    y_queue = queue.Queue()
    p_queue = queue.Queue()
    y, x = start
    grid[y][x] = 2
    x_queue.put(x)
    y_queue.put(y)
    p_queue.put("")
    final_path = ''
    while not x_queue.empty():
        x = x_queue.get()
        y = y_queue.get()
        path_search = p_queue.get()

        if ((y == goal[0]) and (x == goal[1])):
            final_path = path_search
            found = True
            break

        if (is_right_empty(grid, y, x, 'queue', x_queue, y_queue)):
            p_queue.put(path_search+'R')
        if (is_down_empty(grid, y, x, 'queue', x_queue, y_queue)):
            p_queue.put(path_search+'D')
        if (is_left_empty(grid, y, x, 'queue', x_queue, y_queue)):
            p_queue.put(path_search+'L')
        if (is_up_empty(grid, y, x, 'queue', x_queue, y_queue)):
            p_queue.put(path_search+'U')

    if found:
        steps, path = list_path(start, final_path)
    clear_grid(grid)

    if found:
        print(f"It takes {steps} steps to find a path using BFS")
    else:
        print("No path found")
    return path, steps


def dfs(grid, start, goal):
    '''Return a path found by DFS alogrithm 
       and the number of steps it takes to find it.

    arguments:
    grid - A nested list with datatype int. 0 represents free space while 1 is obstacle.
           e.g. a 3x3 2D map: [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    start - The start node in the map. e.g. [0, 0]
    goal -  The goal node in the map. e.g. [2, 2]

    return:
    path -  A nested list that represents coordinates of each step (including start and goal node), 
            with data type int. e.g. [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2]]
    steps - Number of steps it takes to find the final solution, 
            i.e. the number of nodes visited before finding a path (including start and goal node)

    >>> from main import load_map
    >>> grid, start, goal = load_map('test_map.csv')
    >>> dfs_path, dfs_steps = dfs(grid, start, goal)
    It takes 9 steps to find a path using DFS
    >>> dfs_path
    [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [2, 3], [3, 3], [3, 2], [3, 1]]
    '''
    ### YOUR CODE HERE ###
    path = []
    steps = 0
    found = False

    x_stack = []
    y_stack = []
    p_stack = []

    y_stack.append(start[0])
    x_stack.append(start[1])
    p_stack.append('')

    y, x = start
    grid[y][x] = 2

    final_path = ''

    # DFS - Terative (G,s)
    while (len(x_stack) != 0):
        y = y_stack.pop()
        x = x_stack.pop()
        path_search = p_stack.pop()

        if ((y == goal[0]) and (x == goal[1])):
            final_path = path_search
            found = True
            break

        if (is_right_empty(grid, y, x, 'stack', x_stack, y_stack)):
            p_stack.append(path_search+'R')
        if (is_down_empty(grid, y, x, 'stack', x_stack, y_stack)):
            p_stack.append(path_search+'D')
        if (is_left_empty(grid, y, x, 'stack', x_stack, y_stack)):
            p_stack.append(path_search+'L')
        if (is_up_empty(grid, y, x, 'stack', x_stack, y_stack)):
            p_stack.append(path_search+'U')

    if found:
        steps, path = list_path(start, final_path)
    clear_grid(grid)

    if found:
        print(f"It takes {steps} steps to find a path using DFS")
    else:
        print("No path found")
    return path, steps


# Doctest
if __name__ == "__main__":
    # load doc test
    from doctest import testmod, run_docstring_examples
    # Test all the functions
    testmod()
