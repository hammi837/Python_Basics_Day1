# auth.py
from datetime import datetime, timedelta ,timezone
from typing import Optional

from passlib.context import CryptContext
from jose import JWTError, jwt

# -- CONFIG --
SECRET_KEY = "228e4df409fc760a4bfd0f0cd40aeedfc64647593b90d032b9b956491689e860"  # change in prod, keep secret
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # 1 day (adjust as needed)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Password utils
def get_password_hash(password: str):
    password = password[:72]   # bcrypt max length fix
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    plain_password = plain_password[:72]  # same fix during verification
    return pwd_context.verify(plain_password, hashed_password)

# JWT utils
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    now = datetime.now(timezone.utc)
    if expires_delta:
        expire = now + expires_delta
    else:
        expire = now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire, "iat": now})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str) -> dict:
    """
    Decode and validate a JWT. Raises JWTError if invalid/expired.
    Returns payload dict if OK.
    """
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload
   

