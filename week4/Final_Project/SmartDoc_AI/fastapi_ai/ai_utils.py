import os
from pdfminer.high_level import extract_text as extract_pdf
import docx
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from openai import OpenAI

# OpenAI / Groq client
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# ---------------------------
# Document Text Extraction
# ---------------------------
def extract_text(file_path: str) -> str:
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        return extract_pdf(file_path)
    elif ext == ".docx":
        doc = docx.Document(file_path)
        return "\n".join(p.text for p in doc.paragraphs)
    elif ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        raise ValueError("Unsupported file type")


# ---------------------------
# Embedding Model & Index
# ---------------------------
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embeddings(texts: list[str]):
    return model.encode(texts, convert_to_numpy=True)


# Store indexes per document
doc_indexes = {}   # doc_id -> FAISS index
doc_chunks = {}    # doc_id -> list of text chunks

def build_index(doc_id: str, text_chunks: list[str]):
    embeddings = get_embeddings(text_chunks)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    doc_indexes[doc_id] = index
    doc_chunks[doc_id] = text_chunks


def semantic_search(doc_id: str, query: str, top_k: int = 5):
    if doc_id not in doc_indexes:
        return []

    q_emb = get_embeddings([query])
    index = doc_indexes[doc_id]
    chunks = doc_chunks[doc_id]

    distances, indices = index.search(q_emb, top_k)
    results = [{"text": chunks[i], "score": float(distances[0][k])} for k, i in enumerate(indices[0])]
    return results


def answer_question(question: str, context: str, model_name="llama-3.1-8b-instant") -> str:
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant that answers questions using the provided context."
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion:\n{question}"
            }
        ],
        max_tokens=200,
        temperature=0.2
    )
    return response.choices[0].message.content.strip()
