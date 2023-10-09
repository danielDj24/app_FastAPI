from jwt import encode,decode

def create_token(data: dict) -> str:
    """Generate a token for a user-login"""
    token: str= encode(payload=data, key="my_secret_key", algorithm="HS256")
    return token

def validate_token(token: str) -> dict:
    """validate a token with credentials users"""
    data: dict= decode(token, key="my_secret_key", algorithms=['HS256'])
    return data