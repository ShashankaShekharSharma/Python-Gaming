import tkinter as tk
from tkinter import messagebox
import random
import time

class StonePaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Stone Paper Scissors")
        self.root.geometry("300x200")

        self.label_intro = tk.Label(self.root, text="Stone Paper Scissors Game")
        self.label_intro.pack(pady=10)

        self.button_stone = tk.Button(self.root, text="Stone", command=lambda: self.play("Stone"))
        self.button_stone.pack(pady=5)

        self.button_paper = tk.Button(self.root, text="Paper", command=lambda: self.play("Paper"))
        self.button_paper.pack(pady=5)

        self.button_scissors = tk.Button(self.root, text="Scissors", command=lambda: self.play("Scissors"))
        self.button_scissors.pack(pady=5)

    def play(self, user_choice):
        self.label_intro.config(text="Computer's choice is: ")
        self.root.update()
        time.sleep(1)

        computer_choices = ['Stone', 'Paper', 'Scissors']
        computer_choice = random.choice(computer_choices)

        self.label_intro.config(text=f"Computer's choice is: {computer_choice}")
        self.root.update()
        time.sleep(1)

        result = self.determine_winner(user_choice, computer_choice)
        messagebox.showinfo("Result", result)

    def determine_winner(self, user_choice, computer_choice):
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
    root = tk.Tk()
    game = StonePaperScissorsGUI(root)
    root.mainloop()
