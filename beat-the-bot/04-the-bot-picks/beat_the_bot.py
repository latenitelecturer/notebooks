# Beat the Bot
# Episode 4: the bot picks at random

# random lets the program make choices that nobody can predict
import random

print("Rock, paper, scissors!")
print("Can code beat you?")

# A list holds several values, in order
moves = ["rock", "paper", "scissors"]

# The bot picks one move from the list, at random
bot_move = random.choice(moves)

# input() shows a question, waits, and gives back what you type
player_move = input("Your move: ")

print("You played", player_move)
print("The bot played", bot_move)

# The same move is a draw
if player_move == bot_move:
    print("A draw!")
# The three ways that the player can win
elif player_move == "rock" and bot_move == "scissors":
    print("Rock breaks scissors. You win!")
elif player_move == "paper" and bot_move == "rock":
    print("Paper covers rock. You win!")
elif player_move == "scissors" and bot_move == "paper":
    print("Scissors cut paper. You win!")
# Any other result means that the bot wins
else:
    print("The bot wins!")
