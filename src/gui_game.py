import tkinter as tk
from tkinter import ttk
from pathlib import Path
from PIL import Image, ImageTk
import os

from rock_paper_scissors import RockPaperScissors

class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        
        self.game = RockPaperScissors()
        
        # Load images
        self.images = self.load_images()
        
        self.setup_ui()
        
    def load_images(self):
        """Load and resize game images."""
        image_dir = Path(__file__).parent.parent / "assets"
        images = {}
        for choice in ['rock', 'paper', 'scissors']:
            img_path = image_dir / f"{choice}.png"
            if img_path.exists():
                img = Image.open(img_path)
                img = img.resize((100, 100), Image.Resampling.LANCZOS)
                images[choice] = ImageTk.PhotoImage(img)
            else:
                # Fallback text if images are not found
                images[choice] = None
        return images
        
    def setup_ui(self):
        """Set up the game's user interface."""
        # Title
        title = ttk.Label(self.root, text="Rock Paper Scissors", font=('Arial', 24))
        title.pack(pady=20)
        
        # Score display
        self.score_label = ttk.Label(self.root, text="Score - Player: 0  Computer: 0", font=('Arial', 14))
        self.score_label.pack()
        
        # Game status
        self.status_label = ttk.Label(self.root, text="Choose your move!", font=('Arial', 12))
        self.status_label.pack(pady=10)
        
        # Choices frame
        choices_frame = ttk.Frame(self.root)
        choices_frame.pack(pady=20)
        
        # Add choice buttons
        for choice in ['rock', 'paper', 'scissors']:
            btn_frame = ttk.Frame(choices_frame)
            btn_frame.pack(side=tk.LEFT, padx=10)
            
            if self.images.get(choice):
                btn = ttk.Button(btn_frame, image=self.images[choice], 
                               command=lambda c=choice: self.make_choice(c))
            else:
                btn = ttk.Button(btn_frame, text=choice.capitalize(),
                               command=lambda c=choice: self.make_choice(c))
            btn.pack()
            ttk.Label(btn_frame, text=choice.capitalize()).pack()
        
        # Result display
        self.result_label = ttk.Label(self.root, text="", font=('Arial', 12))
        self.result_label.pack(pady=10)
        
        # Reset button
        ttk.Button(self.root, text="Reset Game", command=self.reset_game).pack(pady=10)
        
    def make_choice(self, player_choice):
        """Handle player's choice and update the game state."""
        computer_choice, winner, score = self.game.play_round(player_choice)
        
        # Update status
        result_text = f"You chose {player_choice}\nComputer chose {computer_choice}\n"
        if winner == 'tie':
            result_text += "It's a tie!"
        else:
            result_text += f"{winner.capitalize()} wins!"
        
        self.result_label.config(text=result_text)
        self.score_label.config(text=f"Score - {score}")
        
    def reset_game(self):
        """Reset the game state."""
        self.game.reset_score()
        self.score_label.config(text="Score - Player: 0  Computer: 0")
        self.result_label.config(text="")
        self.status_label.config(text="Choose your move!")

def main():
    root = tk.Tk()
    app = RockPaperScissorsGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()