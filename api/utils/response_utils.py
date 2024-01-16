```python
from fastapi.responses import JSONResponse
from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR

def success_response(data: dict, message: str = "Success") -> JSONResponse:
    return JSONResponse(
        status_code=HTTP_200_OK,
        content={
            "message": message,
            "data": data,
            "error": None
        }
    )

def error_response(error: str, status_code: int = HTTP_400_BAD_REQUEST) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={
            "message": "Error occurred",
            "data": None,
            "error": error
        }
    )

def internal_server_error_response(error: str = "Internal Server Error") -> JSONResponse:
    return JSONResponse(
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "message": "Error occurred",
            "data": None,
            "error": error
        }
    )
```