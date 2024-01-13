import time
import random

def print_with_delay(message, delay=1):
    print(message)
    time.sleep(delay)

def play_game():
    print_with_delay("Welcome")
    
    while True:
        play_option = input("Do you want to play Stone Paper Scissors? (1 for Yes, 0 for No): ")
        
        if play_option == '1':
            print_with_delay("Let's play Stone Paper Scissors", 2)
            print_with_delay("Stone", 1)
            print_with_delay("Paper", 1)
            print_with_delay("Scissors", 1)

            print_with_delay(random.choice(['Stone', 'Paper', 'Scissors']), 2)

            play_option = input("Do you want to play again? (1 for Yes, 0 for No): ")
            
            if play_option != '1':
                print_with_delay("Bye Bye")
                break
        elif play_option == '0':
            print_with_delay("Bye Bye")
            break
        else:
            print_with_delay("Invalid input! Please enter 1 to play or 0 to exit.")

if __name__ == "__main__":
    play_game()
