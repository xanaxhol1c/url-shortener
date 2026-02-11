from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from http import HTTPStatus

from src.routes.urls import router as urls_router

app = FastAPI()

app.include_router(urls_router)

@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exc: RequestValidationError):
    error_messages = [err['msg'] for err in exc.errors()]

    return JSONResponse(
        status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
        content={'message' : error_messages[0]}
    )
