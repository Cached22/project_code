from fastapi import APIRouter, HTTPException, UploadFile, File
from review.review_code import review_code
from utils.file_operations import save_temp_file
from utils.response_utils import create_review_report

router = APIRouter()

@router.post("/review")
async def review_code_endpoint(file: UploadFile = File(...)):
    try:
        # Save the uploaded file temporarily
        file_path = await save_temp_file(file)
        
        # Review the code
        review_results = review_code(file_path)
        
        # Generate a review report
        report = create_review_report(review_results)
        
        # Return the review report
        return report
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))