from datetime import timedelta, datetime

import fastapi
from fastapi import *

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext

from config import SECRET_KEY, ALGORITHM
from app.db import Db
from app.models import UserInDB, TokenData

app = fastapi.FastAPI()

db = Db()
pwd_context = CryptContext(schemes=["bcrypt"])
oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user_by_email(email):
    for name, data in db.fake_db.items():
        if data.get("email") == email:
            return UserInDB(**data)
    return None


def get_user_by_username(username):
    user = db.fake_db.get(username)
    if user:
        return UserInDB(**user)
    return None


def auth_user(email: str, password: str):
    user = get_user_by_email(email=email)

    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def register_user(username: str, email: str, password: str):
    user = get_user_by_username(username)
    print(user)
    if user:
        return False
    new_user = UserInDB(username=username, email=email, hashed_password=get_password_hash(password))
    db.fake_db[username] = new_user
    return new_user


def create_access_token(data: dict, expires_delta: timedelta or None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth_2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="C",
                                          headers={"WWW-Authenticate": "Bearer"})
    try:
        playload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = playload.get("username")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        return credentials_exception
    user = get_user_by_username(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user
