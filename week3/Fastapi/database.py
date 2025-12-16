from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite URL
DATABASE_URL = "sqlite:///./notes.db"

# Create SQLite engine
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Session for database operations
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models
Base = declarative_base()
