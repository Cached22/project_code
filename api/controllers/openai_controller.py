```python
from fastapi import APIRouter, HTTPException
from openai_utils.generate_response import generate_response
from api.schemas import OpenAIRequest, OpenAIResponse
from config.settings import API_KEY

router = APIRouter()

@router.post("/generate-response", response_model=OpenAIResponse)
async def openai_generate_response(request: OpenAIRequest):
    try:
        prompt = request.prompt
        response = generate_response(API_KEY, prompt)
        return OpenAIResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```