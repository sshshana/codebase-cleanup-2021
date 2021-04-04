
from random import choice

#
# USER SELECTION
#

valid_options = ["rock", "paper", "scissors"]


def determine_winner(pl1 ,pl2):
    wins = [("rock","scissors"),("scissors","paper"),("paper","rock")]
    if (pl1, pl2) in wins:
        return "The user wins"
    elif pl1 == pl2:
        return "It's a tie!"
    else:
        return "The computer wins"


if __name__ == '__main__':
    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in valid_options:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    c = choice(valid_options)
    print("COMPUTER CHOICE:", c)

    #
    # DETERMINATION OF WINNER
    #

    # if u == "rock" and c == "rock":
    #     print("It's a tie!")
    # elif u == "rock" and c == "paper":
    #     print("The computer wins")
    # elif u == "rock" and c == "scissors":
    #     print("The user wins")
    # 
    # elif u == "paper" and c == "rock":
    #     print("The computer wins")
    # elif u == "paper" and c == "paper":
    #     print("It's a tie!")
    # elif u == "paper" and c == "scissors":
    #     print("The user wins")
    # 
    # elif u == "scissors" and c == "rock":
    #     print("The computer wins")
    # elif u == "scissors" and c == "paper":
    #     print("The user wins")
    # elif u == "scissors" and c == "scissors":
    #     print("It's a tie!")

    wins = [("rock","scissors"),("scissors","paper"),("paper","rock")]
    if (u, c) in wins:
        print("The user wins")
    elif u == c:
        print("It's a tie!")
    else:
        print("The computer wins")