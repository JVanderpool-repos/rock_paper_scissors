# Rock Paper Scissors Game

A simple command-line implementation of the classic Rock Paper Scissors game in Python.

## Project Structure

```
rock_paper_scissors/
│
├── src/
│   ├── rock_paper_scissors.py  # Core game logic
│   └── main.py                 # Game runner
│
├── tests/
│   └── test_rock_paper_scissors.py  # Unit tests
│
└── requirements.txt            # Project dependencies
```

## Features

- Play Rock Paper Scissors against the computer
- Score tracking
- Input validation
- Unit tests

## Requirements

- Python 3.6+
- Virtual environment (recommended)
- Dependencies listed in requirements.txt

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

## Running the Game

To start the game, run:
```bash
python src/main.py
```

## Running Tests

To run the tests:
```bash
pytest tests/
```

## How to Play

1. Run the game
2. Enter your choice (rock/paper/scissors)
3. See the result and updated score
4. Keep playing or type 'quit' to exit

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