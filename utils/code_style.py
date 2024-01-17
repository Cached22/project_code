```python
import subprocess
import os
from flake8.api import legacy as flake8

def check_code_style(file_path):
    """
    Check for code style violations in the given file using flake8.

    Parameters:
    file_path (str): The path to the file to be checked.

    Returns:
    dict: A dictionary containing the number of style errors and a list of error messages.
    """
    style_errors = []
    try:
        # Run flake8 on the given file to check for PEP 8 violations
        style_guide = flake8.get_style_guide(ignore=['E501'])
        report = style_guide.check_files([file_path])
        for error in report.get_statistics('E'):
            style_errors.append(error)
        return {
            'error_count': report.total_errors,
            'errors': style_errors
        }
    except Exception as e:
        return {
            'error_count': -1,
            'errors': [str(e)]
        }

def auto_correct_code_style(file_path):
    """
    Automatically correct code style violations in the given file using autopep8.

    Parameters:
    file_path (str): The path to the file to be corrected.

    Returns:
    bool: True if autopep8 made changes to the file, False otherwise.
    """
    original_content = ''
    with open(file_path, 'r') as file:
        original_content = file.read()

    # Run autopep8 on the file to automatically fix PEP 8 violations
    subprocess.run(['autopep8', '--in-place', '--aggressive', '--aggressive', file_path], check=True)

    with open(file_path, 'r') as file:
        new_content = file.read()

    return original_content != new_content

def format_code(file_path):
    """
    Format code using the black formatter.

    Parameters:
    file_path (str): The path to the file to be formatted.

    Returns:
    bool: True if black made changes to the file, False otherwise.
    """
    original_content = ''
    with open(file_path, 'r') as file:
        original_content = file.read()

    # Run black on the file to format it
    subprocess.run(['black', file_path], check=True)

    with open(file_path, 'r') as file:
        new_content = file.read()

    return original_content != new_content

def sort_imports(file_path):
    """
    Sort imports in a Python file using isort.

    Parameters:
    file_path (str): The path to the file where imports will be sorted.

    Returns:
    bool: True if isort made changes to the file, False otherwise.
    """
    original_content = ''
    with open(file_path, 'r') as file:
        original_content = file.read()

    # Run isort on the file to sort the imports
    subprocess.run(['isort', file_path], check=True)

    with open(file_path, 'r') as file:
        new_content = file.read()

    return original_content != new_content
```