def print_board_with_blanks(board, original_board):	def print_board_with_blanks(board, original_board):
    for i in range(9):	    for i in range(9):
        if i % 3 == 0 and i != 0:	        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")		@@ -16,8 +27,8 @@ def print_board_with_blanks(board, original_board):
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


def sudoku_game():	def sudoku_game():
    print("Welcome to Sudoku Game")	    print("Welcome to Sudoku Game")
    a=int(input("On a Scale of 1 to 5, what level of sudoku you want solve: "))	    a = int(input("On a Scale of 1 to 5, what level of sudoku you want to solve: "))
    puzzle1 = [	    puzzle1 =  [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],	        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],	        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],	        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],		@@ -28,7 +39,6 @@ def sudoku_game():
        [4, 0, 0, 8, 0, 3, 0, 0, 1],	
        [7, 0, 0, 0, 2, 0, 0, 0, 6],	
        [0, 6, 0, 0, 0, 0, 2, 8, 0],	
        [0, 0, 0, 4, 1, 9, 0, 0, 5],	        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]	        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]	    ]

    puzzle2 = [	    puzzle2 = [
        [0, 0, 0, 0, 0, 0, 0, 9, 0],	        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 4, 3, 0, 2, 0, 0, 8],	        [0, 0, 4, 3, 0, 2, 0, 0, 8],
        [0, 7, 0, 0, 8, 0, 6, 4, 0],		@@ -41,7 +51,7 @@ def sudoku_game():
        [4, 0, 0, 0, 0, 0, 0, 0, 5],	
        [0, 0, 7, 0, 0, 0, 9, 0, 0],	
        [5, 0, 0, 0, 0, 0, 0, 0, 3],	
        [0, 9, 6, 0, 5, 0, 0, 8, 0],	
        [8, 0, 0, 9, 0, 4, 2, 0, 0],	
        [0, 1, 0, 0, 0, 0, 0, 0, 0]	        [0, 1, 0, 0, 0, 0, 0, 0, 0]
    ]	    ]


    puzzle3 = [	    puzzle3 =  [
        [0, 4, 0, 0, 5, 0, 0, 0, 0],	        [0, 4, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 8, 0, 2],	        [0, 0, 0, 0, 0, 1, 8, 0, 2],
        [8, 0, 0, 0, 6, 4, 0, 0, 7],	        [8, 0, 0, 0, 6, 4, 0, 0, 7],
        [0, 2, 0, 0, 0, 0, 0, 9, 0],		@@ -53,6 +63,7 @@ def sudoku_game():
        [0, 0, 7, 9, 0, 3, 6, 0, 0],	
        [0, 1, 0, 0, 0, 0, 0, 4, 0],	
        [5, 0, 0, 7, 3, 0, 0, 0, 1],	
        [3, 0, 2, 8, 0, 0, 0, 0, 0],	
        [0, 0, 0, 0, 2, 0, 0, 8, 0]	        [0, 0, 0, 0, 2, 0, 0, 8, 0]
    ]	    ]



    puzzle4 = [	    puzzle4 = [
        [0, 0, 0, 0, 0, 0, 1, 2, 0],	        [0, 0, 0, 0, 0, 0, 1, 2, 0],
        [0, 8, 0, 0, 2, 0, 0, 0, 0],	        [0, 8, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 6, 0, 8, 0],		@@ -65,6 +76,7 @@ def sudoku_game():
        [0, 0, 7, 0, 0, 2, 0, 0, 0],	
        [0, 0, 0, 0, 8, 0, 0, 0, 0],	
        [0, 0, 0, 6, 0, 0, 3, 0, 0],	
        [0, 5, 0, 2, 0, 0, 6, 0, 0],	
        [0, 0, 0, 0, 9, 0, 0, 5, 0],	
        [0, 4, 2, 0, 0, 0, 0, 0, 0]	        [0, 4, 2, 0, 0, 0, 0, 0, 0]
    ]	    ]



    puzzle5 = [	    puzzle5 = [
        [0, 0, 0, 0, 6, 0, 0, 0, 0],	        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 2, 0, 7, 0, 0, 0, 8, 0],	        [0, 2, 0, 7, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 8, 3, 0, 0, 0],		@@ -76,16 +88,17 @@ def sudoku_game():
        [0, 0, 0, 0, 0, 7, 0, 0, 0],	
        [0, 9, 7, 0, 0, 0, 2, 4, 0],	
        [0, 0, 0, 3, 0, 0, 0, 0, 0],	
        [0, 0, 0, 4, 1, 0, 0, 0, 0],	
        [0, 6, 0, 0, 0, 5, 0, 2, 0],	        [0, 6, 0, 0, 0, 5, 0, 2, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0]	        [0, 0, 0, 0, 7, 0, 0, 0, 0]
    ]	    ]

    if a == 1:	    if a == 1:
      puzzle = puzzle1	        puzzle = puzzle1
    elif a == 2:	    elif a == 2:
      puzzle = puzzle2	        puzzle = puzzle2
    elif a == 3:	    elif a == 3:
      puzzle = puzzle3	        puzzle = puzzle3
    elif a == 4:	    elif a == 4:
      puzzle = puzzle4	        puzzle = puzzle4
    else:	    else:
      puzzle = puzzle5	        puzzle = puzzle5


    user_board = [row[:] for row in puzzle]	    user_board = [row[:] for row in puzzle]

    while not is_board_filled(user_board):	
        print_board_with_blanks(user_board, puzzle)	

        try:	
            row = int(input("Enter the row number (1-9): ")) - 1	
            col = int(input("Enter the column number (1-9): ")) - 1	
            num = int(input("Enter the number (1-9): "))	
        except ValueError:	
            print("Please enter a valid number.")	
            continue	

        if 0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9 and user_board[row][col] == 0:	
            if is_valid_move(user_board, row, col, num):	
                user_board[row][col] = num	
                print("Number added successfully!")	
            else:	
                print("Invalid move. Try again.")	
        else:	
            print("Invalid input. Try again.")	

    print_board_with_blanks(user_board, puzzle)	
    if user_board == puzzle:	
        print("You win!")	
    else:	
        print("You lose!")	

if __name__ == "__main__":	
    sudoku_game()	
