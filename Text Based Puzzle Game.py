import random

def display_intro():
    print("Welcome to Text-Based Puzzle Game!")
    print("Solve puzzles to progress through levels and win the game.\n")

def display_level_intro(level_name):
    print(f"\n*** {level_name} ***\n")

def solve_riddle(riddle, answer):
    print(f"Riddle: {riddle}")
    user_answer = input("Your answer: ").lower()

    if user_answer == answer:
        print("Correct! You've solved the riddle.")
        return True
    else:
        print("Incorrect. Try again.")
        return False

def solve_logic_puzzle(question, correct_option):
    print(f"Logic Puzzle: {question}")
    print("Options:")
    options = ["A", "B", "C", "D"]
    for i in range(4):
        print(f"{options[i]}. {correct_option if i == 0 else random.choice(['True', 'False'])}")

    user_answer = input("Your choice (A/B/C/D): ").upper()

    if user_answer == "A" and correct_option == "True":
        print("Correct! You've solved the logic puzzle.")
        return True
    elif user_answer != "A" and correct_option == "False":
        print("Correct! You've solved the logic puzzle.")
        return True
    else:
        print("Incorrect. Try again.")
        return False

def solve_word_game(word, scrambled_word):
    print(f"Unscramble the Word: {scrambled_word}")
    user_answer = input("Your answer: ").lower()

    if user_answer == word:
        print("Correct! You've unscrambled the word.")
        return True
    else:
        print("Incorrect. Try again.")
        return False

def play_game():
    display_intro()

    # Level 1: Easy
    display_level_intro("Level 1 - Easy Riddle")
    if not solve_riddle("I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?", "echo"):
        print("You failed to solve the riddle. Game over.")
        return

    # Level 2: Medium
    display_level_intro("Level 2 - Medium Logic Puzzle")
    if not solve_logic_puzzle("The sun rises in the east.", "True"):
        print("You failed to solve the logic puzzle. Game over.")
        return

    # Level 3: Hard
    display_level_intro("Level 3 - Hard Word Game")
    if not solve_word_game("python", "nythop"):
        print("You failed to unscramble the word. Game over.")
        return

    # Add more levels and puzzles as needed

    print("Congratulations! You've completed the game.")

if __name__ == "__main__":
    play_game()
