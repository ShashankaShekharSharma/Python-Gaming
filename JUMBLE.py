import random

def choose_word(difficulty):
    if difficulty == "easy":
        words = ["elephant", "guitar", "orange", "mirror", "table"]
    elif difficulty == "medium":
        words = ["keyboard", "jungle", "puzzle", "oxygen", "sunset"]
    elif difficulty == "hard":
        words = ["algorithm", "knowledge", "exquisite", "zygote", "quantum"]
    elif difficulty == "ninja":
        words = ["phenomenal", "ambidextrous", "magnanimous", "labyrinth", "perpendicular"]
    else:
        raise ValueError("Invalid difficulty level")

    return random.choice(words)

def jumble_word(word):
    jumbled_word = list(word)
    random.shuffle(jumbled_word)
    return ''.join(jumbled_word)

def get_hint(word):
    hint_length = max(1, len(word) // 2)
    hint_indices = random.sample(range(len(word)), hint_length)
    hint = ''.join(word[i] if i in hint_indices else '_' for i in range(len(word)))
    return hint

def play_word_jumbles():
    while True:
        print("Welcome to Word Jumbles!")
        
        difficulty = input("Choose a difficulty level (easy/medium/hard/ninja): ").lower()
        original_word = choose_word(difficulty)
        jumbled_word = jumble_word(original_word)

        print("Jumbled Word:", jumbled_word)

        attempts = 3
        while attempts > 0:
            guess = input("Your guess (or type 'hint' for a hint): ").lower()

            if guess == original_word:
                print("Congratulations! You guessed it correctly.")
                break
            elif guess == "hint":
                hint = get_hint(original_word)
                print("Hint:", hint)
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"Wrong! Try again. {attempts} {'attempts' if attempts > 1 else 'attempt'} left.")
                else:
                    print(f"Sorry, you're out of attempts. The correct word was: {original_word}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_word_jumbles()
