import time
import random

def print_with_delay(message, delay=1):
    print(message)
    time.sleep(delay)

print_with_delay("Welcome to the Mind Reading Game!",1)
print_with_delay("Can you read my mind?", 2)
print_with_delay("I don't think you can.", 2)
print_with_delay("Choose a number between 1 and 100.", 2)
print_with_delay("If you are right, you will receive your mind reading score.", 2)
print_with_delay("If you are wrong, I will let you know if you need to think of a number higher or lower than the one you predicted.", 2)
print_with_delay("I am thinking of a number between 1 and 100.", 2)

number = random.randint(1, 100)
count = 0

while True:
    try:
        num = int(input("Predict the number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    count += 1

    if num < 1 or num > 100:
        print("You are beyond the valid range (1 to 100). Please try again.")
    elif num < number:
        print("Nope! It's a number higher than that.")
    elif num > number:
        print("Nope! It's a number lower than that.")
    else:
        print(f"Congratulations! You guessed it right in {count} attempts.")

        if count > 1:
            print(f"Your mind reading score is {round(100 / count, 2)} out of 100.")
        else:
            print("Your mind reading score is 100 out of 100.")

        break
