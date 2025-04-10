from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TransactionBase(BaseModel):
    amount: float
    type: str
    description: Optional[str] = None

class TransactionCreate(TransactionBase):
    pass

class TransactionOut(TransactionBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True