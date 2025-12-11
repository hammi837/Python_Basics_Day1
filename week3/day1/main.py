from fastapi import FastAPI, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import SessionLocal, engine
import models

app = FastAPI()

# Create DB tables
models.Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request, db: Session = Depends(get_db)):
    notes = db.query(models.Note).all()
    return templates.TemplateResponse("index.html", {"request": request, "notes": notes})


@app.post("/notes/create")
async def create_note(
    title: str = Form(...),
    content: str = Form(...),
    db: Session = Depends(get_db)
):
    note = models.Note(title=title, content=content)
    db.add(note)
    db.commit()
    return RedirectResponse("/", status_code=303)


@app.get("/notes/delete/{note_id}")
async def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if note:
        db.delete(note)
        db.commit()
    return RedirectResponse("/", status_code=303)

@app.get("/notes/json")
def get_notes(db: Session = Depends(get_db)):
    return db.query(models.Note).all()
