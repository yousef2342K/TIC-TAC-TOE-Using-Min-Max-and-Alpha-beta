Here’s a `README.md` file tailored for your Tic-Tac-Toe project that uses the Min-Max and Alpha-Beta algorithms:

---

# Tic-Tac-Toe Using Min-Max and Alpha-Beta Pruning

## Overview

This project implements the classic **Tic-Tac-Toe** game with two AI strategies:  
- **Min-Max Algorithm**: A brute-force strategy to determine the best move.  
- **Alpha-Beta Pruning**: An optimized version of Min-Max that reduces unnecessary computations.

The game allows you to play against the AI or observe the AI competing against itself.

---

## Features

1. **Min-Max Algorithm**  
   The AI evaluates all possible moves to determine the optimal choice, ensuring it never loses.

2. **Alpha-Beta Pruning**  
   An optimized version of the Min-Max algorithm that improves performance by pruning unneeded branches.

3. **Human vs AI**  
   Play the game as a human player against the AI.

4. **AI vs AI**  
   Watch the AI algorithms play against each other to observe their decision-making process.

5. **Command-Line Interface (CLI)**  
   A simple and user-friendly CLI to interact with the game.

---

## How It Works

### Min-Max Algorithm
The Min-Max algorithm recursively explores all possible moves and assigns scores to the game states:
- **+10** for a win (AI victory).
- **-10** for a loss (human victory).
- **0** for a draw.

The AI selects the move that maximizes its score while minimizing the opponent's score.

### Alpha-Beta Pruning
Alpha-Beta pruning improves the Min-Max algorithm by:
- **Skipping unnecessary branches** that do not affect the outcome.
- Reducing computation time while still guaranteeing the optimal move.

---

## Requirements

- Python 3.x

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yousef2342K/TIC-TAC-TOE-Using-Min-Max-and-Alpha-beta.git
   cd TIC-TAC-TOE-Using-Min-Max-and-Alpha-beta
   ```

2. Run the script:
   ```bash
   python3 main.py
   ```

---

## Game Modes

1. **Human vs AI**:  
   - You play as 'X' or 'O'.  
   - The AI uses either the Min-Max or Alpha-Beta strategy.

2. **AI vs AI**:  
   - Watch two AIs compete using different algorithms.

---

## Controls

- Enter your move by specifying the row and column number.  
  Example input: `1 2` (row 1, column 2).  

---

## Example Gameplay

```
Tic-Tac-Toe Game
Player (X) vs AI (O)

  1 | 2 | 3
 -----------
  4 | 5 | 6
 -----------
  7 | 8 | 9

Enter your move (row and column): 1 1
You placed 'X' at position (1, 1).

AI is thinking...
AI placed 'O' at position (1, 2).
```

---

## Code Structure

- **`tic_tac_toe.py`**: Main game logic implementing the Min-Max and Alpha-Beta algorithms.
- **Game Functions**:
  - `minimax()`: Min-Max algorithm.
  - `alpha_beta_pruning()`: Optimized Min-Max with Alpha-Beta pruning.
  - `check_winner()`: Determines the winner of the game.
  - `print_board()`: Displays the current game board.

---

## Future Improvements

- Add a GUI for better user interaction.
- Introduce difficulty levels by limiting AI search depth.
- Implement a multiplayer mode.

---

## License

This project is open-source and available under the MIT License.

---

## Author

- **Yousef2342K**  
  GitHub: [https://github.com/yousef2342K](https://github.com/yousef2342K)

---

Enjoy playing Tic-Tac-Toe and exploring AI strategies! 😊
