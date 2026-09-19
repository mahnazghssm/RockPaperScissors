import random
from typing import List


class RockPaperScissors:
    def __init__(self, name: str):
        self.name: str = name
        self.choices: List[str] = ["rock", "paper", "scissors"]

    def user_choice(self) -> str:
        user_input = input(
            f"Dear {self.name}, please choose from {self.choices}: "
        )

        if user_input.lower() in self.choices:
            return user_input.lower()

        print(f"Invalid input. Please choose from {self.choices}")
        return self.user_choice()

    def computer_choice(self) -> str:
        computer_input = random.choice(self.choices)
        return computer_input

    def winner_roles(
        self, user_input: str, computer_input: str
    ) -> str:
        if user_input == computer_input:
            return "It is a tie!"

        winner_competition: List[tuple[str, str]] = [
            ("rock", "scissors"),
            ("paper", "rock"),
            ("scissors", "paper")
        ]

        for win in winner_competition:
            if user_input == win[0] and computer_input == win[1]:
                return "Congratulations! You won!"

        return "Oh no! Computer won"


    def play(self):
        user_choice = self.user_choice()
        computer_choice = self.computer_choice()

        print(f"Computer: {computer_choice}")
        print(self.winner_roles(user_choice, computer_choice))


if __name__ == "__main__":
    game = RockPaperScissors("mahnaz")

    while True:
        game.play()

        continue_game = input(
            "Do you want to play again? "
            "(Enter any key to play again, or q to exit): "
        )

        if continue_game.lower() == "q":
            print("Goodbye!")
            break
