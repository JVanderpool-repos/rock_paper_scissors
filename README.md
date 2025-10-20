# Rock Paper Scissors Game

A Python implementation of the classic Rock Paper Scissors game with both GUI and command-line interfaces.

## Project Structure

```
rock_paper_scissors/
│
├── src/
│   ├── rock_paper_scissors.py  # Core game logic
│   ├── gui_game.py            # GUI implementation
│   └── main.py                # Game runner
│
├── tests/
│   ├── test_rock_paper_scissors.py  # Core logic tests
│   └── test_gui_game.py            # GUI tests
│
├── assets/                    # Game images
│   ├── rock.png
│   ├── paper.png
│   ├── scissors.png
│   └── README.md             # Image guidelines
│
└── requirements.txt          # Project dependencies
```

## Features

- Play Rock Paper Scissors against the computer
- Both GUI and Command-Line interfaces
- Interactive buttons with images in GUI mode
- Score tracking
- Input validation
- Comprehensive unit tests for both interfaces
- Reset game functionality

## Requirements

- Python 3.6+
- Virtual environment (recommended)
- Dependencies listed in requirements.txt:
  - pytest: For running tests
  - Pillow: For image handling in GUI
  - typing-extensions: For enhanced type hints

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/rock_paper_scissors.git
cd rock_paper_scissors
```

2. Create and activate a virtual environment:

Windows (PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Linux/macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Verify installation:
   - Your terminal should show `(.venv)` at the start of the prompt
   - Running `pip list` should show:
     - pytest
     - Pillow
     - typing-extensions

5. Troubleshooting:
   - If you see import errors, ensure you're running from the `src` directory
   - If images don't load, check that they're properly placed in the `assets` directory
   - If GUI doesn't start, verify Pillow is installed with `pip show Pillow`

## Running the Game

### GUI Mode (Default)
```bash
cd src
python main.py
```

The GUI features:
- Visual buttons for each choice
- Real-time score display
- Game status messages
- Reset button to start a new game
- Optional custom images (see Assets Setup below)

### Command-Line Mode
```bash
cd src
python main.py --cli
```

## Assets Setup (Optional)

To use custom images in the GUI:

1. Prepare three images:
   - `rock.png`
   - `paper.png`
   - `scissors.png`

2. Requirements for images:
   - PNG format
   - Square aspect ratio (1:1)
   - Recommended size: 200x200 pixels
   - Transparent background preferred

3. Place the images in the `assets` directory

Note: If images are not provided, the GUI will use text buttons instead.

## Running Tests

To run the tests:
```bash
pytest tests/
```

## How to Play

### GUI Mode (Default)
1. Run the game with `python src/main.py`
2. Click on one of the choice buttons (rock/paper/scissors)
3. See the computer's choice and result
4. Score is automatically updated
5. Use the "Reset Game" button to start over

### CLI Mode
1. Run the game with `python src/main.py --cli`
2. Type your choice (rock/paper/scissors)
3. See the computer's choice and result
4. Score is displayed after each round
5. Type 'quit' to exit

## Game Rules

- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
- Same choices result in a tie

## Development

When making changes to the project:

1. Make sure your virtual environment is activated:
```powershell
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# Linux/macOS
source .venv/bin/activate
```

2. Your terminal should show (.venv) at the beginning of the prompt

3. After adding new dependencies:
```bash
pip freeze > requirements.txt
```