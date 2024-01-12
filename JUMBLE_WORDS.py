import tkinter as tk
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

# Tkinter GUI functions
def new_game():
    global original_word, jumbled_word, score
    difficulty = difficulty_var.get().lower()
    original_word = choose_word(difficulty)
    jumbled_word = jumble_word(original_word)
    canvas.itemconfig(word_text, text=jumbled_word)
    entry.delete(0, tk.END)
    answer.config(text="")
    hint.config(text="")
    score = 0
    update_score()

def check():
    global original_word, score
    answer_text = entry.get().lower()
    if answer_text == original_word:
        score += 1
        answer.config(text="Congratulations! You guessed it correctly.")
    else:
        answer.config(text="Wrong! Try again.")
    update_score()

def show_hint():
    global original_word, score
    hint_text = get_hint(original_word)
    hint.config(text=f"Hint: {hint_text}")
    score += 0.5
    update_score()

def update_score():
    score_label.config(text=f"Score: {score}")

def quit_game():
    window.destroy()

# Create the main window
window = tk.Tk()
window.title("Word Jumble Game")

# Create and configure widgets
canvas = tk.Canvas(window, width=400, height=50)
canvas.pack()

word_text = canvas.create_text(200, 25, text="", font=("Helvetica", 16))

entry = tk.Entry(window)
entry.pack()

answer = tk.Label(window, text="")
answer.pack()

hint = tk.Label(window, text="")
hint.pack()

# Difficulty level selection
difficulty_var = tk.StringVar()
difficulty_var.set("easy")
difficulty_menu = tk.OptionMenu(window, difficulty_var, "easy", "medium", "hard", "ninja")
difficulty_menu.pack()

# Score label
score = 0
score_label = tk.Label(window, text="Score: 0")
score_label.pack()

# Create buttons
new_game_button = tk.Button(window, text="New Game", command=new_game)
check_button = tk.Button(window, text="Check", command=check)
hint_button = tk.Button(window, text="Hint", command=show_hint)
quit_button = tk.Button(window, text="Quit", command=quit_game)

# Place buttons in the window
new_game_button.pack(side=tk.LEFT)
check_button.pack(side=tk.LEFT)
hint_button.pack(side=tk.LEFT)
quit_button.pack(side=tk.LEFT)

# Start the game
new_game()

# Run the Tkinter event loop
window.mainloop()
