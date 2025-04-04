import os
from fastapi import FastAPI, Request, Query
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import torch
from huggingface_hub import hf_hub_download
from llama_cpp import Llama
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
import httpx


# Setup templates
templates = Jinja2Templates(directory="../frontend/templates")

# Define base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construct correct file paths
DATA_PATH = os.path.join(BASE_DIR, "../data/hotel_data_with_text.csv")
INDEX_PATH = os.path.join(BASE_DIR, "../faiss_index/hotel_rag.index")

# Load dataset
if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")
df = pd.read_csv(DATA_PATH)

# Load FAISS index
if not os.path.exists(INDEX_PATH):
    raise FileNotFoundError(f"FAISS index not found: {INDEX_PATH}")
index = faiss.read_index(INDEX_PATH)

# Load embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Download and load the `phi-2` model from Hugging Face
MODEL_REPO = "TheBloke/phi-2-GGUF"
MODEL_FILE = "phi-2.Q4_K_M.gguf"

model_path = hf_hub_download(repo_id=MODEL_REPO, filename=MODEL_FILE)

llm = Llama(
    model_path=model_path,  # Use downloaded model path
    n_gpu_layers=10,  
    n_ctx=2048,
    n_threads=8,
    verbose=False
)

# Initialize FastAPI
app = FastAPI(
    title="Hotel Booking Analytics API",
    description="An API to analyze hotel bookings, cancellations, revenue trends, and answer queries using RAG.",
    version="1.0"
)

# Function to search for relevant hotel data
def search_hotel_data(query, top_k=3):
    query_embedding = model.encode([query], convert_to_numpy=True)
    _, indices = index.search(query_embedding, top_k)
    return df.iloc[indices[0]]

# Function to generate response using `phi-2`
def generate_response(query):
    retrieved_data = search_hotel_data(query)
    context = " ".join(retrieved_data["text"].tolist())

    prompt = f"Based on the following hotel data: {context}\n\nAnswer this question: {query}"

    output = llm(prompt, max_tokens=50)
    answer = output["choices"][0]["text"].strip()

    return answer

# API Endpoint to get analytics reports
@app.get("/analytics")
def get_analytics():
    total_revenue = df["adr"].sum()
    cancellation_rate = df["is_canceled"].mean() * 100
    avg_lead_time = df["lead_time"].mean()

    return {
        "total_revenue": total_revenue,
        "cancellation_rate": cancellation_rate,
        "average_lead_time": avg_lead_time
    }

# API Endpoint to ask questions using RAG
@app.get("/ask")
async def ask_question(query: str):
    answer = generate_response(query)
    return {"query": query, "answer": answer}

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/query")
async def query(user_query: str = Query(..., alias="query")):
    async with httpx.AsyncClient() as client:
        response = await client.get("http://127.0.0.1:8000/ask", params={"query": user_query})

    if response.status_code == 200:
        return JSONResponse(content={"answer": response.json().get("answer", "No valid response received.")})
    else:
        return JSONResponse(content={"answer": "Error: No valid response received."})


# Run FastAPI server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
