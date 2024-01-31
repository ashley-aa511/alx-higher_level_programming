#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    # Check if there is a queen in the same row to the left
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check if there is a queen in the upper diagonal on the left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the lower diagonal on the left
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def print_solution(board, N):
    solution = []
    for row in board:
        solution.append(['Q' if cell == 1 else '.' for cell in row])
    return solution

def solve_nqueens(N):
    board = [[0] * N for _ in range(N)]
    solutions = []

    def solve(row):
        nonlocal solutions
        if row == N:
            solutions.append(print_solution(board, N))
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                solve(row + 1)
                board[row][col] = 0  # backtrack

    solve(0)
    return solutions

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if N is a number
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)

    # Print the solutions
    for solution in solutions:
        for row in solution:
            print(' '.join(row))
        print()

if __name__ == "__main__":
    main()
