def is_board_filled(board):
    # Placeholder for checking if the board is filled
    for row in board:
        if 0 in row:
            return False
    return True

def is_valid_move(board, row, col, num):
    # Placeholder for checking if the move is valid
    return True

def print_board_with_blanks(board, original_board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
	@@ -16,8 +27,8 @@ def print_board_with_blanks(board, original_board):

def sudoku_game():
    print("Welcome to Sudoku Game")
    a = int(input("On a Scale of 1 to 5, what level of sudoku you want to solve: "))
    puzzle1 =  [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
	@@ -28,7 +39,6 @@ def sudoku_game():
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    puzzle2 = [
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 4, 3, 0, 2, 0, 0, 8],
	@@ -41,7 +51,7 @@ def sudoku_game():
        [0, 1, 0, 0, 0, 0, 0, 0, 0]
    ]

    puzzle3 =  [
        [0, 4, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 8, 0, 2],
        [8, 0, 0, 0, 6, 4, 0, 0, 7],
	@@ -53,6 +63,7 @@ def sudoku_game():
        [0, 0, 0, 0, 2, 0, 0, 8, 0]
    ]


    puzzle4 = [
        [0, 0, 0, 0, 0, 0, 1, 2, 0],
        [0, 8, 0, 0, 2, 0, 0, 0, 0],
	@@ -65,6 +76,7 @@ def sudoku_game():
        [0, 4, 2, 0, 0, 0, 0, 0, 0]
    ]


    puzzle5 = [
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 2, 0, 7, 0, 0, 0, 8, 0],
	@@ -76,16 +88,17 @@ def sudoku_game():
        [0, 6, 0, 0, 0, 5, 0, 2, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0]
    ]

    if a == 1:
        puzzle = puzzle1
    elif a == 2:
        puzzle = puzzle2
    elif a == 3:
        puzzle = puzzle3
    elif a == 4:
        puzzle = puzzle4
    else:
        puzzle = puzzle5

    user_board = [row[:] for row in puzzle]
