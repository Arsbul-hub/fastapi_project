from pydantic import BaseModel


class Data(BaseModel):
    name: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str or None = None


class User(BaseModel):
    username: str
    email: str


class UserInDB(User):
    hashed_password: str
