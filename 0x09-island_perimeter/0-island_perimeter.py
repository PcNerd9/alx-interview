#!/usr/bin/python3

"""
contain a function island_perimeter
"""
from typing import List


def island_perimeter(grid: List[List]) -> int:
    """
    compute the island perimiter of a list of list represented
    as grid where 1 represent a land and 0 represent water
    """

    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4

                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    perimeter -= 1

                if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                    perimeter -= 1

                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    perimeter -= 1

                if i + 1 < len(grid) and grid[i + 1][j] == 1:
                    perimeter -= 1
    return perimeter
