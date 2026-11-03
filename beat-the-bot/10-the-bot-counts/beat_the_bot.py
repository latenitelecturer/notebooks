# Beat the Bot
# Episode 10: the bot counts your habits

# random lets the program make choices that nobody can predict
import random

print("Rock, paper, scissors!")
print("Can code beat you?")

# A list holds several values, in order
moves = ["rock", "paper", "scissors"]

# A dictionary links each key to a value:
# here, each move to the move that beats it
what_beats = {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock",
}

# A second dictionary: how many times you have played each move
counts = {
    "rock": 0,
    "paper": 0,
    "scissors": 0,
}

# Both scores start at zero
player_score = 0
bot_score = 0

# An empty list. The bot writes down every move you make here.
history = []

# How many rounds to play, and how many we have played so far
total_rounds = 10
round_number = 0

# Repeat the indented lines while there are rounds left to play
while round_number < total_rounds:
    round_number = round_number + 1
    print()
    print("Round", round_number)

    # len() counts the items in a list
    moves_seen = len(history)

    # The bot chooses before you type, so it cannot cheat
    if moves_seen == 0:
        # Nothing to remember yet, so pick at random
        bot_move = random.choice(moves)
    else:
        # Find your favourite move so far
        favourite = "rock"
        for option in moves:
            if counts[option] > counts[favourite]:
                favourite = option
        # Play the move that beats your favourite
        bot_move = what_beats[favourite]

    # Ask for a move, then tidy the answer
    answer = input("Your move: ")
    # strip() removes spaces from the start and the end
    trimmed = answer.strip()
    # lower() makes every letter small, so "Rock" becomes "rock"
    player_move = trimmed.lower()

    # Ask again until the answer is one of the moves in the list
    while player_move not in moves:
        print("Please type rock, paper or scissors.")
        answer = input("Your move: ")
        trimmed = answer.strip()
        player_move = trimmed.lower()

    # append() adds your move to the end of the list
    history.append(player_move)
    # Add one to the count for this move
    counts[player_move] = counts[player_move] + 1

    print("The bot played", bot_move)

    # The move that would beat the bot's move
    beats_bot = what_beats[bot_move]

    if player_move == bot_move:
        print("A draw!")
    elif player_move == beats_bot:
        print(player_move, "beats", bot_move, "- you win!")
        player_score = player_score + 1
    else:
        print(bot_move, "beats", player_move, "- the bot wins!")
        bot_score = bot_score + 1

    print("Score: you", player_score, "bot", bot_score)

# The loop has finished, so the game is over
print()
print("Final score: you", player_score, "bot", bot_score)

if player_score > bot_score:
    print("You beat the bot!")
elif bot_score > player_score:
    print("The bot beat you.")
else:
    print("It is a tie.")

# Look back at every move you made, and at your habits
print("Your moves:", history)
print("Your habits:", counts)
