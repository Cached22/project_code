from fastapi import APIRouter, HTTPException, UploadFile, File
from enhancement.enhance_code import enhance_code
from utils.file_operations import save_temp_file
from utils.documentation_utils import generate_enhancement_report
from data.output.enhancements import ENHANCEMENTS_FOLDER_PATH

router = APIRouter()

@router.post("/enhance")
async def enhance_code_endpoint(code_file: UploadFile = File(...)):
    try:
        # Save the uploaded file temporarily
        file_path = await save_temp_file(code_file)

        # Read the content of the code file
        with open(file_path, 'r') as file:
            code_content = file.read()

        # Enhance the code
        enhanced_code = enhance_code(code_content)

        # Generate a report for the enhancement
        report = generate_enhancement_report(enhanced_code)

        # Save the enhanced code to a file
        enhanced_file_path = f"{ENHANCEMENTS_FOLDER_PATH}/{code_file.filename}"
        with open(enhanced_file_path, 'w') as file:
            file.write(enhanced_code)

        return {
            "message": "Code enhancement completed successfully.",
            "enhanced_code": enhanced_code,
            "report": report
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))