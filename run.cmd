@echo off

rem Build the Docker image
echo Building Docker image...
docker build -t stockfish-app .

rem Run the container with code mounted
rem set FEN=startpos
set FEN=r2qk1r1/ppb2p2/2p1pnn1/3p2Q1/4P3/7P/PPPPNPP1/R1BB1RK1 w q - 5 15
echo Running Stockfish container with FEN=%FEN% ...
docker run -it --rm -v "%cd%":/app -w /app stockfish-app python main.py "%FEN%" 5 20
docker run -it --rm -v "%cd%":/app -w /app stockfish-app python main.py "%FEN%" 10 20
docker run -it --rm -v "%cd%":/app -w /app stockfish-app python main.py "%FEN%" 15 20

