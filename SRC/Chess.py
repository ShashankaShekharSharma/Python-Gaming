import sys
import time
import os

# Define the board class.
class Board:
    def __init__(self):
        self.board = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"]
        ]

    def print_board(self):
        print("   a b c d e f g h")
        for i, row in enumerate(self.board):
            print(str(i + 1) + " ", end="")
            for piece in row:
                print(piece, end=" ")
            print()

    def move_piece(self, start, end):
        if self.board[start[0]][start[1]] == " ":
            print("There is no piece at that location.")
            return False

        if self.board[end[0]][end[1]] != " ":
            # Piece at the destination is an opponent's piece, capture it
            print("Capturing {} at {}!".format(self.board[end[0]][end[1]], chr(end[1] + ord('a')) + str(end[0] + 1)))

        self.board[end[0]][end[1]] = self.board[start[0]][start[1]]
        self.board[start[0]][start[1]] = " "

        return True

# Define the player class.
class Player:
    def __init__(self, color, board):
        self.color = color
        self.board = board

    def get_move(self):
        while True:
            move = input("Enter your move (e.g. e2e4): ")
            if move.lower() == "resign":
                return move

            if len(move) != 4:
                print("Invalid move.")
                continue

            start = (int(move[1]) - 1, ord(move[0]) - ord('a'))
            end = (int(move[3]) - 1, ord(move[2]) - ord('a'))

            if not self.board.move_piece(start, end):
                print("Invalid move.")
                continue

            break

        return move

# Create the board and players.
board = Board()
player1 = Player("white", board)
player2 = Player("black", board)

# Main game loop.
while True:
    # Print the board.
    os.system('clear')
    board.print_board()

    # Get the move from the current player.
    if player1.color == "white":
        move = player1.get_move()
    else:
        move = player2.get_move()

    # Check if the game is over.
    if move.lower() == "resign":
        print("Game over. {} wins.".format(player1.color if player1.color == "white" else player2.color))
        break

    # Switch to the other player.
    player1, player2 = player2, player1

# Print the final board.
os.system('clear')
board.print_board()
