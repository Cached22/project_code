```python
from flask import Blueprint, request, jsonify
from enhancement.enhance_code import enhance_code
from utils.web_error_handling import handle_enhancement_error
from utils.web_utils import allowed_file, read_file_content

web_enhancement_controller = Blueprint('web_enhancement_controller', __name__)

@web_enhancement_controller.route('/enhance', methods=['POST'])
def enhance():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        try:
            code_content = read_file_content(file)
            enhanced_code = enhance_code(code_content)
            return jsonify({'enhanced_code': enhanced_code}), 200
        except Exception as e:
            return handle_enhancement_error(e)

    return jsonify({'error': 'Unsupported file type'}), 400
```