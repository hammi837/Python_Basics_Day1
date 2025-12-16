# dependencies.py
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session

from fastapi import Request 
from database import SessionLocal
from models import User
from schemas import TokenData
from auth import decode_access_token
import models

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")  
# tokenUrl is the endpoint that clients will use to get tokens

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Helper to check cookie if header is missing
def get_token_from_request(request: Request):
    # Check Authorization Header first
    auth_header = request.headers.get("Authorization")
    if auth_header and auth_header.startswith("Bearer "):
        return auth_header.replace("Bearer ", "")
    
    # Check Cookies if header is missing
    token = request.cookies.get("access_token")
    if token:
        # If you stored it as "Bearer <token>" in the cookie
        return token.replace("Bearer ", "")
    return None

def get_current_user(request: Request, db: Session = Depends(get_db)):
    token = get_token_from_request(request)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    if not token:
        raise credentials_exception
    try:
        payload = decode_access_token(token)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(models.User).filter(models.User.username == username).first()
    if user is None:
        raise credentials_exception
    return user




def get_admin(user: User = Depends(get_current_user)):
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Admin only")
    return user
