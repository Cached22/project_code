```python
from flask import jsonify

def handle_error(e):
    """Handle errors in a standardized way across the web backend.

    Args:
        e (Exception): The exception that was raised.

    Returns:
        A response object containing the error message and the appropriate HTTP status code.
    """
    if hasattr(e, 'code'):  # HTTPException
        response = jsonify(error=str(e.description), code=e.code)
        response.status_code = e.code
    else:
        response = jsonify(error=str(e), code=500)
        response.status_code = 500

    # Log the error for debugging purposes
    # Assuming there's a logger set up in the application
    # logger.error(f'An error occurred: {str(e)}')

    return response

def register_error_handlers(app):
    """Register error handlers for the Flask application.

    Args:
        app (Flask): The Flask application instance.
    """
    app.register_error_handler(404, handle_error)
    app.register_error_handler(500, handle_error)
    # Add other error codes as needed
```
