import sys
import os
import chess
import chess.pgn
import datetime
from stockfish import Stockfish

# Setup
stockfish_path = "/usr/games/stockfish"
if len(sys.argv) != 4:
    print("Usage: python main.py <FEN or 'startpos'> <depth_white> <depth_black>")
    sys.exit(1)

start_fen = sys.argv[1]
depth_white = int(sys.argv[2])
depth_black = int(sys.argv[3])

stockfish_white = Stockfish(stockfish_path)
stockfish_black = Stockfish(stockfish_path)

# Initialize PGN tracking
game = chess.pgn.Game()
board = chess.Board() if start_fen == "startpos" else chess.Board(start_fen)
node = game

# 🔹 Set PGN Headers
game.headers["Event"] = "Stockfish Self-Play"
game.headers["Site"] = "Docker Container"
game.headers["Date"] = datetime.datetime.now().strftime("%Y.%m.%d")
game.headers["Round"] = "1"
game.headers["White"] = f"Stockfish ({depth_white})"
game.headers["Black"] = f"Stockfish ({depth_black})"
game.headers["Result"] = "*"

# Add FEN header if starting from a custom position
if start_fen != "startpos":
    game.headers["FEN"] = start_fen
    game.headers["SetUp"] = "1"

# Set position
if start_fen == "startpos":
    stockfish_white.set_position([])
    stockfish_black.set_position([])
else:
    stockfish_white.set_fen_position(start_fen)
    stockfish_black.set_fen_position(start_fen)

# Game loop
while not board.is_game_over():
    engine = stockfish_white if board.turn == chess.WHITE else stockfish_black
    engine.set_depth(depth_white if board.turn == chess.WHITE else depth_black)

    move = engine.get_best_move()
    if not move:
        print(f"Game over! Result: {board.result()}")
        game.headers["Result"] = board.result()
        break

    # Convert move to PGN format and update board
    chess_move = chess.Move.from_uci(move)
    if chess_move not in board.legal_moves:
        print("Illegal move detected. Exiting.")
        break

    board.push(chess_move)
    node = node.add_variation(chess_move)

    # Apply move to both engines
    stockfish_white.make_moves_from_current_position([move])
    stockfish_black.make_moves_from_current_position([move])

    print(f"Move {board.fullmove_number}: {move} | New FEN: {board.fen()}")

# Find next available filename
base_name = "game"
ext = ".pgn"
i = 1
while os.path.exists(f"{base_name}{i}{ext}"):
    i += 1
pgn_filename = f"{base_name}{i}{ext}"

# Save PGN
with open(pgn_filename, "w") as pgn_file:
    pgn_file.write(str(game))

print(f"Game saved to {pgn_filename}")