from fastapi import APIRouter
from api.controllers.analysis_controller import analyze_code
from api.controllers.enhancement_controller import enhance_code
from api.controllers.review_controller import review_code
from api.controllers.learning_controller import learn_from_code
from api.controllers.openai_controller import generate_response
from api.dependencies import get_query_token, get_payload

router = APIRouter()

@router.post("/analyze", dependencies=[Depends(get_query_token)])
async def analyze_code_route(file_path: str = Depends(get_payload)):
    return analyze_code(file_path)

@router.post("/enhance", dependencies=[Depends(get_query_token)])
async def enhance_code_route(code: str = Depends(get_payload)):
    return enhance_code(code)

@router.post("/review", dependencies=[Depends(get_query_token)])
async def review_code_route(code: str = Depends(get_payload)):
    return review_code(code)

@router.post("/learn", dependencies=[Depends(get_query_token)])
async def learn_from_code_route(code: str = Depends(get_payload)):
    return learn_from_code(code)

@router.post("/generate-response", dependencies=[Depends(get_query_token)])
async def generate_response_route(prompt: str = Depends(get_payload)):
    return generate_response(prompt)