# Hotel Booking Data Analytics & QA System

## Overview
This project is a **Hotel Booking Data Analytics & Question Answering (QA) System** using **FastAPI** . It analyzes hotel booking data, provides insights, and answers user queries using a **RAG (Retrieval-Augmented Generation)**.

## Directory Structure
```
Hotel-Booking-Analytics-QA-System/
│── data/                    
│   ├── hotel_bookings.csv            # Raw hotel booking data
│   ├── hotel_data_with_text.csv       # Processed data with additional text features
│
│── notebooks/                         # Jupyter notebooks for data analysis & model training
│   ├── analytics.ipynb                # Exploratory data analysis & assignment analytics
│   ├── RAG_Phi-2_Quantisation.ipynb   # Model quantization for efficiency
│
│── backend/                           # FastAPI backend handling analytics & QA
│   ├── app.py                         # Main API server
│
│── frontend/                           
│   ├── templates/                     
│   │   ├── index.html                 # Main UI template
│
│── faiss_index/                       # FAISS index for efficient retrieval
│   ├── hotel_rag.index                # Precomputed FAISS index
│
│── requirements.txt                    # List of required dependencies
│── README.md                           # Project documentation
│── run.sh                              # Script to start backend & frontend together
│── .gitignore                          # Ignore unnecessary files (venv, etc.)
│── screenshots/                        # Contains UI response screenshots (if included)
```

## Prerequisites
- Python 3.8+
- Virtual environment (recommended)
- `pip` package manager

## Setup Instructions
### 1. Clone the repository
```bash
git clone https://github.com/your-username/Hotel-Booking-Analytics-QA-System.git 
cd HotelBooking-RAG
```

### 2. Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Start the application
```bash
./run.sh  # Runs backend and frontend together
```

## Usage
- **Backend API (FastAPI)** runs on `http://127.0.0.1:8000`
- Ask hotel-related questions using the frontend UI.

## Analytics & Sample Queries
- The **`analytics.ipynb`** file contains the **required analytics for the assignment**, including data analysis and sample test queries with their expected answers.
- These queries demonstrate how the system responds to different hotel-related questions.

## Model Handling
- The **`phi-2.Q4_K_M.gguf` model** is **not included** in the repository.
- It is automatically downloaded and cached from Hugging Face.

## Screenshots (Optional)
- If required, UI screenshots of the system answering user queries can be included in the **screenshots/** directory.
- [Optional: Insert images here if necessary]

## License
MIT License.

