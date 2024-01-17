```python
import os
from typing import List

def read_file_lines(file_path: str) -> List[str]:
    """
    Reads a file and returns a list of its lines.
    
    :param file_path: Path to the file to be read.
    :return: List of lines in the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def write_file_lines(file_path: str, lines: List[str]):
    """
    Writes a list of lines to a file.
    
    :param file_path: Path to the file to be written.
    :param lines: List of lines to write to the file.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def list_files_in_directory(directory_path: str) -> List[str]:
    """
    Lists all files in a given directory.
    
    :param directory_path: Path to the directory.
    :return: List of file paths.
    """
    return [os.path.join(directory_path, file) for file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, file))]

def list_python_files(directory_path: str) -> List[str]:
    """
    Lists all Python (.py) files in a given directory.
    
    :param directory_path: Path to the directory.
    :return: List of Python file paths.
    """
    return [file for file in list_files_in_directory(directory_path) if file.endswith('.py')]

def create_directory_if_not_exists(directory_path: str):
    """
    Creates a directory if it does not exist.
    
    :param directory_path: Path to the directory to be created.
    """
    os.makedirs(directory_path, exist_ok=True)

def get_file_extension(file_path: str) -> str:
    """
    Returns the file extension for a given file path.
    
    :param file_path: Path to the file.
    :return: File extension.
    """
    _, file_extension = os.path.splitext(file_path)
    return file_extension

def is_python_file(file_path: str) -> bool:
    """
    Checks if a file is a Python file based on its extension.
    
    :param file_path: Path to the file.
    :return: True if the file is a Python file, False otherwise.
    """
    return get_file_extension(file_path) == '.py'
```