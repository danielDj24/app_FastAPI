from pydantic import BaseModel

class User(BaseModel):
    """model users"""
    email: str
    password: str 