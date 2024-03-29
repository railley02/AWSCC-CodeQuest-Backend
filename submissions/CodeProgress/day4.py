print("Choose between rock, paper, and scissors")

player1 = input("Player 1: ")
player2 = input("Player 2: ")


if player1 == "rock" and player2 == "scissors":
    print("Player 1 wins the game")
elif player1 == "scissors" and player2 == "paper":
    print("Player 1 wins the game")
elif player1 == "paper" and player2 == "rock":
    print("Player 1 wins the game")
elif player1 == player2:
    print("It's a tie!")
else:
    print("Player 2 wins the game")