#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Start FastAPI backend
cd backend
python app.py &

# Start Flask frontend
cd ../frontend
python frontend.py &

# Wait for both to finish
wait
