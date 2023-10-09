from fastapi.security import HTTPBearer
from fastapi import Request
from utils.jwt_manager import  validate_token
from fastapi import HTTPException


class JWTbearer(HTTPBearer):
    """verificate token of a users"""
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail="credentials invalidated")
        