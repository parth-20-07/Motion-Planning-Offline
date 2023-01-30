import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.cbook as cbook
import matplotlib.image as image
import csv
import os
import time
from search import dfs, bfs
import numpy as np


from PIL import Image


def merge_images(file1, file2, seconds):
    """Merge two images into one, displayed side by side
    :param file1: path to first image file
    :param file2: path to second image file
    :return: the merged Image object
    """
    image1 = Image.open(file1)
    image2 = Image.open(file2)

    (width1, height1) = image1.size
    (width2, height2) = image2.size

    result_width = width1 + width2
    result_height = max(height1, height2)

    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=image1, box=(0, 0))
    result.paste(im=image2, box=(width1, 0))
    result.save(f'Images/{seconds} Map.png')
    return result

# Load map, start and goal point.


def load_map(file_path):
    grid = []
    start = [0, 0]
    goal = [0, 0]
    # Load from the file
    with open(file_path, 'r') as map_file:
        reader = csv.reader(map_file)
        for i, row in enumerate(reader):
            # load start and goal point
            if i == 0:
                start[0] = int(row[1])
                start[1] = int(row[2])
            elif i == 1:
                goal[0] = int(row[1])
                goal[1] = int(row[2])
            # load the map
            else:
                int_row = [int(col) for col in row]
                grid.append(int_row)
    return grid, start, goal


# Draw final results
def draw_path(grid, path, title, steps):
    # Visualization of the found path using matplotlib
    fig, ax = plt.subplots(1)
    ax.margins()
    # Draw map
    row = len(grid)     # map size
    col = len(grid[0])  # map size
    for i in range(row):
        for j in range(col):
            if grid[i][j]:
                ax.add_patch(Rectangle((j-0.5, i-0.5), 1, 1,
                             edgecolor='k', facecolor='k'))  # obstacle
            else:
                ax.add_patch(Rectangle((j-0.5, i-0.5), 1, 1,
                             edgecolor='k', facecolor='w'))  # free space
    # Draw path
    for x, y in path:
        ax.add_patch(Rectangle((y-0.5, x-0.5), 1, 1,
                     edgecolor='k', facecolor='b'))          # path
    ax.add_patch(Rectangle((start[1]-0.5, start[0]-0.5),
                 1, 1, edgecolor='k', facecolor='g'))  # start
    ax.add_patch(Rectangle((goal[1]-0.5, goal[0]-0.5),
                 1, 1, edgecolor='k', facecolor='r'))  # goal
    # Graph settings
    plt.title(f"{title}: {steps} Steps")
    plt.axis('scaled')
    plt.gca().invert_yaxis()
    plt.savefig(f"{title}.png")


if __name__ == "__main__":
    # Load the map
    grid, start, goal = load_map('map.csv')

    # Search
    bfs_path, bfs_steps = bfs(grid, start, goal)
    dfs_path, dfs_steps = dfs(grid, start, goal)

    # Show result
    seconds = round(time.time())
    draw_path(grid, bfs_path, 'BFS',  bfs_steps)
    draw_path(grid, dfs_path, 'DFS',  dfs_steps)

    if not os.path.isdir('Images'):
        os.mkdir('Images')
    merge_images('BFS.png', 'DFS.png', seconds)
    os.system(f'rm BFS.png DFS.png')
