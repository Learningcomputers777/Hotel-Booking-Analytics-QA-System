#!/bin/bash

# Setting up environment
python -m venv venv
pip install -r requirements.txt

# Activate virtual environment
source venv/bin/activate

# Start FastAPI backend
cd backend
python app.py 
