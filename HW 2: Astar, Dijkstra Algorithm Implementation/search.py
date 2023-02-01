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


def dijkstra(grid, start, goal):
    '''Return a path found by Dijkstra algorithm 
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
    '''
    ### YOUR CODE HERE ###
    path = []
    steps = 0
    found = False

    if found:
        print(f"It takes {steps} steps to find a path using Dijkstra")
    else:
        print("No path found")
    return path, steps


def astar(grid, start, goal):
    '''Return a path found by A* algorithm
        and the number of steps it takes to find it.

    arguments:
    grid - A nested list with datatype int. 0 represents free space while 1 is obstacle.
            e.g. a 3x3 2D map: [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    start - The start node in the map. e.g. [0, 0]
    goal  - The goal node in the map. e.g. [2, 2]

    return:
    path  - A nested list that represents coordinates of each step (including start and goal node), 
            with data type int. e.g. [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2]]
    steps - Number of steps it takes to find the final solution, 
            i.e. the number of nodes visited before finding a path (including start and goal node)
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
