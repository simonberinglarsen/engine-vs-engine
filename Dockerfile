# Base image with Python
FROM python:3.11-slim

# Install stockfish and unzip
RUN apt update && apt install -y stockfish && \
    apt clean && rm -rf /var/lib/apt/lists/*

# Set work directory in the container
WORKDIR /app

# Copy code into container (optional if you mount it)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command (optional)
CMD ["python", "main.py"]
