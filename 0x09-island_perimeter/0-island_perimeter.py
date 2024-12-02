#!/usr/bin/python3

"""
Performs the island perimeter algorithm
"""


def island_perimeter(grid):
    """
    compute the island perimeter
    """
    perimeter = 0
    border = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                border = 4
                if j != 0:
                    if grid[i][j - 1] == 1:
                        border -= 1
                if j != (len(grid[0]) - 1):
                    if grid[i][j + 1] == 1:
                        border -= 1
                if i != 0:
                    if grid[i - 1][j] == 1:
                        border -= 1
                if i != (len(grid) - 1):
                    if grid[i + 1][j] == 1:
                        border -= 1
                perimeter += border
    return perimeter
