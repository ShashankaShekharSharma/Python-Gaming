import random

class SnakesAndLaddersGame:
    def __init__(self, num_players):
        self.num_players = num_players
        self.player_positions = [0] * num_players

    def roll_dice(self):
        return random.randint(1, 6)

    def move_player(self, player_index, dice_roll):
        new_position = self.player_positions[player_index] + dice_roll
        if new_position > 100:
            new_position = 100 - (new_position - 100)
        return new_position

    def check_snake_or_ladder(self, new_position):
        if new_position in self.snakes_and_ladders:
            print("You landed on a " + ("ladder" if self.snakes_and_ladders[new_position] > new_position else "snake") + "!")
            return self.snakes_and_ladders[new_position]
        return new_position

    def play_turn(self, player_index):
        print("Player", player_index + 1, "turn:")
        input("Press Enter to roll the dice...")
        dice_roll = self.roll_dice()
        print("You rolled a", dice_roll)

        self.player_positions[player_index] = self.move_player(player_index, dice_roll)
        self.player_positions[player_index] = self.check_snake_or_ladder(self.player_positions[player_index])

        print("Player", player_index + 1, "is now on square", self.player_positions[player_index])

        if self.player_positions[player_index] == 100:
            print("Player", player_index + 1, "wins!")
            return True

        return False

    def play_game(self):
        while True:
            for i in range(self.num_players):
                if self.play_turn(i):
                    return

if __name__ == "__main__":
    num_players = int(input("Enter the number of players: "))
    snakes_and_ladders_game = SnakesAndLaddersGame(num_players)
    snakes_and_ladders_game.play_game()
