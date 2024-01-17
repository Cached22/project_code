```python
from fastapi import HTTPException, Request
from pydantic import ValidationError
from api.schemas import ProjectMetadata, AnalysisReport, EnhancementReport, ReviewReport, LearningResult, GPTResponse

async def validate_project_metadata(request: Request):
    try:
        # Validate request body against ProjectMetadata schema
        body = await request.json()
        ProjectMetadata(**body)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())

async def validate_analysis_report(request: Request):
    try:
        # Validate request body against AnalysisReport schema
        body = await request.json()
        AnalysisReport(**body)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())

async def validate_enhancement_report(request: Request):
    try:
        # Validate request body against EnhancementReport schema
        body = await request.json()
        EnhancementReport(**body)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())

async def validate_review_report(request: Request):
    try:
        # Validate request body against ReviewReport schema
        body = await request.json()
        ReviewReport(**body)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())

async def validate_learning_result(request: Request):
    try:
        # Validate request body against LearningResult schema
        body = await request.json()
        LearningResult(**body)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())

async def validate_gpt_response(request: Request):
    try:
        # Validate request body against GPTResponse schema
        body = await request.json()
        GPTResponse(**body)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
```