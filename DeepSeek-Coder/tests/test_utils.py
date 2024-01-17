import unittest
from deepseeker.utils import clone_repository, review_codebase

class TestUtils(unittest.TestCase):

    def test_clone_repository(self):
        # Assuming clone_repository returns the path to the cloned repository
        repo_url = "https://github.com/deepseek-ai/DeepSeek-Coder.git"
        cloned_path = clone_repository(repo_url)
        self.assertTrue(os.path.isdir(cloned_path))
        self.assertTrue(os.path.isdir(os.path.join(cloned_path, '.git')))

    def test_review_codebase(self):
        # Assuming review_codebase returns a dictionary with review details
        repo_path = "/path/to/cloned/DeepSeek-Coder"
        review_results = review_codebase(repo_path)
        self.assertIsInstance(review_results, dict)
        self.assertIn('summary', review_results)
        self.assertIn('details', review_results)

if __name__ == '__main__':
    unittest.main()