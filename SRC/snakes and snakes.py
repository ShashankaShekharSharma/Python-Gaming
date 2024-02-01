import tkinter as tk
import random

snakes_and_ladders = {
    16: 6,
    48: 26,
    49: 11,
    56: 53,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    98: 79
}

class SnakesAndLaddersGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Snakes and Ladders")
        self.num_players = 1
        self.player_positions = [0] * self.num_players
        self.create_board()
        self.create_players()
        self.create_roll_dice_button()

    def create_board(self):
        for i in range(9, -1, -1):
            for j in range(10):
                cell_value = i * 10 + j + 1
                cell_bg = "#F5F5DC"
                cell = tk.Canvas(self, width=50, height=50, borderwidth=1, relief="solid", bg=cell_bg)
                cell.grid(row=9 - i, column=j, padx=1, pady=1)
                label = tk.Label(self, text=cell_value, bg=cell_bg)
                label.grid(row=9 - i, column=j, padx=1, pady=1)



    def create_players(self):
        self.player_circles = []
        for i in range(self.num_players):
            circle = tk.Canvas(self, width=20, height=20, bg=('#ff0000', '#00ff00', '#0000ff', '#ff00ff', '#ffff00')[i % 5])
            self.player_circles.append(circle)
            circle.grid(row=9, column=0, padx=5, pady=5)

    def create_roll_dice_button(self):
        self.roll_dice_button = tk.Button(self, text="Roll Dice", command=self.roll_dice_command)
        self.roll_dice_button.grid(row=10, column=0, pady=10)

    def roll_dice_command(self):
        for i in range(self.num_players):
            print("Player", i + 1, "turn:")
            dice_roll = self.roll_dice()
            print("You rolled a", dice_roll)

            self.player_positions[i] = self.move_player(self.player_positions[i], dice_roll)
            self.player_positions[i] = self.check_snake_or_ladder(self.player_positions[i])

            print("Player", i + 1, "is now on square", self.player_positions[i])

            self.update_board()

            if self.player_positions[i] == 100:
                print("Player", i + 1, "wins!")
                self.roll_dice_button["state"] = "disabled"
                break

    def update_board(self):
        for i, circle in enumerate(self.player_circles):
            row, col = 9 - self.player_positions[i] // 10, self.player_positions[i] % 10
            circle.grid(row=row, column=col)

    def roll_dice(self):
        return random.randint(1, 6)

    def move_player(self, player_position, dice_roll):
        new_position = player_position + dice_roll
        if new_position > 100:
            new_position = 100 - (new_position - 100)
        return new_position

    def check_snake_or_ladder(self, new_position):
        if new_position in snakes_and_ladders:
            print("You landed on a " + ("ladder" if snakes_and_ladders[new_position] > new_position else "snake") + "!")
            return snakes_and_ladders[new_position]
        return new_position

if __name__ == "__main__":
    game = SnakesAndLaddersGame()
    game.mainloop()
