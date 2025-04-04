#!/bin/bash

# Setting up environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate
pip install -r requirements.txt

# Start FastAPI backend
cd backend
python app.py 
