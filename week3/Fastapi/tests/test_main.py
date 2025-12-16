from main import app
from fastapi.testclient import TestClient
from fastapi import status

client=TestClient(app=app)

def test_home():
    response=client.get("/")
    assert response.status_code==status.HTTP_200_OK

def test_create_note():
    note_data={
        "title":"Intro",
        "content":"Hello,I am hammad"
    }
    response= client.post("/notes/create",data=note_data)
    assert response.status_code==status.HTTP_200_OK

    notes_response=client.get("/notes/json")
    notes=notes_response.json()

    assert any(note["title"] == "Intro" and note["content"] == "Hello,I am hammad" for note in notes)



