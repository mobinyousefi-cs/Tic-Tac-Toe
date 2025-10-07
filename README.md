# Tic Tac Toe (pygame)

A polished, pygame-based **Tic Tac Toe** with **Human vs Human** and **Human vs AI (minimax)** modes.  
Clean architecture: game logic isolated from rendering; fully tested board logic.

## Features
- 3×3 board, win/draw detection
- Human vs Human / Human vs AI (toggle with `M`)
- Restart anytime (`R`)
- Minimal, responsive UI (pygame)
- `src/` layout, tests, CI, Ruff + Black

## Quickstart

```bash
# (Recommended) create a venv
python -m venv .venv && . .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install
pip install -e ".[dev]"

# Run
python -m tictactoe
# or
tictactoe
