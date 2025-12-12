# 🧩 Playable Sudoku Game (Python + Pygame)

A **playable Sudoku game** built with **Python and Pygame**, featuring manual gameplay and an **AI-powered DFS backtracking solver** with real-time visualization.

You can play the puzzle yourself or let the algorithm solve it step by step.

---

## ✨ Features

- 🎮 Fully **playable Sudoku board**
- 🖱️ Click cells & type numbers (1–9)
- ❌ Fixed cells are locked
- ⌫ Clear cells with Backspace/Delete
- 🤖 **Auto-solve** using DFS + Backtracking
- 🔁 Reset puzzle anytime
- 🧠 Visualized solving process
- 🪶 Lightweight & beginner-friendly codebase

---

## 🎮 Controls

| Action | Key / Input |
|------|------------|
| Select cell | Mouse Click |
| Enter number | `1 – 9` |
| Clear cell | `Backspace` / `Delete` |
| Auto-solve puzzle | `SPACE` |
| Reset puzzle | `R` |
| Quit game | `ESC` |

---

## 📸 Gameplay Overview

- Dark numbers → fixed puzzle values  
- Light numbers → player-entered values  
- Solver fills cells step-by-step using **Depth-First Search with backtracking**

---

## 🛠️ Tech Stack

- **Python 3**
- **Pygame**
- DFS + Backtracking Algorithm
- Modular, readable project structure

---

## 📂 Project Structure

sudoku_game/
│
├── main.py # Game loop & event handling
├── sudoku_board.py # Board logic & validation
├── sudoku_solver.py # DFS backtracking solver
├── sudoku_visualizer.py # Rendering & UI
├── puzzles.py # Predefined puzzles
├── constants.py # UI constants
└── README.md

yaml
Copy code

---

## 🚀 How to Run

### 1️⃣ Install dependencies
```bash
pip install pygame
2️⃣ Run the game
bash
Copy code
python main.py
Make sure you run the command from the project folder.

🧠 Algorithm Used
The solver uses Depth-First Search (DFS) with backtracking:

Tries values 1–9

Validates each move

Backtracks when a dead-end is reached

Continues until the puzzle is solved

📌 Why This Project?
This project was built to:

Practice algorithm visualization

Learn event-driven game programming

Combine manual gameplay with AI-assisted solving

Create a clean, portfolio-ready Python project

📜 License
This project is licensed under the MIT License — feel free to use, modify, and learn from it.

⭐ If you like this project, consider starring the repo!