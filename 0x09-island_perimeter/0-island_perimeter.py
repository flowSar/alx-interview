#!/usr/bin/python3

# This script calculates the perimeter of an island in a 2D grid.
# The island is represented as a grid of 1s (land) and 0s (water).
# Each cell in the grid can have 4 boundaries (top, bottom, left, right),
# and the perimeter is determined by the number of
# water cells adjacent to land cells.

# Sets to store grid positions of cells based on the number of boundaries:
bound_4 = set()
bound_3 = set()
bound_2 = set()
bound_1 = set()


def boundary(grid, i, j):
    """
    Determines how many sides of a cell at position (i, j)
    are exposed to water.
    Updates the respective sets (bound_1, bound_2, bound_3, bound_4)
    based on the number of boundaries.

    Args:
        grid (list[list[int]]): The 2D grid representing the island and water.
        i (int): The row index of the cell.
        j (int): The column index of the cell.
    """
    boundaries = 0

    try:
        if i == 0 or grid[i-1][j] == 0:
            boundaries += 1
    except IndexError:
        boundaries += 1

    try:
        if grid[i+1][j] == 0:
            boundaries += 1
    except IndexError:
        boundaries += 1

    try:
        if grid[i][j+1] == 0:
            boundaries += 1
    except IndexError:
        boundaries += 1

    try:
        if j == 0 or grid[i][j-1] == 0:
            boundaries += 1
    except IndexError:
        boundaries += 1

    if boundaries == 1:
        bound_1.add((i, j))
    elif boundaries == 2:
        bound_2.add((i, j))
    elif boundaries == 3:
        bound_3.add((i, j))
    elif boundaries == 4:
        bound_4.add((i, j))


def island_perimeter(grid):
    """
    Calculates the perimeter of the island in a 2D grid.

    Args:
        grid (list[list[int]]): A 2D list representing
        the island (1s) and water (0s).

    Returns:
        int: The perimeter of the island.
    """
    if not grid:
        return 0

    n_row = len(grid)
    n_column = len(grid[0])

    for i in range(n_row):
        for j in range(n_column):
            if grid[i][j] == 1:
                boundary(grid, i, j)

                if len(bound_4) != 0:
                    return 4

    perimeter = (len(bound_3) * 3) + (len(bound_2) * 2) + len(bound_1)
    return perimeter
