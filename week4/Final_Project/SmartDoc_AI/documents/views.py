# documents/views.py
import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Document



@login_required
def list(request):
    documents = Document.objects.filter(user=request.user)
    return render(request, 'list.html', {'documents': documents})


FASTAPI_URL = "http://127.0.0.1:8001/api/upload-document/"
@login_required
def upload(request):
    if request.method == "POST" and request.FILES.get("file"):
        file = request.FILES["file"]

        # Save in Django first
        doc = Document.objects.create(user=request.user, file=file)
        print(doc)

        # Send to FastAPI
        with open(doc.file.path, "rb") as f:
            response = requests.post(FASTAPI_URL, files={"file": f})
        
        if response.status_code == 200:
            doc.doc_id = response.json().get("doc_id")
            print(doc.doc_id)
            doc.save()

        
        return redirect("list")

    return render(request, "upload.html")




import requests

def ask_ai(request, doc_id):
    answer = None
    doc = Document.objects.get(id=doc_id)  # Django numeric ID
    file_name = doc.file.name.split("/")[-1] 
    if request.method == "POST":
        question = request.POST.get("question")
        payload = {"query": question, "doc_id": file_name}

        try:
            response = requests.post("http://127.0.0.1:8001/api/qa/", params=payload, timeout=10)
            # Make sure we only try to parse JSON if status code is 200
            if response.status_code == 200:
                try:
                    data = response.json()
                    answer = data.get("answer", data.get("error", "No answer"))
                except ValueError:
                    answer = "Invalid response from AI server."
            else:
                answer = f"AI server returned status {response.status_code}"
        except requests.ConnectionError:
            answer = "Cannot connect to AI server. Make sure FastAPI is running."
        except requests.Timeout:
            answer = "Request to AI server timed out."

    return render(request, "ask_ai.html", {"answer": answer})

