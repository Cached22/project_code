```python
from fastapi import FastAPI, HTTPException
from api.routes import analysis_router, enhancement_router, review_router, learning_router, openai_router
from api.middleware.error_handler import add_error_handling_middleware
from api.middleware.security import add_security_middleware
from api.middleware.validation import add_validation_middleware

app = FastAPI(title='Code Analysis and Enhancement Tool')

# Add middleware
add_error_handling_middleware(app)
add_security_middleware(app)
add_validation_middleware(app)

# Include routers
app.include_router(analysis_router, tags=["Code Analysis"], prefix="/analyze")
app.include_router(enhancement_router, tags=["Code Enhancement"], prefix="/enhance")
app.include_router(review_router, tags=["Code Review"], prefix="/review")
app.include_router(learning_router, tags=["Continuous Learning"], prefix="/learn")
app.include_router(openai_router, tags=["OpenAI Utils"], prefix="/generate-response")

@app.get("/", include_in_schema=False)
async def root():
    return {"message": "Welcome to the Code Analysis and Enhancement Tool API!"}
```