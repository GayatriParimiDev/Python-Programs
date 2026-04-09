import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic-Tac-Toe")

players = ["X", "O"]
current_player = players[0]
board = [[" " for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]


def check_winner(player):
    
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
 
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def on_click(row, col):
    global current_player

    if board[row][col] == " ":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, state="disabled")

        if check_winner(current_player):
            messagebox.showinfo("Game Over", f"🎉 Player {current_player} wins!")
            reset_game()
            return

        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
            return

       
        current_player = players[(players.index(current_player) + 1) % 2]
    else:
        messagebox.showwarning("Invalid Move", "Cell already taken!")


def reset_game():
    global board, current_player
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = players[0]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=" ", state="normal")


for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=" ", font=("Arial", 20), width=5, height=2,
                                  command=lambda r=i, c=j: on_click(r, c))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()
