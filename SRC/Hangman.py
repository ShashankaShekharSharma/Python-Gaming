import tkinter as tk
from tkinter import simpledialog
import random

class HangmanGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hangman Game")

        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        self.word_label = tk.Label(self.root, text="Word: ")
        self.word_label.pack()

        self.hangman_parts = [
            self.canvas.create_oval(170, 100, 230, 160, width=2, state=tk.HIDDEN),  # Head
            self.canvas.create_line(200, 160, 200, 280, width=2, state=tk.HIDDEN),  # Body
            self.canvas.create_line(200, 200, 170, 230, width=2, state=tk.HIDDEN),  # Left arm
            self.canvas.create_line(200, 200, 230, 230, width=2, state=tk.HIDDEN),  # Right arm
            self.canvas.create_line(200, 280, 170, 320, width=2, state=tk.HIDDEN),  # Left leg
            self.canvas.create_line(200, 280, 230, 320, width=2, state=tk.HIDDEN)   # Right leg
        ]

        self.play_hangman()

    def get_word(self):
        words = ["python", "bhailang", "coder", "frontend", "backend", "fullstack", "hardware", "software",
                 "internet", "intranet", "email", "facebook", "instagram", "cybersecurity", "blockchain",
                 "cryptocurrency", "bitcoin", "ethereum", "metaverse", "motherboard", "bluetooth", "monitor",
                 "javascript", "computer", "programming", "software", "julia", "ruby", "algorithm", "bandwidth",
                 "encryption", "joystick", "keyboard", "mouse", "phone", "object", "network", "robot", "software",
                 "terminal", "cloud", "latency", "viewport", "github"]
        return random.choice(words).upper()

    def display_word(self, word, used_letters):
        word_display = " ".join([letter if letter in used_letters else "-" for letter in word])
        self.word_label.config(text=f"Word: {word_display}")

    def play_hangman(self):
        word = self.get_word()
        word_letters = set(word)
        alphabet = set(chr(i) for i in range(65, 91))
        used_letters = set()

        lives = 6

        while len(word_letters) > 0 and lives > 0:
            self.display_word(word, used_letters)

            user_letter = self.get_user_input(alphabet - used_letters)
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                self.draw_next_hangman_part(lives)

        self.display_word(word, word_letters)  # Display the remaining letters in the word
        self.show_game_result(lives, word)

    def get_user_input(self, available_letters):
        user_letter = simpledialog.askstring("Hangman", f"Available letters: {' '.join(available_letters)}\nGuess a letter:")
        return user_letter.upper() if user_letter else ""

    def draw_next_hangman_part(self, lives):
        if lives <= 6:
            self.canvas.itemconfig(self.hangman_parts[5 - lives], state=tk.NORMAL)

    def show_game_result(self, lives, word):
        if lives == 0:
            self.word_label.config(text=f"Game Over! The word was {word}")
        else:
            self.word_label.config(text=f"You won! The word was {word}")

        play_again = simpledialog.askinteger("Hangman", "Do you want to play again? (1 for Yes, 0 for No)", minvalue=0, maxvalue=1)

        if play_again:
            self.reset_hangman()
            self.play_hangman()
        else:
            self.root.destroy()

    def reset_hangman(self):
        for part in self.hangman_parts:
            self.canvas.itemconfig(part, state=tk.HIDDEN)

if __name__ == "__main__":
    hangman_gui = HangmanGUI()
    hangman_gui.root.mainloop()
