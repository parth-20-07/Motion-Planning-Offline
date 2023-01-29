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


right = [0, +1]
down = [+1, 0]
left = [0, -1]
up = [-1, 0]


def is_left_empty(grid, y, x):
    if x == 0:
        return False
    else:
        if grid[y][x-1] == 0:
            return True
        else:
            return False


def is_right_empty(grid, y, x):
    grid_height = len(grid)-1
    grid_width = len(grid[0]) - 1
    if x == grid_width:
        return False
    else:
        if grid[y][x+1] == 0:
            return True
        else:
            return False


def is_up_empty(grid, y, x):
    if y == 0:
        return False
    else:
        if grid[y-1][x] == 0:
            return True
        else:
            return False


def is_down_empty(grid, y, x):
    grid_height = len(grid)-1
    grid_width = len(grid[0]) - 1
    if y == grid_height:
        return False
    else:
        if grid[y+1][x] == 0:
            return True
        else:
            return False


def clear_grid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (grid[y][x] == 2):
                grid[y][x] = 0


def list_path(start, steps, path, final_path):
    print(f"Steps for BFS: {final_path}")
    y, x = start
    for step in final_path:
        if (step == 'D'):
            y = y+1
            steps += 1
            path.append((y, x))
        elif (step == 'R'):
            x = x+1
            steps += 1
            path.append((y, x))
        elif (step == 'U'):
            y = y-1
            steps += 1
            path.append((y, x))
        elif (step == 'L'):
            x = x-1
            steps += 1
            path.append((y, x))
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

        if (is_down_empty(grid, y, x)):
            y_queue.put(y+1)
            x_queue.put(x)
            p_queue.put(path_search+'D')
            grid[y+1][x] = 2
        if (is_right_empty(grid, y, x)):
            y_queue.put(y)
            x_queue.put(x+1)
            p_queue.put(path_search+'R')
            grid[y][x+1] = 2
        if (is_up_empty(grid, y, x)):
            y_queue.put(y-1)
            x_queue.put(x)
            p_queue.put(path_search+'U')
            grid[y-1][x] = 2
        if (is_left_empty(grid, y, x)):
            y_queue.put(y)
            x_queue.put(x-1)
            p_queue.put(path_search+'L')
            grid[y][x-1] = 2
    if found:
        steps, path = list_path(start, steps, path, final_path)
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

        if (is_down_empty(grid, y, x)):
            y_stack.append(y+1)
            x_stack.append(x)
            p_stack.append(path_search+'D')
            grid[y+1][x] = 2
        if (is_right_empty(grid, y, x)):
            y_stack.append(y)
            x_stack.append(x+1)
            p_stack.append(path_search+'R')
            grid[y][x+1] = 2
        if (is_up_empty(grid, y, x)):
            y_stack.append(y-1)
            x_stack.append(x)
            p_stack.append(path_search+'U')
            grid[y-1][x] = 2
        if (is_left_empty(grid, y, x)):
            y_stack.append(y)
            x_stack.append(x-1)
            p_stack.append(path_search+'L')
            grid[y][x-1] = 2

    if found:
        steps, path = list_path(start, steps, path, final_path)
    clear_grid(grid)
    # DFS Recursive

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
