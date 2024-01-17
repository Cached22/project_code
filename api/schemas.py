from pydantic import BaseModel

class AnalysisReport(BaseModel):
    total_lines: int
    lines_of_code: int
    comments: int
    blank_lines: int
    functions: int
    classes: int
    cyclomatic_complexity: float
    maintainability_index: float

class EnhancementReport(BaseModel):
    original_code: str
    enhanced_code: str
    readability_improvements: int
    simplifications_made: int
    comments_added: int
    refactoring_details: str

class ReviewReport(BaseModel):
    syntax_errors: list
    code_smells: list
    potential_bugs: list
    style_violations: list
    security_vulnerabilities: list
    performance_issues: list

class LearningResult(BaseModel):
    structure_observations: str
    style_observations: str
    pattern_observations: str
    best_practices_observations: str

class GPTResponse(BaseModel):
    prompt: str
    response: str

class ProjectMetadata(BaseModel):
    project_name: str
    analysis_report: AnalysisReport
    enhancement_report: EnhancementReport
    review_report: ReviewReport
    learning_result: LearningResult
    gpt_response: GPTResponse

class ErrorResponse(BaseModel):
    error_message: str
    error_code: int
    error_details: str

# Define a schema for the input data expected from the user
class CodeAnalysisInput(BaseModel):
    file_path: str

class CodeEnhancementInput(BaseModel):
    code: str

class CodeReviewInput(BaseModel):
    code: str

class LearningFromCodeInput(BaseModel):
    code: str

class OpenAIResponseInput(BaseModel):
    prompt: str
