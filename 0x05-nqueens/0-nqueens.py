#!/usr/bin/python3

"""
A program that solves the N queens puzzle
"""

import sys


def is_safe(board, cordinate, n: int) -> bool:
    for cor in board:
        if cor[0] == cordinate[0] or cor[1] == cordinate[1]:
            return False
        for i, j in zip(range(1, n - cor[0]), range(1, n - cor[1])):
            if cor[0] + i == cordinate[0] and cor[1] + j == cordinate[1]:
                return False

        for i, j in zip(range(cor[0] + 1, n), range(cor[1] - 1, -1, -1)):
            if i == cordinate[0] and j == cordinate[1]:
                return False
    return True


def solve_nq(board, row, n):
    if row >= n:
        return

    for col in range(n):
        cordinate = [row, col]
        if is_safe(board, cordinate, n):
            copy_board = board.copy()
            copy_board.append(cordinate)
            if len(copy_board) == n:
                print(copy_board)
                return
            else:
                solve_nq(copy_board, row + 1, n)


def main() -> None:
    """
    performs the N queens algorithm
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    n = sys.argv[1]
    try:
        int_n = int(n)
    except ValueError as e:
        print("N must be a number")
        exit(1)
    if int_n < 4:
        print("N must be at least 4")
        exit(1)

    board = []
    solve_nq(board, 0, int_n)
    exit(0)


if __name__ == "__main__":
    main()
