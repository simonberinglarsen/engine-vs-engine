# ♟️ Stockfish Self-Play in Docker

This project runs games between two instances of Stockfish using Python, Docker, and PGN generation. Great for self-play testing, analysis, and fun experiments!

---

## 📦 Features

- Full game between two Stockfish engines (different depths)
- Supports `startpos` or custom FEN input
- PGN generation with full headers
- Auto-incrementing PGN filenames (e.g. `game1.pgn`, `game2.pgn`, …)
- Dockerized for clean, portable execution

---

## 🛠 Requirements

- [Docker](https://www.docker.com/)
- Windows with CMD (or adapt `run_stockfish.cmd` for PowerShell/bash)

---

## 🚀 How to Run

1. Clone or copy this repo  
2. Make sure your `main.py`, `Dockerfile`, `requirements.txt`, and `run_stockfish.cmd` are in the same folder

3. **Edit the script (optional)**  
   In `run_stockfish.cmd`, set your desired FEN:
   ```cmd
   set FEN=startpos
