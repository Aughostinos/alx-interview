#!/usr/bin/python3
"""0x05. N Queens"""
import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        # Check if there's a queen in the same column or diagonal
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N, board, row):
    """Recursively solve the N queens problem"""
    if row == N:
        # All queens are placed, print the solution
        print([[i, board[i]] for i in range(N)])
        return
    
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(N, board, row + 1)


if __name__ == "__main__":
    # Check if the right number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Validate that N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board with -1 to indicate no queen is placed
    board = [-1 for _ in range(N)]
    
    # Solve the N queens problem
    solve_nqueens(N, board, 0)
