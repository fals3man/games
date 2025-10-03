# Python Games Collection 🎮

This repository contains Python implementations of two classic games: **Tic-Tac-Toe (with unbeatable AI)** and **Tetris**.

---

## 1. Tic-Tac-Toe (with Minimax AI)
An AI-powered Tic-Tac-Toe game using the **Minimax adversarial search algorithm**.  
The AI plays optimally, making it impossible to beat.

### Run the Game
```bash
python3 runner.py
```

### Screenshot
![Tic-Tac-Toe](https://user-images.githubusercontent.com/57314773/178114104-aafcff1c-934b-45d4-8854-fa1c4675f859.png)

---

## 2. Tetris (PyQt5)
A **classic Tetris game** built with Python and **PyQt5**.

### Requirements
- Python 3.x
- PyQt5

Install dependencies:
```bash
pip install PyQt5
```

### Run the Game
```bash
python3 tetris_game.py
```

### Controls
- ⬅️ **Left Arrow** – Move left
- ➡️ **Right Arrow** – Move right
- ⬆️ **Up Arrow** – Rotate shape
- ⬇️ *(optional if added)* – Move down slowly
- ␣ **Spacebar** – Drop shape instantly
- **P** – Pause / Resume

The right panel shows the **next shape** in the queue.

### Screenshot
![Tetris](https://user-images.githubusercontent.com/57314773/178114277-3131f002-1ac1-4b48-bcd3-e0e84640c2fb.png)

---

## Project Structure
```
.
├── tic_tac_toe/
│   ├── runner.py          # Entry point for Tic-Tac-Toe
│   └── ...                # Supporting files
│
├── tetris/
│   ├── tetris_game.py     # Entry point for Tetris
│   ├── tetris.py          # Main application logic
│   └── board.py           # Data model for the game board
│
└── README.md
```

---

## Future Improvements
- Add difficulty levels to Tic-Tac-Toe.
- Add score tracking and high-score saving in Tetris.
- Package both games as standalone executables.  

// nice game , very challenging levels
