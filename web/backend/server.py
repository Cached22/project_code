from flask import Flask, request, jsonify
from web.backend.controllers.web_analysis_controller import analyze_code
from web.backend.controllers.web_enhancement_controller import enhance_code
from web.backend.controllers.web_review_controller import review_code
from web.backend.controllers.web_learning_controller import learn_from_code
from web.backend.controllers.web_openai_controller import generate_response
from web.backend.middleware.web_security import setup_security
from web.backend.middleware.web_validation import validate_request
from web.backend.utils.web_error_handling import handle_errors

app = Flask(__name__)

# Setup middleware
setup_security(app)
app.register_error_handler(Exception, handle_errors)

@app.route('/analyze', methods=['POST'])
def web_analyze_code():
    data = request.get_json()
    file_path = data.get('file_path')
    return jsonify(analyze_code(file_path))

@app.route('/enhance', methods=['POST'])
def web_enhance_code():
    data = request.get_json()
    code = data.get('code')
    return jsonify(enhance_code(code))

@app.route('/review', methods=['POST'])
def web_review_code():
    data = request.get_json()
    code = data.get('code')
    return jsonify(review_code(code))

@app.route('/learn', methods=['POST'])
def web_learn_from_code():
    data = request.get_json()
    code = data.get('code')
    return jsonify(learn_from_code(code))

@app.route('/generate-response', methods=['POST'])
def web_generate_openai_response():
    data = request.get_json()
    prompt = data.get('prompt')
    return jsonify(generate_response(prompt))

@app.route('/')
def index():
    return "Welcome to the Code Analysis and Enhancement Tool"

if __name__ == '__main__':
    app.run(debug=True)