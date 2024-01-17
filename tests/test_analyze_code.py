```python
import unittest
from analysis.analyze_code import analyze_code
from utils.file_operations import read_file

class TestAnalyzeCode(unittest.TestCase):

    def setUp(self):
        # Setup code can be added here if needed
        pass

    def test_analyze_code_with_valid_file(self):
        # Assuming a valid Python file path is provided
        file_path = 'path/to/valid_python_file.py'
        file_content = read_file(file_path)
        analysis_result = analyze_code(file_path)

        # Check if the result is a dictionary
        self.assertIsInstance(analysis_result, dict)

        # Check if all required keys are in the result
        required_keys = [
            'total_lines', 'lines_of_code', 'comments', 
            'blank_lines', 'functions', 'classes', 
            'cyclomatic_complexity', 'maintainability_index'
        ]
        for key in required_keys:
            self.assertIn(key, analysis_result)

        # Check if the values are of correct type
        self.assertIsInstance(analysis_result['total_lines'], int)
        self.assertIsInstance(analysis_result['lines_of_code'], int)
        self.assertIsInstance(analysis_result['comments'], int)
        self.assertIsInstance(analysis_result['blank_lines'], int)
        self.assertIsInstance(analysis_result['functions'], int)
        self.assertIsInstance(analysis_result['classes'], int)
        self.assertIsInstance(analysis_result['cyclomatic_complexity'], int)
        self.assertIsInstance(analysis_result['maintainability_index'], float)

    def test_analyze_code_with_invalid_file(self):
        # Assuming an invalid file path is provided
        file_path = 'path/to/invalid_file.txt'
        with self.assertRaises(ValueError):
            analyze_code(file_path)

    def test_analyze_code_with_nonexistent_file(self):
        # Assuming a nonexistent file path is provided
        file_path = 'path/to/nonexistent_file.py'
        with self.assertRaises(FileNotFoundError):
            analyze_code(file_path)

    def tearDown(self):
        # Tear down code can be added here if needed
        pass

if __name__ == '__main__':
    unittest.main()
```