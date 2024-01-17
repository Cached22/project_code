import unittest
from deepseeker.coder import CodeEnhancer

class TestCodeEnhancer(unittest.TestCase):

    def setUp(self):
        self.code_enhancer = CodeEnhancer()

    def test_enhance_code(self):
        original_code = "def hello_world():\n    print('Hello, world!')"
        enhanced_code = self.code_enhancer.enhance_code(original_code)
        self.assertNotEqual(original_code, enhanced_code, "Enhanced code should not be the same as the original code.")

    def test_enhance_code_with_invalid_input(self):
        with self.assertRaises(ValueError):
            self.code_enhancer.enhance_code(None)

    def test_enhance_code_with_empty_string(self):
        with self.assertRaises(ValueError):
            self.code_enhancer.enhance_code("")

if __name__ == '__main__':
    unittest.main()