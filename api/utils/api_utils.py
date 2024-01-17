```python
from fastapi import HTTPException, status
from api.schemas import AnalysisReport, EnhancementReport, ReviewReport, LearningResult, GPTResponse
from utils.file_operations import validate_file_path
from utils.error_handling import log_error

def validate_and_extract_file_path(file_path: str) -> str:
    """
    Validates the given file path and returns the absolute path if valid.
    Raises HTTPException if the file path is invalid.
    """
    try:
        return validate_file_path(file_path)
    except ValueError as e:
        log_error(str(e))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

def create_analysis_report(data: dict) -> AnalysisReport:
    """
    Converts a dictionary to an AnalysisReport object.
    """
    return AnalysisReport(**data)

def create_enhancement_report(data: dict) -> EnhancementReport:
    """
    Converts a dictionary to an EnhancementReport object.
    """
    return EnhancementReport(**data)

def create_review_report(data: dict) -> ReviewReport:
    """
    Converts a dictionary to a ReviewReport object.
    """
    return ReviewReport(**data)

def create_learning_result(data: dict) -> LearningResult:
    """
    Converts a dictionary to a LearningResult object.
    """
    return LearningResult(**data)

def create_gpt_response(data: dict) -> GPTResponse:
    """
    Converts a dictionary to a GPTResponse object.
    """
    return GPTResponse(**data)

def handle_api_error(e: Exception):
    """
    Handles exceptions raised during API operations and logs them.
    """
    log_error(str(e))
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="An unexpected error occurred."
    )
```