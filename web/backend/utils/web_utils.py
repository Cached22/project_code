```python
import os
from utils.error_handling import handle_errors
from utils.file_operations import read_file_content
from config.settings import (
    PROJECTS_FOLDER_PATH,
    REPORTS_FOLDER_PATH,
    ERRORS_FOLDER_PATH,
    ENHANCEMENTS_FOLDER_PATH,
    REVIEWS_FOLDER_PATH,
    LEARNING_RESULTS_FOLDER_PATH,
    GPT_RESPONSES_FOLDER_PATH
)

def get_project_paths():
    """
    Retrieves the paths of all projects within the designated projects folder.
    """
    try:
        projects = [os.path.join(PROJECTS_FOLDER_PATH, name) for name in os.listdir(PROJECTS_FOLDER_PATH)]
        return [project for project in projects if os.path.isdir(project)]
    except Exception as e:
        handle_errors(e, ERRORS_FOLDER_PATH)
        return []

def save_report(report, report_type):
    """
    Saves the given report to the appropriate folder based on the report type.
    """
    try:
        report_folder = {
            'analysis': REPORTS_FOLDER_PATH,
            'enhancement': ENHANCEMENTS_FOLDER_PATH,
            'review': REVIEWS_FOLDER_PATH,
            'learning': LEARNING_RESULTS_FOLDER_PATH,
            'gpt_response': GPT_RESPONSES_FOLDER_PATH
        }.get(report_type, REPORTS_FOLDER_PATH)

        report_path = os.path.join(report_folder, f"{report['project_name']}_{report_type}_report.json")
        with open(report_path, 'w') as file:
            file.write(json.dumps(report, indent=4))
    except Exception as e:
        handle_errors(e, ERRORS_FOLDER_PATH)

def load_report(project_name, report_type):
    """
    Loads a report of the given type for the specified project.
    """
    try:
        report_folder = {
            'analysis': REPORTS_FOLDER_PATH,
            'enhancement': ENHANCEMENTS_FOLDER_PATH,
            'review': REVIEWS_FOLDER_PATH,
            'learning': LEARNING_RESULTS_FOLDER_PATH,
            'gpt_response': GPT_RESPONSES_FOLDER_PATH
        }.get(report_type, REPORTS_FOLDER_PATH)

        report_path = os.path.join(report_folder, f"{project_name}_{report_type}_report.json")
        if os.path.exists(report_path):
            return json.loads(read_file_content(report_path))
        else:
            return None
    except Exception as e:
        handle_errors(e, ERRORS_FOLDER_PATH)
        return None

def validate_file_extension(file_path, valid_extensions=['.py']):
    """
    Validates if the file has one of the valid extensions.
    """
    _, file_extension = os.path.splitext(file_path)
    return file_extension in valid_extensions
```