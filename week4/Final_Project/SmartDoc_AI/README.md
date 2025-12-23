# AI-powered Knowledge Management System

## Description
A platform where users can upload documents (PDF, Word, TXT) and ask AI questions about them.  
Django handles authentication, user management, and frontend UI, while FastAPI handles AI endpoints for document processing, semantic search, and question-answering.

---

## **Features**
- Upload documents in multiple formats (PDF, DOCX, TXT)
- AI-powered question answering using LLMs
- Semantic search for relevant content
- Django-based user authentication and management
- Interactive and responsive web interface
- Separation of concerns: Django handles frontend, FastAPI handles AI logic

---

## **Technologies**
- **Backend:** Django 6.0, FastAPI
- **AI & NLP:** OpenAI / Groq API, SentenceTransformers (`all-MiniLM-L6-v2`), FAISS
- **File Handling:** PDFMiner, python-docx
- **Frontend:** Django templates (HTML, Bootstrap optional)
- **Python:** 3.13+
- **Database:** SQLite (default) or PostgreSQL

---

## **Installation**

1. Clone the repository:
```bash
git clone https://github.com/username/SmartDoc_AI.git
cd SmartDoc_AI

2. Create a virtual environment:
python -m venv venv
source venv/bin/activate    # Linux / macOS
venv\Scripts\activate       # Windows

3. Install dependencies:
pip install -r requirements.txt

4. Set environment variables:
export GROQ_API_KEY="your_api_key_here"   # Linux / macOS
set GROQ_API_KEY="your_api_key_here"      # Windows

5. Run Django server:
python manage.py migrate
python manage.py runserver 8000

6. Run FastAPI server:
uvicorn main:app --reload --port 8001

Folder Structure:
```text
SmartDoc_AI/
│
├── documents/                # Django app for document management
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   └── admin.py
│
├── fastapi_ai/               # FastAPI app for AI processing
│   ├── main.py               # FastAPI endpoints
│   └── ai_utils.py           # Text extraction, embedding, semantic search, QA
│
├── media/                    # Uploaded documents storage
│   └── documents/
│
├── SmartDoc_AI/              # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── templates                    
├── requirements.txt
└── README.md
