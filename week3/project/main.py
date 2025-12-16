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
from schemas import UserCreate, UserOut, Token ,BookCreate,ReviewCreate
from dependencies import get_db, get_current_user ,get_admin

from database import engine
from models import Book ,User,Reviews
from database import engine
from models import Base
import models
limiter = Limiter(key_func=get_remote_address)
app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=engine)


templates = Jinja2Templates(directory="templates")


from fastapi import Form

from fastapi import Request
from fastapi.responses import HTMLResponse

@app.get("/register", response_class=HTMLResponse)
def get_register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.post("/register",response_class=HTMLResponse)
def post_register(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    existing_user = db.query(models.User).filter(
        (models.User.username == username) | (models.User.email == email)
    ).first()
    if existing_user:
        return templates.TemplateResponse(
            "register.html",
            {"request": request, "error": "Username or email already exists"}
        )

    hashed_pw = get_password_hash(password)
    user = models.User(username=username, email=email, password=hashed_pw)
    db.add(user)
    db.commit()
    db.refresh(user)

    return templates.TemplateResponse(
        "login.html",
        {"request": request, "message": "Registration successful! Please login."}
    )



@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})




@app.post("/login")  # This matches the 'action' in your HTML form
def post_login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    # 1. Verify User
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user or not verify_password(password, user.password):
        # If login fails, send them back to login page with an error
        return templates.TemplateResponse("login.html", {
            "request": request, 
            "error": "Invalid username or password"
        })

    # 2. Create Token
    access_token = create_access_token(data={"sub": user.username})

    # 3. Create Redirect to Home
    response = RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
    
    # 4. Store token in a Cookie (Crucial for browser navigation)
    response.set_cookie(
        key="access_token", 
        value=f"Bearer {access_token}", 
        httponly=True
    )
    
    return response
    
    



@app.get("/users/me", response_model=UserOut)
def read_users_me(current_user: models.User = Depends(get_current_user)):
    return current_user

@app.get("/", response_class=HTMLResponse)
def home_page(request: Request, db: Session = Depends(get_db)):
    try:
        user = get_current_user(request, db)
        return templates.TemplateResponse("home.html", {"request": request, "user": user})
    except HTTPException:
        return RedirectResponse(url="/login")

# Add this to show the form
@app.get("/books/create", response_class=HTMLResponse)
def get_create_book(request: Request, admin: User = Depends(get_admin)):
    return templates.TemplateResponse("create_book.html", {"request": request})

# Your existing POST route (Fixed the URL redirect)
@app.post("/books")
def create_book(
    title: str = Form(...),
    author: str = Form(...),
    db: Session = Depends(get_db),
    admin: User = Depends(get_admin)
):
    book = models.Book(title=title, author=author)
    db.add(book)
    db.commit()
    db.refresh(book)
    # Changed from "/home" to "/" to match your home_page route
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)


@app.get("/books")
def get_books(request: Request,db:Session=Depends(get_db)):
    books= db.query(models.Book).all()
    return templates.TemplateResponse("books.html", {"request": request, "books": books})


@app.post("/books/{book_id}/reviews")
def add_review(
    book_id: int,
    rating: int = Form(...),
    comment: str = Form(...),
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    # 1. Save the review to the database
    db_review = Reviews(
        rating=rating,
        comment=comment,
        book_id=book_id,
        user_id=user.id,
        approved=False  # Assuming reviews need admin approval first
    )
    db.add(db_review)
    db.commit()

    # 2. Redirect back to the book page
    return RedirectResponse(
        url=f"/books/{book_id}?message=Review submitted for approval", 
        status_code=status.HTTP_303_SEE_OTHER
    )

@app.get("/books/{book_id}/reviews")
def get_reviews(book_id: int, db: Session = Depends(get_db)):
    return db.query(models.Reviews).filter(
        Reviews.book_id == book_id,
        Reviews.approved == True
    ).all()




@app.get("/books/{book_id}", response_class=HTMLResponse)
def get_book_details(
    request: Request, 
    book_id: int, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    
    # Get all reviews for this book
    # We show: 1. All approved reviews, 2. The current user's unapproved reviews
    reviews = db.query(models.Reviews).filter(
        models.Reviews.book_id == book_id
    ).filter(
        (models.Reviews.approved == True) | (models.Reviews.user_id == current_user.id)
    ).all()

    return templates.TemplateResponse("book_detail.html", {
        "request": request, 
        "book": book, 
        "reviews": reviews,
        "current_user": current_user
    })

# ---------- ADMIN ----------
# 1. Page to view pending reviews
@app.get("/admin/reviews", response_class=HTMLResponse)
def review_queue(request: Request, db: Session = Depends(get_db), admin: User = Depends(get_admin)):
    pending_reviews = db.query(models.Reviews).filter(models.Reviews.approved == False).all()
    return templates.TemplateResponse("admin_reviews.html", {
        "request": request, 
        "reviews": pending_reviews
    })

# 2. Updated Approval Route (using POST for easier HTML form handling)
@app.post("/admin/reviews/{review_id}/approve")
def approve_review(review_id: int, db: Session = Depends(get_db), admin: User = Depends(get_admin)):
    review = db.query(models.Reviews).filter(models.Reviews.id == review_id).first()
    if review:
        review.approved = True
        db.commit()
    return RedirectResponse(url="/admin/reviews", status_code=303)

# 3. Updated Delete Route (using POST for easier HTML form handling)
@app.post("/admin/reviews/{review_id}/delete")
def delete_review(review_id: int, db: Session = Depends(get_db), admin: User = Depends(get_admin)):
    review = db.query(models.Reviews).filter(models.Reviews.id == review_id).first()
    if review:
        db.delete(review)
        db.commit()
    return RedirectResponse(url="/admin/reviews", status_code=303)