import tkinter as tk
import random

class WordJumbleGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Word Jumble Game")

        self.original_word = ""
        self.jumbled_word = ""
        self.score = 0

        # Create and configure widgets
        self.canvas = tk.Canvas(self.window, width=400, height=50)
        self.canvas.pack()

        self.word_text = self.canvas.create_text(200, 25, text="", font=("Helvetica", 16))

        self.entry = tk.Entry(self.window)
        self.entry.pack()

        self.answer = tk.Label(self.window, text="")
        self.answer.pack()

        self.hint = tk.Label(self.window, text="")
        self.hint.pack()

        # Difficulty level selection
        self.difficulty_var = tk.StringVar()
        self.difficulty_var.set("easy")
        self.difficulty_menu = tk.OptionMenu(self.window, self.difficulty_var, "easy", "medium", "hard", "ninja")
        self.difficulty_menu.pack()

        # Score label
        self.score_label = tk.Label(self.window, text="Score: 0")
        self.score_label.pack()

        # Create buttons
        self.new_game_button = tk.Button(self.window, text="New Game", command=self.new_game)
        self.check_button = tk.Button(self.window, text="Check", command=self.check)
        self.hint_button = tk.Button(self.window, text="Hint", command=self.show_hint)
        self.quit_button = tk.Button(self.window, text="Quit", command=self.quit_game)

        # Place buttons in the window
        self.new_game_button.pack(side=tk.LEFT)
        self.check_button.pack(side=tk.LEFT)
        self.hint_button.pack(side=tk.LEFT)
        self.quit_button.pack(side=tk.LEFT)

        # Start the game
        self.new_game()

    def choose_word(self, difficulty):
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

    def jumble_word(self, word):
        jumbled_word = list(word)
        random.shuffle(jumbled_word)
        return ''.join(jumbled_word)

    def get_hint(self, word):
        hint_length = max(1, len(word) // 2)
        hint_indices = random.sample(range(len(word)), hint_length)
        hint = ''.join(word[i] if i in hint_indices else '_' for i in range(len(word)))
        return hint

    # Tkinter GUI functions
    def new_game(self):
        difficulty = self.difficulty_var.get().lower()
        self.original_word = self.choose_word(difficulty)
        self.jumbled_word = self.jumble_word(self.original_word)
        self.canvas.itemconfig(self.word_text, text=self.jumbled_word)
        self.entry.delete(0, tk.END)
        self.answer.config(text="")
        self.hint.config(text="")
        self.score = 0
        self.update_score()

    def check(self):
        answer_text = self.entry.get().lower()
        if answer_text == self.original_word:
            self.score += 1
            self.answer.config(text="Congratulations! You guessed it correctly.")
        else:
            self.answer.config(text="Wrong! Try again.")
        self.update_score()

    def show_hint(self):
        hint_text = self.get_hint(self.original_word)
        self.hint.config(text=f"Hint: {hint_text}")
        self.score -= 0.5
        self.update_score()

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")

    def quit_game(self):
        self.window.destroy()

    def run(self):
        # Run the Tkinter event loop
        self.window.mainloop()

# Create an instance of the WordJumbleGame class and run the game
word_jumble_game = WordJumbleGame()
