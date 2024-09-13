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


def solve_nqueens(N, board=[], row=0):
    """ find all solutions"""
    if row == N:
        # All queens are placed
        print([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col):
            board.append(col)
            solve_nqueens(N, board, row + 1)
            board.pop()


if __name__ == "__main__":
    # check number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # make sure that N is greater than or equal to 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)
