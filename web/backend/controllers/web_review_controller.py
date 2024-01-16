from flask import request, jsonify, Blueprint
from review.review_code import review_code
from utils.web_error_handling import handle_web_error
from utils.web_utils import allowed_file, save_temp_file
from utils.response_utils import success_response, failure_response
from config.settings import REVIEWS_FOLDER_PATH

web_review_controller = Blueprint('web_review_controller', __name__)

@web_review_controller.route('/review', methods=['POST'])
def web_review_code():
    if 'file' not in request.files:
        return handle_web_error('No file part in the request', 400)

    file = request.files['file']
    if file.filename == '':
        return handle_web_error('No selected file', 400)

    if file and allowed_file(file.filename):
        try:
            # Save the file temporarily to analyze
            file_path = save_temp_file(file)
            
            # Perform code review
            review_result = review_code(file_path)
            
            # Save the review result to a file
            review_file_path = f"{REVIEWS_FOLDER_PATH}/review_{file.filename}.json"
            with open(review_file_path, 'w') as review_file:
                review_file.write(json.dumps(review_result))
            
            return success_response(review_result, 'Code review completed successfully')
        except Exception as e:
            return handle_web_error(str(e), 500)
    else:
        return handle_web_error('File type not allowed', 400)