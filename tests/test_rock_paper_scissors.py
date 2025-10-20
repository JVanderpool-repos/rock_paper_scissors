import pytest
from src.rock_paper_scissors import RockPaperScissors

def test_game_initialization():
    game = RockPaperScissors()
    assert game.choices == ['rock', 'paper', 'scissors']
    assert game.score == {'player': 0, 'computer': 0}

def test_computer_choice():
    game = RockPaperScissors()
    choice = game.get_computer_choice()
    assert choice in game.choices

def test_winner_determination():
    game = RockPaperScissors()
    # Test ties
    assert game.get_winner('rock', 'rock') == 'tie'
    assert game.get_winner('paper', 'paper') == 'tie'
    assert game.get_winner('scissors', 'scissors') == 'tie'
    
    # Test winning combinations
    assert game.get_winner('rock', 'scissors') == 'player'
    assert game.get_winner('paper', 'rock') == 'player'
    assert game.get_winner('scissors', 'paper') == 'player'
    
    # Test losing combinations
    assert game.get_winner('rock', 'paper') == 'computer'
    assert game.get_winner('paper', 'scissors') == 'computer'
    assert game.get_winner('scissors', 'rock') == 'computer'

def test_play_round():
    game = RockPaperScissors()
    # Test valid input
    computer_choice, winner, score = game.play_round('rock')
    assert computer_choice in game.choices
    assert winner in ['player', 'computer', 'tie']
    assert isinstance(score, str)
    
    # Test invalid input
    with pytest.raises(ValueError):
        game.play_round('invalid')

def test_score_tracking():
    game = RockPaperScissors()
    initial_score = game.score.copy()
    
    # Play multiple rounds and verify score updates
    game.play_round('rock')
    assert game.score != initial_score
    
    # Test score reset
    game.reset_score()
    assert game.score == initial_score