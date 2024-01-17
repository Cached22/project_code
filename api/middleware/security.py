```python
from flask import request, jsonify
from functools import wraps
from api.utils.api_utils import verify_api_key

def require_api_key(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        if 'API-Key' not in request.headers:
            return jsonify({"message": "API key is missing"}), 403

        api_key = request.headers.get('API-Key')
        if not verify_api_key(api_key):
            return jsonify({"message": "Invalid API key"}), 403

        return view_function(*args, **kwargs)
    return decorated_function

def security_middleware(app):
    # Register middleware here if needed
    app.before_request(require_api_key)
```