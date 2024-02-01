# MainMenu.py

from tkinter import messagebox
from Atlas import AtlasGameGUI
from Hangman import HangmanGUI
from Maze import MazeGame
from MindGuess_Prodigy import MindReadingGame
from Rock_Paper_Scissors import StonePaperScissorsGUI
from snakes_and_snakes import SnakesAndLaddersGame
from Sudoku import SudokuGame
from tictactoe import TicTacToeGameApp
from Word_Whisler import WordJumbleGame
from Word_Blitz import TypingTest  # Import the TypingTest class

def display_menu():
    print("Main Menu:")
    print("1. Atlas Game")
    print("2. Hangman Game")
    print("3. Maze Game")
    print("4. Mind Reading Game")
    print("5. Stone Paper Scissors Game")
    print("6. Snakes and Ladders Game")
    print("7. Sudoku Game")
    print("8. Tic-Tac-Toe Game")
    print("9. Word Jumble Game")
    print("10. Word Blitz Typing Test")  # Add Word Blitz Typing Test option
    print("11. Exit")

def start_atlas_game():
    atlas_game_gui = AtlasGameGUI()

def start_hangman_game():
    hangman_gui = HangmanGUI()

def start_maze_game():
    maze_game = MazeGame()
    maze_game.run_game()

def start_mind_reading_game():
    mind_reading_game = MindReadingGame()
    mind_reading_game.play_game()

def start_stone_paper_scissors_game():
    root = tk.Tk()
    stone_paper_scissors_game = StonePaperScissorsGUI(root)
    root.mainloop()

def start_snakes_and_ladders_game():
    snakes_and_ladders_game = SnakesAndLaddersGame()
    snakes_and_ladders_game.mainloop()

def start_sudoku_game():
    sudoku_game = SudokuGame()
    sudoku_game.sudoku_game()

def start_tic_tac_toe_game():
    tic_tac_toe_game = TicTacToeGameApp()

def start_word_jumble_game():
    word_jumble_game = WordJumbleGame()
    word_jumble_game.run()

def start_word_blitz_typing_test():  # New function to start Word Blitz Typing Test
    print("Choose the number of words to type:")
    print("1. 10 words")
    print("2. 30 words")
    print("3. 50 words")
    print("4. 70 words")
    print("5. 100 words")
    print("6. 250 words")
    print("7. 500 words")

    choice = input("Enter your choice : ")

    if choice == '1':
        test = TypingTest(10)
    elif choice == '2':
        test = TypingTest(30)
    elif choice == '3':
        test = TypingTest(50)
    elif choice == '4':
        test = TypingTest(70)
    elif choice == '5':
        test = TypingTest(100)
    elif choice == '6':
        test = TypingTest(250)
    elif choice == '7':
        test = TypingTest(500)
    else:
        print("Invalid choice. Please run the script again.")

    test.typing_test()

if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Enter the number of the game you want to play (or '11' to exit): ")

        if choice == '1':
            start_atlas_game()
        elif choice == '2':
            start_hangman_game()
        elif choice == '3':
            start_maze_game()
        elif choice == '4':
            start_mind_reading_game()
        elif choice == '5':
            start_stone_paper_scissors_game()
        elif choice == '6':
            start_snakes_and_ladders_game()
        elif choice == '7':
            start_sudoku_game()
        elif choice == '8':
            start_tic_tac_toe_game()
        elif choice == '9':
            start_word_jumble_game()
        elif choice == '10':
            start_word_blitz_typing_test()  # Add Word Blitz Typing Test option
        elif choice == '11':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid number.")
