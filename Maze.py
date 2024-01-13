import random
import tkinter as tk
from tkinter import simpledialog, messagebox

class WordJumbleGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Word Jumbles")

        self.difficulty_label = tk.Label(master, text="Choose a difficulty level:")
        self.difficulty_label.pack()

        self.difficulty_var = tk.StringVar()
        self.difficulty_entry = tk.Entry(master, textvariable=self.difficulty_var)
        self.difficulty_entry.pack()

        self.start_button = tk.Button(master, text="Start Game", command=self.start_game)
        self.start_button.pack()

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

    def play_game(self, original_word, jumbled_word):
        self.difficulty_label.pack_forget()
        self.difficulty_entry.pack_forget()
        self.start_button.pack_forget()

        self.jumbled_word_label = tk.Label(self.master, text="Jumbled Word: " + jumbled_word)
        self.jumbled_word_label.pack()

        attempts = 3
        while attempts > 0:
            guess = simpledialog.askstring("Word Jumbles", f"Your guess (or type 'hint' for a hint):").lower()

            if guess == original_word:
                messagebox.showinfo("Word Jumbles", "Congratulations! You guessed it correctly.")
                break
            elif guess == "hint":
                hint = self.get_hint(original_word)
                messagebox.showinfo("Word Jumbles", "Hint: " + hint)
            else:
                attempts -= 1
                if attempts > 0:
                    messagebox.showwarning("Word Jumbles", f"Wrong! Try again. {attempts} {'attempts' if attempts > 1 else 'attempt'} left.")
                else:
                    messagebox.showinfo("Word Jumbles", f"Sorry, you're out of attempts. The correct word was: {original_word}")

        play_again = messagebox.askyesno("Word Jumbles", "Do you want to play again?")
        if play_again:
            self.jumbled_word_label.pack_forget()
            self.start_game()
        else:
            messagebox.showinfo("Word Jumbles", "Thanks for playing! Goodbye!")
            self.master.destroy()

    def start_game(self):
        difficulty = self.difficulty_var.get().lower()
        original_word = self.choose_word(difficulty)
        jumbled_word = self.jumble_word(original_word)
        self.play_game(original_word, jumbled_word)

if __name__ == "__main__":
    root = tk.Tk()
    game = WordJumbleGame(root)
    root.mainloop()
