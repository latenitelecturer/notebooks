# Beat the Bot
# Episode 8: look back with for

# random lets the program make choices that nobody can predict
import random

print("Rock, paper, scissors!")
print("Can code beat you?")

# A list holds several values, in order
moves = ["rock", "paper", "scissors"]

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
        # [-1] is the last item in the list: your last move
        last_move = history[-1]
        # Guess you will play it again; play the move that beats it
        if last_move == "rock":
            bot_move = "paper"
        elif last_move == "paper":
            bot_move = "scissors"
        else:
            bot_move = "rock"

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

    print("The bot played", bot_move)

    # The same move is a draw
    if player_move == bot_move:
        print("A draw!")
    # The three ways that the player can win
    elif player_move == "rock" and bot_move == "scissors":
        print("Rock breaks scissors. You win!")
        player_score = player_score + 1
    elif player_move == "paper" and bot_move == "rock":
        print("Paper covers rock. You win!")
        player_score = player_score + 1
    elif player_move == "scissors" and bot_move == "paper":
        print("Scissors cut paper. You win!")
        player_score = player_score + 1
    # Any other result means that the bot wins
    else:
        print("The bot wins!")
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

# Look back at every move you made
print("Your moves:", history)

# Count each move, one at a time
rock_count = 0
paper_count = 0
scissors_count = 0

# for repeats the indented lines once for each item in the list
for move in history:
    if move == "rock":
        rock_count = rock_count + 1
    elif move == "paper":
        paper_count = paper_count + 1
    else:
        scissors_count = scissors_count + 1

print("Rock:", rock_count)
print("Paper:", paper_count)
print("Scissors:", scissors_count)
