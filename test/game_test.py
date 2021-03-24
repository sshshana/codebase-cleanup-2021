

from app.game import determine_winner

def test_determination_of_the_winner():
    assert determine_winner("rock", "rock") == "It's a tie!"
    assert determine_winner("rock", "paper") == "The computer wins"
    assert determine_winner("rock", "scissors") == "The user wins"

    assert determine_winner("paper", "rock") == "The user wins"
    assert determine_winner("paper", "paper") == "It's a tie!"
    assert determine_winner("paper", "scissors") == "The computer wins"

    assert determine_winner("scissors", "rock") == "The computer wins"
    assert determine_winner("scissors", "paper") == "The user wins"
    assert determine_winner("scissors", "scissors") == "It's a tie!"