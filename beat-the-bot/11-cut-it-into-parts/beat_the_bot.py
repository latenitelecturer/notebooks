# Beat the Bot
# Episode 11: cut it into parts

# random lets the program make choices that nobody can predict
import random

# A list holds several values, in order
moves = ["rock", "paper", "scissors"]

# A dictionary links each key to a value:
# here, each move to the move that beats it
what_beats = {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock",
}


# def makes a function: a named set of steps that you can use again
def ask_for_move():
    # Ask for a move, then tidy the answer
    answer = input("Your move: ")
    trimmed = answer.strip()
    move = trimmed.lower()
    # Ask again until the answer is one of the moves in the list
    while move not in moves:
        print("Please type rock, paper or scissors.")
        answer = input("Your move: ")
        trimmed = answer.strip()
        move = trimmed.lower()
    # return gives the answer back to the line that called it
    return move


def count_moves(history):
    # How many times the player has played each move
    counts = {
        "rock": 0,
        "paper": 0,
        "scissors": 0,
    }
    for move in history:
        counts[move] = counts[move] + 1
    return counts


def winner(player_move, bot_move):
    # Who won the round: "draw", "player" or "bot"
    if player_move == bot_move:
        return "draw"
    beats_bot = what_beats[bot_move]
    if player_move == beats_bot:
        return "player"
    return "bot"


# The game starts here
print("Rock, paper, scissors!")
print("Can code beat you?")

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
        counts = count_moves(history)
        # Find your favourite move so far
        favourite = "rock"
        for option in moves:
            if counts[option] > counts[favourite]:
                favourite = option
        # Play the move that beats your favourite
        bot_move = what_beats[favourite]

    player_move = ask_for_move()
    # append() adds your move to the end of the list
    history.append(player_move)

    print("The bot played", bot_move)

    result = winner(player_move, bot_move)
    if result == "draw":
        print("A draw!")
    elif result == "player":
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
habits = count_moves(history)
print("Your moves:", history)
print("Your habits:", habits)
