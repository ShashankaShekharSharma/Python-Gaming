import random

class Hangman:
    def __init__(self):
        print("Welcome to the word guessing game")
        print("Guess the word related to technology to win the game")

    def get_word(self):
        words = ["python", "bhailang", "coder", "frontend", "backend", "fullstack", "hardware", "software",
                 "internet", "intranet", "email", "facebook", "instagram", "cybersecurity", "blockchain",
                 "cryptocurrency", "bitcoin", "ethereum", "metaverse", "motherboard", "bluetooth", "monitor",
                 "javascript", "computer", "programming", "software", "julia", "ruby", "algorithm", "bandwidth",
                 "encryption", "joystick", "keyboard", "mouse", "phone", "object", "network", "robot", "software",
                 "terminal", "cloud", "latency", "viewport", "github"]
        return random.choice(words).upper()

    def play_hangman(self):
        b = int(input("Choose game level: (1. Level 1.  2. Level 2.  3. Level 3.  (Enter the number)"))
        word = self.get_word()
        word_letters = set(word)  # Letters in the word
        alphabet = set(chr(i) for i in range(65, 91))  # All letters of the alphabet
        used_letters = set()  # Letters already guessed

        if b == 3:
            lives = 6
        elif b == 2:
            lives = 9
        else:
            lives = 12

        while len(word_letters) > 0 and lives > 0:
            print("Lives left:", lives)
            print("Used letters:", " ".join(used_letters))

            word_list = [letter if letter in used_letters else "-" for letter in word]
            print("Current word:", " ".join(word_list))

            user_letter = input("Guess a letter: ").upper()
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                    print("Correct guess!")
                else:
                    lives -= 1
                    print("Incorrect guess!")
            elif user_letter in used_letters:
                print("You already guessed that letter. Try again.")
            else:
                print("Invalid input. Please enter a letter.")

        if lives == 0:
            print("You lost! The word was", word)
            a = int(input("Do you want to play again (1 if yes, 0 if no): "))
            if a == 1:
                self.play_hangman()
            else:
                print("Bye")
        else:
            print("You won! The word was", word)
            a = int(input("Do you want to play again (1 if yes, 0 if no): "))
            if a == 1:
                self.play_hangman()
            else:
                print("Bye")


if __name__ == "__main__":
    hangman_game = Hangman()
    hangman_game.play_hangman()
