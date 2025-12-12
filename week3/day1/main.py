from fastapi import FastAPI, Request, Depends, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from datetime import timedelta
from slowapi import Limiter
from slowapi.util import get_remote_address

from auth import get_password_hash, verify_password, create_access_token
from schemas import UserCreate, UserOut, Token
from dependencies import get_db, get_current_user

from database import engine
import models
limiter = Limiter(key_func=get_remote_address)
app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.post("/register", response_model=UserOut)
@limiter.limit("5/minute")
def register(request: Request, user_in: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(models.User.username == user_in.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already registered")

    hashed_pw = get_password_hash(user_in.password)

    user = models.User(
        username=user_in.username,
        email=user_in.email,
        password=hashed_pw    # IMPORTANT: match your model field
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.post("/token", response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = db.query(models.User).filter(models.User.username == form_data.username).first()

    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=60 * 24)

    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires,
    )

    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me", response_model=UserOut)
def read_users_me(current_user: models.User = Depends(get_current_user)):
    return current_user



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


