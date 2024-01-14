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
def roll_dice():
    return random.randint(1, 6)

def move_player(player_position, dice_roll):
    new_position = player_position + dice_roll
    if new_position > 100:
        new_position = 100 - (new_position - 100)
    return new_position

def check_snake_or_ladder(new_position):
    if new_position in snakes_and_ladders:
        print("You landed on a " + ("ladder" if snakes_and_ladders[new_position] > new_position else "snake") + "!")
        return snakes_and_ladders[new_position]
    return new_position

def play_game(num_players):
    player_positions = [0] * num_players
    while True:
        for i in range(num_players):
            print("Player", i+1, "turn:")
            input("Press Enter to roll the dice...")
            dice_roll = roll_dice()
            print("You rolled a", dice_roll)

            player_positions[i] = move_player(player_positions[i], dice_roll)
            player_positions[i] = check_snake_or_ladder(player_positions[i])

            print("Player", i+1, "is now on square", player_positions[i])

            if player_positions[i] == 100:
                print("Player", i+1, "wins!")
                return
num_players = int(input("Enter the number of players: "))
play_game(num_players)

