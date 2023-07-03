#!/usr/bin/python3
"""101-nqueens finds all possible solutions the N queens puzzle
    Attributes: N (int): base number of queens, and length of board side in piece positions
"""
from sys import argv

def is_safe(board, row, col):
    """ Check if the current position is safe for a queen
        Check row on the left side"""
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left side
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve_nqueens(board, col):
    """ Base case: If all queens are placed
     then print the solution """
    if col == N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    # Recursive backtracking to find a safe position
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens(board, col + 1)
            board[i][col] = 0

def print_solutions(solutions):
    """ start of the func """
    for solution in solutions:
        print(solution)

# Check if the correct number of arguments is provided
if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)

# Check if N is a valid integer
try:
    N = int(argv[1])
except ValueError:
    print("N must be a number")
    exit(1)

# Check if N is at least 4
if N < 4:
    print("N must be at least 4")
    exit(1)

# Solve the N Queens problem
board = [[0 for _ in range(N)] for _ in range(N)]
solutions = []
solve_nqueens(board, 0)
print_solutions(solutions)
