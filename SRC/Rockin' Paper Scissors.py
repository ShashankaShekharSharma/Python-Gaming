import time
import random

def print_with_delay(message, delay=1):
    print(message)
    time.sleep(delay)

def get_user_choice():
    while True:
        user_choice = input("Choose (1) Stone, (2) Paper, or (3) Scissors: ")
        if user_choice in ['1', '2', '3']:
            return user_choice
        else:
            print_with_delay("Invalid input! Please enter 1, 2, or 3.")

def play_game():
    print_with_delay("Welcome to Stone Paper Scissors!")

    while True:
        print_with_delay("\nLet's play Stone Paper Scissors", 2)

        user_choice = get_user_choice()

        options = ['Stone', 'Paper', 'Scissors']
        print_with_delay(f"You chose: {options[int(user_choice) - 1]}", 1)

        print_with_delay("Computer is making a choice...", 2)
        computer_choice = random.choice(options)
        print_with_delay(f"Computer chose: {computer_choice}", 1)

        result = determine_winner(options[int(user_choice) - 1], computer_choice)
        print_with_delay(result, 1)

        play_option = input("Do you want to play again? (1 for Yes, 0 for No): ")

        if play_option != '1':
            print_with_delay("Thank you for playing! Bye Bye")
            break

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'Stone' and computer_choice == 'Scissors') or
        (user_choice == 'Paper' and computer_choice == 'Stone') or
        (user_choice == 'Scissors' and computer_choice == 'Paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

if __name__ == "__main__":
    play_game()
