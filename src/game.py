"""
Author: Mahnaz Ghassemi
Date created: 07,07,2024
Description: Rock Paper Scissors game
"""

import random
from typing import List


class RockpaperScissors:
    """Main class for Rock Paper Scissors game."""
    def __init__(self, name: str):
        self.name: str = name
        self.choices: List[str] = ["rock", "paper", "scissors"]

    def user_choice(self) -> str:
        while True:
            user_input: str = input(f"Dear {self.name}, please choose from {self.choices}: ").lower()
            if user_input in self.choices:
                return user_input
            print(f"Invalid input. Please choose from {self.choices}")

    def computer_choice(self) -> str:
        """Get computer choice randomly from choices: Rock, Paper, Scissors."""
        return random.choice(self.choices)

    def winner_roles(self, user_input: str, computer_input: str) -> str:
        """Decide the winner of the game based on user and computer choices."""
        if user_input == computer_input:
            return "It's a tie!"

        winner_combinations: List[tuple[str, str]] = [
            ("rock", "scissors"),
            ("paper", "rock"),
            ("scissors", "paper")
        ]
        for win in winner_combinations:
            if (user_input == win[0]) and (computer_input == win[1]):
                return "Congratulations! You won!"

        return "Oh no! The computer won!"

    def play(self):
        """Play the game."""
        user_pick = self.user_choice()
        computer_pick = self.computer_choice()
        print(f"Computer: {computer_pick}")
        print(self.winner_roles(user_pick, computer_pick))


if __name__ == "__main__":
    game = RockpaperScissors("Mahnaz")
    while True:
        game.play()
        continue_game = input("Do you want to play again? (Enter any key to continue, 'q' to quit): ")
        if continue_game.lower() == "q":
            print("Goodbye!")
            break
