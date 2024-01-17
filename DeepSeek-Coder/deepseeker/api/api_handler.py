from flask import Flask, request, jsonify
from deepseeker.coder import enhance_code
from deepseeker.utils import clone_repository, get_codebase_review

app = Flask(__name__)

@app.route('/clone', methods=['POST'])
def clone_repo():
    data = request.json
    repo_url = data.get('repo_url', 'https://github.com/deepseek-ai/DeepSeek-Coder.git')
    branch = data.get('branch', 'main')
    try:
        clone_repository(repo_url, branch)
        return jsonify({"message": "Repository cloned successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/review', methods=['GET'])
def review_codebase():
    try:
        review = get_codebase_review()
        return jsonify({"review": review}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/enhance', methods=['POST'])
def enhance_project_code():
    data = request.json
    code = data.get('code', '')
    try:
        enhanced_code = enhance_code(code)
        return jsonify({"enhanced_code": enhanced_code}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')