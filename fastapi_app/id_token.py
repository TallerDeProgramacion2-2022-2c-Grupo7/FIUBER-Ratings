from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi import status
from firebase_admin import auth
from firebase_admin import _auth_utils as auth_utils
from starlette.middleware.base import BaseHTTPMiddleware


class IdTokenMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.method == "OPTIONS" or request.url.path in (
            "/docs",
            "/openapi.json",
        ):
            return await call_next(request)
        try:
            authorization = request.headers["Authorization"]
            user = auth.verify_id_token(authorization[7:])
        except (
            KeyError,
            TypeError,
            UnicodeDecodeError,
            auth_utils.InvalidIdTokenError,
        ) as e:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": "You must be logged in to make this request"},
                headers={"Access-Control-Allow-Origin": "*"},
            )
        return await call_next(request)
