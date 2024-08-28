#!/usr/bin/python3
"""
A module that solves the N queens problem.
"""
import sys


def solve_n_queens(n):
    """
    Solves the N queens problem and prints all solutions.
    """
    def is_safe(queens, row, col):
        """
        Helper function to check if it's safe
        to place a queen at the given row and col.
        """
        for r, c in enumerate(queens[:row]):
            if c == col or abs(r - row) == abs(c - col):
                return False
        return True

    def solve(row, queens):
        """
        Helper function to solve the N queens problem using backtracking.
        """
        if row == n:
            result.append(queens[:])
            return
        for col in range(n):
            if is_safe(queens, row, col):
                queens[row] = col
                solve(row + 1, queens)

    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    result = []
    queens = [-1] * n
    solve(0, queens)

    for solution in result:
        formatted_solution = [[i, col] for i, col in enumerate(solution)]
        print(formatted_solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_n_queens(N)
