# Implementation Choices & Challenges

## Implementation Choices
1. **Model Selection**
   - Initially tested multiple models (**LLaMA, Falcon, Mistral, GPT-Neo**), but faced GPU limitations.
   - Final model: **Phi-2 (GGUF format)** for efficient inference.

2. **Backend Development**
   - Used **FastAPI** for handling API requests efficiently.
   - Integrated **FAISS** for fast retrieval of relevant documents.
   - Model is automatically downloaded from Hugging Face when running `app.py`.

3. **Frontend Development**
   - Built using **Flask** for a simple UI.
   - Communicates with FastAPI backend to process user queries.
   - Issue: Clicking 'Ask' rapidly caused server crashes.

4. **Virtual Environment & Dependency Management**
   - Used **Python `venv`** for environment isolation.
   - Created **`requirements.txt`** for tracking dependencies.

5. **Automated Setup & Execution**
   - Created `run.sh` to launch **both backend and frontend** using a single command.
   - Ensures correct virtual environment activation.

## Challenges Faced
### 1. Model Compatibility Issues
   - **LLaMA, Falcon, Mistral, GPT-Neo 1.3B** did not fit into GPU memory.
   - Model offloading to **meta disk** caused slow performance.
   
### 2. Hugging Face Model Access
   - Tried accessing **LLaMA-2**, but access request was rejected by the author.
   - Switched to **Phi-2 GGUF**, which is open access.

### 3. GPU Memory Management
   - Encountered **data not being erased** from GPU memory when switching models.
   - Resolved by manually clearing memory using `torch.cuda.empty_cache()`.

### 4. Frontend Button Issue
   - Clicking 'Ask' too quickly **crashed the server**.
   - Tried using **async functions**, but resulted in unresponsiveness.

### 5. Local vs Cached Model
   - Attempted to run the model **without local installation**, but failed.
   - Found a workaround: **download & cache model automatically on first run**.

### 6. Large Unused Model Files
   - Hugging Face cache contained **25GB of unnecessary models**.
   - Manually deleted excess files to free up storage.

## Conclusion
Despite challenges, the project successfully implemented a **working RAG-based QA system** for hotel booking analytics. Future improvements include optimizing model loading, handling concurrent requests better, and refining the frontend experience.

