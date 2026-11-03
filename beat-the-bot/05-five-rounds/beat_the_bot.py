# Beat the Bot
# Episode 5: five rounds and a scoreboard

# random lets the program make choices that nobody can predict
import random

print("Rock, paper, scissors!")
print("Can code beat you?")

# A list holds several values, in order
moves = ["rock", "paper", "scissors"]

# Both scores start at zero
player_score = 0
bot_score = 0

# How many rounds to play, and how many we have played so far
total_rounds = 5
round_number = 0

# Repeat the indented lines while there are rounds left to play
while round_number < total_rounds:
    round_number = round_number + 1
    print()
    print("Round", round_number)

    # The bot picks one move from the list, at random
    bot_move = random.choice(moves)

    player_move = input("Your move: ")
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
