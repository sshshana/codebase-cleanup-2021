
from random import choice

#
# USER SELECTION
#

valid_options = ["rock", "paper", "scissors"]


def determine_winner(pl1 ,pl2):
    """
    Parameters:
        pl1 and pl2 are both strings: one of "rock", "paper", and "scissors"
    """
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
    
    #
    # INPUT VALIDATION
    #

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
    
    print(determine_winner(u, c))