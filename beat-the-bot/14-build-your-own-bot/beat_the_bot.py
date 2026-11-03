# Beat the Bot
# Episode 14: build your own bot

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


# Every bot is a function: your moves in, its move out
def random_bot(history):
    # Ignore the history and pick at random
    bot_move = random.choice(moves)
    return bot_move


def habit_bot(history):
    moves_seen = len(history)
    # Nothing to remember yet, so pick at random
    if moves_seen == 0:
        bot_move = random.choice(moves)
        return bot_move
    counts = count_moves(history)
    # Find your favourite move so far
    favourite = "rock"
    for option in moves:
        if counts[option] > counts[favourite]:
            favourite = option
    # Play the move that beats your favourite
    bot_move = what_beats[favourite]
    return bot_move


def pattern_bot(history):
    moves_seen = len(history)
    # It needs at least two moves to see a pattern
    if moves_seen < 2:
        bot_move = random.choice(moves)
        return bot_move
    # Count the pairs of moves you played, like "rock then paper"
    pair_counts = {}
    previous = history[0]
    # [1:] means every move except the first
    for move in history[1:]:
        pair = previous + " then " + move
        # get() gives the count so far, or 0 if the pair is new
        seen = pair_counts.get(pair, 0)
        pair_counts[pair] = seen + 1
        previous = move
    # Your last move
    last_move = history[-1]
    # Which move usually comes after it? Start by guessing a repeat.
    prediction = last_move
    best_count = 0
    for option in moves:
        pair = last_move + " then " + option
        seen = pair_counts.get(pair, 0)
        if seen > best_count:
            best_count = seen
            prediction = option
    # Play the move that beats the prediction
    bot_move = what_beats[prediction]
    return bot_move


def my_bot(history):
    # Your bot. Change these lines to give it your own plan.
    # It gets the list of the player's moves.
    # It must return "rock", "paper" or "scissors".
    moves_seen = len(history)
    if moves_seen == 0:
        bot_move = "paper"
        return bot_move
    # A starting plan: copy the player's last move
    bot_move = history[-1]
    return bot_move


# The game starts here
print("Rock, paper, scissors!")
print("Can code beat you?")

# Each number on the menu links to one bot
bots = {
    "1": random_bot,
    "2": habit_bot,
    "3": pattern_bot,
    "4": my_bot,
}

print("Choose your opponent:")
print("1  random bot")
print("2  habit bot")
print("3  pattern bot")
print("4  my bot")

# Ask again until the answer is a number on the menu
choice = input("Opponent number: ")
while choice not in bots:
    print("Please type 1, 2, 3 or 4.")
    choice = input("Opponent number: ")

bot = bots[choice]

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

    # The bot chooses before you type, so it cannot cheat
    bot_move = bot(history)
    player_move = ask_for_move()
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

# Your win rate: the share of rounds that you won, as a percentage
win_share = player_score / total_rounds
win_rate = win_share * 100
win_rate_rounded = round(win_rate)
print("You won", win_rate_rounded, "percent of the rounds.")

# Look back at every move you made, and at your habits
habits = count_moves(history)
print("Your moves:", history)
print("Your habits:", habits)
