import random

class TextBasedPuzzleGame:
    def __init__(self):
        self.levels = [
            {"type": "riddle", "question": "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?", "answer": "echo"},
            {"type": "logic", "question": "The sun rises in the east.", "correct_option": "True"},
            {"type": "word", "word": "python", "scrambled_word": "nythop"}
            # Add more levels and puzzles as needed
        ]

    def display_intro(self):
        print("Welcome to Text-Based Puzzle Game!")
        print("Solve puzzles to progress through levels and win the game.\n")

    def display_level_intro(self, level_name):
        print(f"\n*** {level_name} ***\n")

    def solve_riddle(self, riddle, answer):
        print(f"Riddle: {riddle}")
        user_answer = input("Your answer: ").lower()

        if user_answer == answer:
            print("Correct! You've solved the riddle.")
            return True
        else:
            print("Incorrect. Try again.")
            return False

    def solve_logic_puzzle(self, question, correct_option):
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

    def solve_word_game(self, word, scrambled_word):
        print(f"Unscramble the Word: {scrambled_word}")
        user_answer = input("Your answer: ").lower()

        if user_answer == word:
            print("Correct! You've unscrambled the word.")
            return True
        else:
            print("Incorrect. Try again.")
            return False

    def play_game(self):
        self.display_intro()

        for idx, level in enumerate(self.levels, start=1):
            level_name = f"Level {idx} - {level['type'].capitalize()}"

            self.display_level_intro(level_name)

            if level['type'] == 'riddle':
                if not self.solve_riddle(level['question'], level['answer']):
                    print("You failed to solve the riddle. Game over.")
                    return
            elif level['type'] == 'logic':
                if not self.solve_logic_puzzle(level['question'], level['correct_option']):
                    print("You failed to solve the logic puzzle. Game over.")
                    return
            elif level['type'] == 'word':
                if not self.solve_word_game(level['word'], level['scrambled_word']):
                    print("You failed to unscramble the word. Game over.")
                    return

        print("Congratulations! You've completed the game.")

if __name__ == "__main__":
    game = TextBasedPuzzleGame()
    game.play_game()
