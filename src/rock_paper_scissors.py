import random
from typing import Tuple, Literal

class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.score = {'player': 0, 'computer': 0}
    
    def get_computer_choice(self) -> str:
        """Get a random choice for the computer."""
        return random.choice(self.choices)
    
    def get_winner(self, player_choice: str, computer_choice: str) -> Literal['player', 'computer', 'tie']:
        """Determine the winner of the round."""
        if player_choice == computer_choice:
            return 'tie'
        
        winning_combinations = {
            'rock': 'scissors',
            'paper': 'rock',
            'scissors': 'paper'
        }
        
        if winning_combinations[player_choice] == computer_choice:
            return 'player'
        return 'computer'
    
    def play_round(self, player_choice: str) -> Tuple[str, str, str]:
        """Play a single round of the game."""
        player_choice = player_choice.lower()
        if player_choice not in self.choices:
            raise ValueError("Invalid choice! Please choose rock, paper, or scissors.")
        
        computer_choice = self.get_computer_choice()
        winner = self.get_winner(player_choice, computer_choice)
        
        if winner != 'tie':
            self.score[winner] += 1
            
        return computer_choice, winner, f"Player: {self.score['player']} - Computer: {self.score['computer']}"
    
    def reset_score(self):
        """Reset the game score."""
        self.score = {'player': 0, 'computer': 0}