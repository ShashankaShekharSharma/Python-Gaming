class SudokuGame:
    def __init__(self):
        self.puzzle1 = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

        self.puzzle2 = [
            [0, 0, 0, 0, 0, 0, 0, 9, 0],
            [0, 0, 4, 3, 0, 2, 0, 0, 8],
            [0, 7, 0, 0, 8, 0, 6, 4, 0],
            [4, 0, 0, 0, 0, 0, 0, 0, 5],
            [0, 0, 7, 0, 0, 0, 9, 0, 0],
            [5, 0, 0, 0, 0, 0, 0, 0, 3],
            [0, 9, 6, 0, 5, 0, 0, 8, 0],
            [8, 0, 0, 9, 0, 4, 2, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0]
        ]

        self.puzzle3 = [
            [0, 4, 0, 0, 5, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 8, 0, 2],
            [8, 0, 0, 0, 6, 4, 0, 0, 7],
            [0, 2, 0, 0, 0, 0, 0, 9, 0],
            [0, 0, 7, 9, 0, 3, 6, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 4, 0],
            [5, 0, 0, 7, 3, 0, 0, 0, 1],
            [3, 0, 2, 8, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 8, 0]
        ]

        self.puzzle4 = [
            [0, 0, 0, 0, 0, 0, 1, 2, 0],
            [0, 8, 0, 0, 2, 0, 0, 0, 0],
            [0, 0, 4, 0, 0, 6, 0, 8, 0],
            [0, 0, 7, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 0, 8, 0, 0, 0, 0],
            [0, 0, 0, 6, 0, 0, 3, 0, 0],
            [0, 5, 0, 2, 0, 0, 6, 0, 0],
            [0, 0, 0, 0, 9, 0, 0, 5, 0],
            [0, 4, 2, 0, 0, 0, 0, 0, 0]
        ]

        self.puzzle5 = [
            [0, 0, 0, 0, 6, 0, 0, 0, 0],
            [0, 2, 0, 7, 0, 0, 0, 8, 0],
            [0, 0, 0, 0, 8, 3, 0, 0, 0],
            [0, 0, 0, 0, 0, 7, 0, 0, 0],
            [0, 9, 7, 0, 0, 0, 2, 4, 0],
            [0, 0, 0, 3, 0, 0, 0, 0, 0],
            [0, 0, 0, 4, 1, 0, 0, 0, 0],
            [0, 6, 0, 0, 0, 5, 0, 2, 0],
            [0, 0, 0, 0, 7, 0, 0, 0, 0]
        ]

    def print_board_with_blanks(self, board, original_board):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - -")
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                if original_board[i][j] == 0:
                    if board[i][j] == 0:
                        print("_", end=" ")
                    else:
                        print(board[i][j], end=" ")
                else:
                    print(original_board[i][j], end=" ")
            print()

    def is_board_filled(self, board):
        for row in board:
            for num in row:
                if num == 0:
                    return False
        return True

    def is_valid_move(self, board, row, col, num):
        # Check if the number is already in the row or column
        if num in board[row] or num in [board[i][col] for i in range(9)]:
            return False

        # Check if the number is in the 3x3 subgrid
        subgrid_row, subgrid_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(subgrid_row, subgrid_row + 3):
            for j in range(subgrid_col, subgrid_col + 3):
                if board[i][j] == num:
                    return False

        return True

    def sudoku_game(self):
        print("Welcome to Sudoku Game")
        a = int(input("On a Scale of 1 to 5, what level of sudoku you want to solve: "))

        if a == 1:
            puzzle = self.puzzle1
        elif a == 2:
            puzzle = self.puzzle2
        elif a == 3:
            puzzle = self.puzzle3
        elif a == 4:
            puzzle = self.puzzle4
        else:
            puzzle = self.puzzle5

        user_board = [row[:] for row in puzzle]

        while not self.is_board_filled(user_board):
            self.print_board_with_blanks(user_board, puzzle)

            try:
                row = int(input("Enter the row number (1-9): ")) - 1
                col = int(input("Enter the column number (1-9): ")) - 1
                num = int(input("Enter the number (1-9): "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if 0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9 and user_board[row][col] == 0:
                if self.is_valid_move(user_board, row, col, num):
                    user_board[row][col] = num
                    print("Number added successfully!")
                else:
                    print("Invalid move. Try again.")
            else:
                print("Invalid input. Try again.")

        self.print_board_with_blanks(user_board, puzzle)
        if all(user_board[i] == puzzle[i] for i in range(9)):

            print("You win!")
        else:
            print("You lose!")

if __name__ == "__main__":
    game = SudokuGame()
    game.sudoku_game()

