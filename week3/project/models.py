from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)   
    password = Column(String)
    is_admin = Column(Boolean, default=False)

    reviews = relationship("Reviews", back_populates="user")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)

    reviews = relationship("Reviews", back_populates="book")


class Reviews(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Integer)
    comment = Column(String)
    approved = Column(Boolean, default=False)

    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey("books.id"))

    user = relationship("User", back_populates="reviews")
    book = relationship("Book", back_populates="reviews")
