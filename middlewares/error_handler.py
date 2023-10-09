
from starlette.middleware.base import  BaseHTTPMiddleware
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse


class ErrorHandler(BaseHTTPMiddleware):
    """Model for detected errors in the app """
    def __init__(self, app: FastAPI) -> None:
        """function for catch APP"""
        super().__init__(app)
        
    async def dispatch(self, request: Request, call_next) -> Response or JSONResponse:
        """async function for manage errors or return message with the error"""
        try:
            return await call_next(request)
        except Exception as e:
            return JSONResponse(status_code=500, content={'error': str(e)})