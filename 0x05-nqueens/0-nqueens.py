#!/usr/bin/python3
"""model for N queens puzzle is the challenge """
import sys


def solve_queens_problem(board_size):
    """solve queen probleem"""

    def is_valid_position(pos, occupied_pos):
        """check is position valid"""
        for i in range(len(occupied_pos)):
            if (
                occupied_pos[i] == pos or
                occupied_pos[i] - i == pos - len(occupied_pos) or
                occupied_pos[i] + i == pos + len(occupied_pos)
            ):
                return False
        return True

    def place_queens(board_size, index, occupied_pos, solutions):
        """place queens """
        if index == board_size:
            solutions.append(occupied_pos[:])
            return

        for i in range(board_size):
            if is_valid_position(i, occupied_pos):
                occupied_pos.append(i)
                place_queens(board_size, index + 1, occupied_pos, solutions)
                occupied_pos.pop()

    solutions = []
    place_queens(board_size, 0, [], solutions)
    return solutions


def main():
    """main function """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_queens_problem(board_size)
    for solution in solutions:
        print([[i, solution[i]] for i in range(len(solution))])


if __name__ == "__main__":
    main()
