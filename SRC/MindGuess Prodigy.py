import time
import random

class MindReadingGame:
    def __init__(self):
        self.number = random.randint(1, 100)
        self.count = 0

    def print_with_delay(self, message, delay=1):
        print(message)
        time.sleep(delay)

    def play_game(self):
        self.print_with_delay("Welcome to the Mind Reading Game!", 1)
        self.print_with_delay("Can you read my mind?", 2)
        self.print_with_delay("I don't think you can.", 2)
        self.print_with_delay("Choose a number between 1 and 100.", 2)
        self.print_with_delay("If you are right, you will receive your mind reading score.", 2)
        self.print_with_delay("If you are wrong, I will let you know if you need to think of a number higher or lower than the one you predicted.", 2)
        self.print_with_delay("I am thinking of a number between 1 and 100.", 2)

        while True:
            try:
                num = int(input("Predict the number: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            self.count += 1

            if num < 1 or num > 100:
                print("You are beyond the valid range (1 to 100). Please try again.")
            elif num < self.number:
                print("Nope! It's a number higher than that.")
            elif num > self.number:
                print("Nope! It's a number lower than that.")
            else:
                print(f"Congratulations! You guessed it right in {self.count} attempts.")

                if self.count > 1:
                    print(f"Your mind reading score is {round(100 / self.count, 2)} out of 100.")
                else:
                    print("Your mind reading score is 100 out of 100.")

                break

# Instantiate the class and start the game
mind_reading_game = MindReadingGame()
mind_reading_game.play_game()
