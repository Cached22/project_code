```python
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

async def error_handler(request: Request, exc: HTTPException):
    """
    Middleware error handler to intercept HTTP exceptions and return a custom JSON response.
    This function will be used to handle errors across the API, ensuring a consistent error
    response format for the client.
    """
    # Log the error details for debugging purposes
    # This assumes a logger is set up in the application
    request.app.logger.error(f"Error occurred: {exc.detail}")

    # Return a JSON response with the error details
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "type": "Exception",
                "message": exc.detail
            }
        }
    )

# To use this middleware, it should be added to the FastAPI application instance
# in the main app.py file like so:
# app.add_middleware(
#     middleware_class=error_handler
# )
```