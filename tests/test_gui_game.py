import pytest
from src.gui_game import RockPaperScissorsGUI
import tkinter as tk

@pytest.fixture
def gui_app():
    root = tk.Tk()
    app = RockPaperScissorsGUI(root)
    yield app
    root.destroy()

def test_gui_initialization(gui_app):
    assert gui_app.game is not None
    assert gui_app.root.title() == "Rock Paper Scissors"
    
def test_reset_game(gui_app):
    # Make some moves
    gui_app.make_choice('rock')
    gui_app.make_choice('paper')
    
    # Reset the game
    gui_app.reset_game()
    
    # Verify score is reset
    assert gui_app.game.score == {'player': 0, 'computer': 0}
    assert gui_app.score_label['text'] == "Score - Player: 0  Computer: 0"
    
def test_make_choice(gui_app):
    # Test making a choice
    gui_app.make_choice('rock')
    
    # Verify that result label is updated
    assert gui_app.result_label['text'] != ""
    
    # Verify score label is updated
    assert "Score" in gui_app.score_label['text']