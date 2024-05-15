#!/usr/bin/python3
"""
Module to calculate the perimeter of
an Island
"""


def island_perimeter(grid):
    """
    Calculate Island perimeter
    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4  # Each land cell contributes 4 sides to the perimeter

                # Check adjacent cells (up, down, left, right) and subtract if adjacent cell is also land
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtract 2 for each adjacent land cell (vertical)
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Subtract 2 for each adjacent land cell (horizontal)

    return perimeter
