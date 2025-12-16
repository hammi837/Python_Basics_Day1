from pydantic import BaseModel, EmailStr
from typing import Optional
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = {
        "from_attributes": True
    }

class LoginRequest(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    username: str | None = None


class BookCreate(BaseModel):
    title: str
    author: str

class ReviewCreate(BaseModel):
    rating: float
    comment: Optional[str]