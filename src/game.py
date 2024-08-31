"""
Author: Mahnaz Ghassemi
Date created: 07,07,2024
Description: Rock Paper Scissors game
"""

import random
from typing import List


class RockpaperScissors:
    """main class for Rock Paper Scissors game."""
    def __init__(self, name: str):
        self.name: str = name
        self.choices: List[str] = ["rock", "paper", "scissors"]

    def user_choice(self) -> str:
        user_input: str = input(f"Dear {self.name} please choose from {self.choices}")
        if user_input.lower() in self.choices:
            return user_input.lower()
        
        print (f"Invalid input. please chooose from {self.choices}")
        return self.user_choice()
    
    def computer_choice (self) -> str:
        """Get computer choice randomly from choices: Rock , Paper, Scissors."""
        computer_input = random.choice(self.choices)
        return computer_input
    
    def winner_roles (self, user_input: str , computer_input: str) -> str:
        """Decide the winner of the game based on user and computer choices.

        :param user_input: The choice of the user
        :param computer_input: The choice of the computer
        :return: the result of the game. (who won)
        """
        if user_input == computer_input:
            return "it is a tie!"
        
        winner_competition: List[tuple[str, str]] = [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")]
        for win in winner_competition:
            if (user_input == win[0]) & (computer_input == win[1]):
                return "Congradualtions! You won!"

        return "Oh no! Computer won"
    
    def play(self):
        """play the game.
        - Get user choice.
        - Get computer choice.
        - Decide the winner
        - print the result.
        """
        user_choice = self.user_choice()
        computer_choice = self.computer_choice()
        print(f"computer:{computer_choice}")
        print(self.winner_roles(user_choice, computer_choice))


if __name__ == "__main__":
    game = RockpaperScissors("mahnaz")

while True:
    #play again
    game.play()

    continue_game = input("Do you want to play it again? (Enter any key to play again, Enter q to exit)")
    if continue_game.lower() == "q":
        print("Goodbye!")
        break
