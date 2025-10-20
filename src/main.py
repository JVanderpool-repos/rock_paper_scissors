import argparse
from rock_paper_scissors import RockPaperScissors
from gui_game import main as gui_main

def cli_main():
    game = RockPaperScissors()
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter 'quit' to exit the game.")
    
    while True:
        choice = input("\nEnter your choice (rock/paper/scissors): ").lower()
        
        if choice == 'quit':
            print("\nThanks for playing!")
            break
            
        try:
            computer_choice, winner, score = game.play_round(choice)
            print(f"\nYou chose: {choice}")
            print(f"Computer chose: {computer_choice}")
            
            if winner == 'tie':
                print("It's a tie!")
            else:
                print(f"{winner.capitalize()} wins!")
            
            print(f"Score: {score}")
            
        except ValueError as e:
            print(f"\nError: {e}")

def main():
    parser = argparse.ArgumentParser(description='Rock Paper Scissors Game')
    parser.add_argument('--cli', action='store_true', help='Run in command-line interface mode')
    args = parser.parse_args()
    
    if args.cli:
        cli_main()
    else:
        gui_main()

if __name__ == "__main__":
    main()