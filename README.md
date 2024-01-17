# Code Analysis and Enhancement Tool (CAET)

CAET is a comprehensive application designed to assist developers in analyzing, enhancing, reviewing, and learning from their code. It provides a suite of tools to improve code quality and maintainability.

## Features

- **Code Analysis**: Analyze code files to extract metrics such as line counts, comment counts, function and class counts, cyclomatic complexity, and maintainability index.
- **Code Enhancement**: Automatically enhance code readability, simplify structures, and add comments to complex code sections.
- **Code Review**: Review code for syntax errors, code smells, potential bugs, style violations, security vulnerabilities, and performance issues.
- **Continuous Learning**: Learn from code patterns, structures, styles, and best practices.
- **OpenAI Utils**: Utilize OpenAI's GPT-4 Turbo to analyze and write new code based on user prompts.
- **Project Comparison**: Compare 10 or more projects within a single folder, providing detailed analysis and reports.

## Installation

To set up the CAET application, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/your-repository/caet.git
   ```
2. Navigate to the project directory:
   ```
   cd caet
   ```
3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the installation scripts (if any):
   ```
   sh scripts/install_dependencies.sh
   ```

## Usage

To use the application, run the `main.py` script and follow the prompts:

```
python main.py
```

You can also use the provided shell scripts to run specific parts of the application:

- Analyze code: `sh scripts/run_analysis.sh`
- Enhance code: `sh scripts/run_enhancements.sh`
- Review code: `sh scripts/run_reviews.sh`
- Learn from code: `sh scripts/run_learning.sh`
- Use OpenAI Utils: `sh scripts/run_openai_utils.sh`

## Documentation

For detailed documentation on each module and function, refer to the docstrings within the code files. The main functions and their purposes are:

- `analyze_code`: Located in `analysis/analyze_code.py`
- `enhance_code`: Located in `enhancement/enhance_code.py`
- `review_code`: Located in `review/review_code.py`
- `learn_from_code`: Located in `learning/learn_from_code.py`
- `generate_response`: Located in `openai_utils/generate_response.py`
- `main`: The entry point of the application in `main.py`

## Contributing

Contributions to CAET are welcome. Please read `CONTRIBUTING.md` for guidelines on how to submit pull requests.

## License

CAET is released under the MIT License. See `LICENSE` for more information.

## Support

For support, please open an issue in the GitHub issue tracker or contact the maintainers directly.

## Acknowledgments

This project utilizes several open-source libraries listed in `requirements.txt`. We thank the open-source community for their valuable contributions.