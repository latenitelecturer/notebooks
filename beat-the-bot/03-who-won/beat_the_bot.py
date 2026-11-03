# Beat the Bot
# Episode 3: who won?

print("Rock, paper, scissors!")
print("Can code beat you?")

# The bot's move. For now, it never changes.
bot_move = "rock"

# input() shows a question, waits, and gives back what you type
player_move = input("Your move: ")

print("You played", player_move)
print("The bot played", bot_move)

# The bot always plays rock, so only a few results are possible
# == asks "are these the same?"
if player_move == bot_move:
    print("A draw!")
elif player_move == "paper":
    print("Paper covers rock. You win!")
elif player_move == "scissors":
    print("Rock breaks scissors. The bot wins!")
else:
    print("That is not a move I know.")
