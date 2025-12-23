from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from ai_utils import extract_text, build_index, semantic_search, answer_question
import os

app = FastAPI(title="SmartDoc AI Service")

# Allow frontend to communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

documents = {}  # doc_id -> file_path


@app.post("/api/upload-document/")
async def upload_document(file: UploadFile = File(...)):
    # Ensure the folder exists
    file_location = f"media/documents/{file.filename}"
    os.makedirs(os.path.dirname(file_location), exist_ok=True)

    # Save uploaded file
    with open(file_location, "wb") as f:
        f.write(await file.read())

    documents[file.filename] = file_location

    # Extract text and build semantic index
    text = extract_text(file_location)
    chunks = [text[i:i + 1000] for i in range(0, len(text), 1000)]
    build_index(file.filename, chunks)

    return {"status": "success", "doc_id": file.filename}


@app.post("/api/search/")
async def search(query: str, doc_id: str, top_k: int = 5):
    doc_id = doc_id.strip('"').strip("'")
    if doc_id not in documents:
        return {"error": "Document not found"}

    results = semantic_search(doc_id, query, top_k)
    return {"results": results}


@app.post("/api/qa/")
async def qa(query: str, doc_id: str):
    doc_id = doc_id.strip('"').strip("'")
    if doc_id not in documents:
        return {"error": "Document not found"}

    try:
        # Get top relevant chunks using semantic search
        top_chunks = semantic_search(doc_id, query, top_k=3)
        if not top_chunks:
            return {"answer": "No relevant information found in document."}

        context = "\n".join([chunk["text"] for chunk in top_chunks])

        # Generate answer from model
        answer = answer_question(query, context)

        return {"answer": answer}

    except Exception as e:
        return {"error": str(e)}

