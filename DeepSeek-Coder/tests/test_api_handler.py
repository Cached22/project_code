import unittest
from unittest.mock import patch
from deepseeker.api.api_handler import APIHandler

class TestAPIHandler(unittest.TestCase):

    def setUp(self):
        self.api_handler = APIHandler()

    @patch('deepseeker.api.api_handler.requests')
    def test_clone_repository(self, mock_requests):
        mock_requests.get.return_value.ok = True
        response = self.api_handler.clone_repository('https://github.com/deepseek-ai/DeepSeek-Coder.git', 'main')
        self.assertTrue(response)
        mock_requests.get.assert_called_with('https://github.com/deepseek-ai/DeepSeek-Coder.git', params={'branch': 'main'})

    @patch('deepseeker.api.api_handler.requests')
    def test_clone_repository_failure(self, mock_requests):
        mock_requests.get.return_value.ok = False
        response = self.api_handler.clone_repository('https://github.com/deepseek-ai/DeepSeek-Coder.git', 'main')
        self.assertFalse(response)
        mock_requests.get.assert_called_with('https://github.com/deepseek-ai/DeepSeek-Coder.git', params={'branch': 'main'})

    @patch('deepseeker.api.api_handler.os')
    @patch('deepseeker.api.api_handler.subprocess')
    def test_review_codebase(self, mock_subprocess, mock_os):
        mock_os.path.exists.return_value = True
        mock_subprocess.check_output.return_value = b'Code review output'
        response = self.api_handler.review_codebase('/path/to/DeepSeek-Coder')
        self.assertEqual(response, 'Code review output')
        mock_subprocess.check_output.assert_called_with(['git', 'review', '/path/to/DeepSeek-Coder'], stderr=mock_subprocess.STDOUT)

    @patch('deepseeker.api.api_handler.os')
    def test_review_codebase_no_repo(self, mock_os):
        mock_os.path.exists.return_value = False
        with self.assertRaises(ValueError):
            self.api_handler.review_codebase('/path/to/nonexistent/repo')

if __name__ == '__main__':
    unittest.main()