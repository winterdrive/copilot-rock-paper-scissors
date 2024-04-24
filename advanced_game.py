"""
This module contains a FastAPI application for a game of rock, paper, scissors, lizard, spock.
"""

import random
from fastapi import FastAPI
import uvicorn

app = FastAPI()


def determine_winner(player_choice, computer_choice):
    """
    Determines the winner of a game round.

    Args:
        player_choice (str): The player's choice. One of "rock", "paper", "scissors",
        "lizard", "spock".
        computer_choice (str): The computer's choice. One of "rock", "paper", "scissors",
        "lizard", "spock".

    Returns:
        str: The result of the game round. One of "It's a tie!", "You win!", "Computer wins!".
    """
    winning_combinations = {
        "rock": {"scissors", "lizard"},
        "paper": {"rock", "spock"},
        "scissors": {"paper", "lizard"},
        "lizard": {"paper", "spock"},
        "spock": {"rock", "scissors"}
    }

    if player_choice == computer_choice:
        return "It's a tie!"
    if computer_choice in winning_combinations[player_choice]:
        return "You win!"
    return "Computer wins!"


@app.post("/rock")
async def rock():
    """
    Endpoint for the game when player chooses "rock".

    Returns:
        dict: The result of the game round in the format {"result": result}.
    """
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    computer_choice = random.choice(choices)
    result = determine_winner("rock", computer_choice)
    return {"result": result}


def play_game():
    """
    Function to play a game round with user input.
    """
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    player_choice = input("Enter your choice (rock, paper, scissors, lizard, spock): ").lower()
    while player_choice not in choices:
        print("Invalid choice. Please try again.")
        player_choice = input("Enter your choice (rock, paper, scissors, lizard, spock): ").lower()
    computer_choice = random.choice(choices)
    print(f"Computer chooses: {computer_choice}")
    print(determine_winner(player_choice, computer_choice))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
