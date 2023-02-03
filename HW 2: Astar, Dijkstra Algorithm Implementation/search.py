import numpy as np
import queue
# Basic searching algorithms

# Class for each node in the grid


class Node:
    def __init__(self, row, col, is_obs, h):
        self.row = row        # coordinate
        self.col = col        # coordinate
        self.is_obs = is_obs  # obstacle?
        self.g = None         # cost to come (previous g + moving cost)
        self.h = h            # heuristic
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
            return True
        else:
            return False


def is_up_left_empty(grid, y, x, data_type, x_data, y_data):
    if x == 0 or y == 0:
        return False
    else:
        if grid[y-1][x-1] == 0:
            if (data_type == 'queue'):
                x_data.put(x-1)
                y_data.put(y-1)
            elif (data_type == 'stack'):
                x_data.append(x-1)
                y_data.append(y-1)
            return True
        else:
            return False


def is_up_right_empty(grid, y, x, data_type, x_data, y_data):
    grid_height = len(grid)-1
    grid_width = len(grid[0]) - 1
    if x == grid_width or y == 0:
        return False
    else:
        if grid[y-1][x+1] == 0:
            if (data_type == 'queue'):
                x_data.put(x+1)
                y_data.put(y-1)
            elif (data_type == 'stack'):
                x_data.append(x+1)
                y_data.append(y-1)
            return True
        else:
            return False


def is_down_left_empty(grid, y, x, data_type, x_data, y_data):
    grid_height = len(grid)-1
    grid_width = len(grid[0]) - 1
    if y == grid_height or x == 0:
        return False
    else:
        if grid[y+1][x-1] == 0:
            if (data_type == 'queue'):
                x_data.put(x-1)
                y_data.put(y+1)
            elif (data_type == 'stack'):
                x_data.append(x-1)
                y_data.append(y+1)
            return True
        else:
            return False


def is_down_right_empty(grid, y, x, data_type, x_data, y_data):
    grid_height = len(grid)-1
    grid_width = len(grid[0]) - 1
    if y == grid_height or x == grid_width:
        return False
    else:
        if grid[y+1][x+1] == 0:
            if (data_type == 'queue'):
                x_data.put(x+1)
                y_data.put(y+1)
            elif (data_type == 'stack'):
                x_data.append(x+1)
                y_data.append(y+1)
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
        elif (step == 'Q'):
            x = x-1
            y = y-1
            steps += 1
        elif (step == 'E'):
            x = x+1
            y = y-1
            steps += 1
        elif (step == 'Z'):
            x = x-1
            y = y+1
            steps += 1
        elif (step == 'C'):
            x = x+1
            y = y+1
            steps += 1
        path.append([y, x])
    return steps, path


def dijkstra(grid, start, goal):
    """Return a path found by Dijkstra algorithm
        and the number of steps it takes to find it.

    Args:
        grid (array): A nested list with datatype int. 0 represents free space while 1 is obstacle.
                        e.g. a 3x3 2D map: [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        start ((int,int)): The start node in the map. e.g. [0, 0]
        goal ((int,int)): The goal node in the map. e.g. [2, 2]

    Returns:
    path (list(int,int)): A nested list that represents coordinates of each step(including start and goal node),
                            with data type int. e.g. [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2]]
    steps (int): Number of steps it takes to find the final solution,
                    i.e. the number of nodes visited before finding a path(including start and goal node)
    """
    ### YOUR CODE HERE ###
    path = []
    steps = 0
    found = False

    grid_data = np.zeros([len(grid), len(grid[0]), 3], dtype=np.int)

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid_data[y][x][2] = 100000

    x_queue = queue.Queue()
    y_queue = queue.Queue()

    x_queue.put(start[1])
    y_queue.put(start[0])

    grid_data[start[0]][start[1]] = (start[0], start[1], 0)

    while not x_queue.empty():
        x = x_queue.get()
        y = y_queue.get()
        distance = grid_data[y][x][2]

        if ((y == goal[0]) and (x == goal[1])):
            found = True
            break

        if (is_down_empty(grid, y, x, 'queue', x_queue, y_queue)):
            ny = y+1
            nx = x
            x_queue.put(nx)
            y_queue.put(ny)
            if (grid_data[ny][nx][2] > distance+1):
                grid_data[ny][nx] = (y, x, distance+1)
        if (is_down_left_empty(grid, y, x, 'queue', x_queue, y_queue)):
            ny = y+1
            nx = x-1
            x_queue.put(nx)
            y_queue.put(ny)
            if (grid_data[ny][nx][2] > distance+1):
                grid_data[ny][nx] = (y, x, distance+1)
        if (is_left_empty(grid, y, x, 'queue', x_queue, y_queue)):
            ny = y
            nx = x-1
            x_queue.put(nx)
            y_queue.put(ny)
            if (grid_data[ny][nx][2] > distance+1):
                grid_data[ny][nx] = (y, x, distance+1)
        if (is_up_left_empty(grid, y, x, 'queue', x_queue, y_queue)):
            ny = y-1
            nx = x-1
            x_queue.put(nx)
            y_queue.put(ny)
            if (grid_data[ny][nx][2] > distance+1):
                grid_data[ny][nx] = (y, x, distance+1)
        if (is_up_empty(grid, y, x, 'queue', x_queue, y_queue)):
            ny = y-1
            nx = x
            x_queue.put(nx)
            y_queue.put(ny)
            if (grid_data[ny][nx][2] > distance+1):
                grid_data[ny][nx] = (y, x, distance+1)
        if (is_up_right_empty(grid, y, x, 'queue', x_queue, y_queue)):
            ny = y-1
            nx = x+1
            x_queue.put(nx)
            y_queue.put(ny)
            if (grid_data[ny][nx][2] > distance+1):
                grid_data[ny][nx] = (y, x, distance+1)
        if (is_right_empty(grid, y, x, 'queue', x_queue, y_queue)):
            ny = y
            nx = x+1
            x_queue.put(nx)
            y_queue.put(ny)
            if (grid_data[ny][nx][2] > distance+1):
                grid_data[ny][nx] = (y, x, distance+1)
        if (is_down_right_empty(grid, y, x, 'queue', x_queue, y_queue)):
            ny = y+1
            nx = x+1
            x_queue.put(nx)
            y_queue.put(ny)
            if (grid_data[ny][nx][2] > distance+1):
                grid_data[ny][nx] = (y, x, distance+1)
        grid[y][x] = 2

    if found:
        y, x = goal
        while True:
            ny = grid_data[y][x][0]
            nx = grid_data[y][x][1]
            y = ny
            x = nx
            path.append([y, x])
            if ((y == start[0]) and (x == start[1])):
                break
        steps = len(path)
    clear_grid(grid)

    if found:
        print(f"It takes {steps} steps to find a path using Dijkstra")
    else:
        print("No path found")
    return path, steps


def astar(grid, start, goal):
    '''Return a path found by A * algorithm
        and the number of steps it takes to find it.

    arguments:
    grid - A nested list with datatype int. 0 represents free space while 1 is obstacle.
            e.g. a 3x3 2D map: [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    start - The start node in the map. e.g. [0, 0]
    goal - The goal node in the map. e.g. [2, 2]

    return:
    path - A nested list that represents coordinates of each step(including start and goal node),
            with data type int. e.g. [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2]]
    steps - Number of steps it takes to find the final solution,
            i.e. the number of nodes visited before finding a path(including start and goal node)
    '''
    ### YOUR CODE HERE ###
    path = []
    steps = 0
    found = False

    if found:
        print(f"It takes {steps} steps to find a path using A*")
    else:
        print("No path found")
    return path, steps


# Doctest
if __name__ == "__main__":
    # load doc test
    from doctest import testmod, run_docstring_examples
    # Test all the functions
    testmod()
