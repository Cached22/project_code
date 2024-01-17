from flask import request, jsonify
from openai_utils.generate_response import generate_response
from web.utils.web_error_handling import handle_errors
from web.utils.web_utils import validate_prompt

class OpenAIController:
    @staticmethod
    @handle_errors
    def generate_openai_response():
        data = request.get_json()
        prompt = data.get('prompt', '')

        if not validate_prompt(prompt):
            return jsonify({"error": "Invalid prompt provided."}), 400

        response = generate_response(prompt)
        return jsonify({"response": generate_response}), 200

# Utility function to validate the prompt
def validate_prompt(prompt):
    return isinstance(prompt, str) and len(prompt) > 0
