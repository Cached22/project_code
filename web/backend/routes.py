from flask import Blueprint, request, jsonify
from web.backend.controllers.web_analysis_controller import analyze_code
from web.backend.controllers.web_enhancement_controller import enhance_code
from web.backend.controllers.web_review_controller import review_code
from web.backend.controllers.web_learning_controller import learn_from_code
from web.backend.controllers.web_openai_controller import generate_response
from web.backend.utils.web_error_handling import handle_errors

routes = Blueprint('routes', __name__)

@routes.route('/analyze', methods=['POST'])
@handle_errors
def web_analyze_code():
    file_path = request.form.get('file_path')
    result = analyze_code(file_path)
    return jsonify(result), 200

@routes.route('/enhance', methods=['POST'])
@handle_errors
def web_enhance_code():
    code = request.form.get('code')
    result = enhance_code(code)
    return jsonify(result), 200

@routes.route('/review', methods=['POST'])
@handle_errors
def web_review_code():
    code = request.form.get('code')
    result = review_code(code)
    return jsonify(result), 200

@routes.route('/learn', methods=['POST'])
@handle_errors
def web_learn_from_code():
    code = request.form.get('code')
    result = learn_from_code(code)
    return jsonify(result), 200

@routes.route('/generate-response', methods=['POST'])
@handle_errors
def web_generate_openai_response():
    prompt = request.form.get('prompt')
    result = generate_response(prompt)
    return jsonify(result), 200
