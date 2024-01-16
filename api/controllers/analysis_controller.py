from fastapi import APIRouter, HTTPException
from analysis.analyze_code import analyze_code
from utils.file_operations import read_file_content
from utils.error_handling import handle_errors
from schemas import AnalysisReport

router = APIRouter()

@router.post("/analyze", response_model=AnalysisReport)
async def analyze_code_endpoint(file_path: str):
    try:
        # Read the content of the file
        file_content = read_file_content(file_path)
        
        # Analyze the code
        analysis_results = analyze_code(file_content)
        
        # Create an AnalysisReport object
        report = AnalysisReport(
            total_lines=analysis_results['total_lines'],
            lines_of_code=analysis_results['lines_of_code'],
            comments=analysis_results['comments'],
            blank_lines=analysis_results['blank_lines'],
            functions=analysis_results['functions'],
            classes=analysis_results['classes'],
            cyclomatic_complexity=analysis_results['cyclomatic_complexity'],
            maintainability_index=analysis_results['maintainability_index']
        )
        
        return report
    except Exception as e:
        # Use a custom error handler to format the exception properly
        handle_errors(e)
        raise HTTPException(status_code=500, detail=str(e))