#This module contains functions for a simple Tic-Tac-Toe game.

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-"*5)

def check_winner(board, mark):
    return any(all(cell==mark for cell in row) for row in board) or \
           any(all(row[i]==mark for row in board) for i in range(3)) or \
           all(board[i][i]==mark for i in range(3)) or \
           all(board[i][2-i]==mark for i in range(3))

# --- Add this code to run and show output ---
if __name__ == "__main__":
    board = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["O", "x", "X"]
    ]
    print_board(board)
    if check_winner(board, "X"):
        print("X wins!")
    elif check_winner(board, "O"):
        print("O wins!")
    else:
        print("No winner.")
