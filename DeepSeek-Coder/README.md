# DeepSeek-Coder

DeepSeek-Coder is an application designed to clone the main branch of a project code, review the codebase, and enhance the project code using the DeepSeeker Coder AI. It features a user interface with buttons and OpenAI chat capabilities, providing an intuitive user experience for code enhancement and review.

## Features

- Clone the main branch of a project from a Git repository.
- Review the codebase with AI-powered insights.
- Enhance code using DeepSeeker Coder AI suggestions.
- User Interface with:
  - Buttons to perform actions like cloning, reviewing, and enhancing code.
  - OpenAI chat feature to interact with the AI for code suggestions.
- Local run capability for easy setup and use.

## Getting Started

To get started with DeepSeek-Coder, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/deepseek-ai/DeepSeek-Coder.git
   ```
2. Navigate to the project directory:
   ```
   cd DeepSeek-Coder
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the setup script:
   ```
   python setup.py install
   ```
5. Start the UI locally:
   ```
   sh scripts/start_ui.sh
   ```

## Usage

Once the application is running, you can use the UI to clone a project, review the codebase, and interact with the DeepSeeker Coder AI for code enhancement.

- Use the **Clone** button to clone a project's main branch.
- Click on **Review Code** to have the AI review the codebase.
- Interact with the AI through the OpenAI chat feature for code suggestions and enhancements.

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for details on how to contribute to the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI for providing the GPT models.
- Contributors and maintainers of DeepSeek-Coder.

For more information on the project structure and specific files, please refer to the respective files in the repository:

- [requirements.txt](requirements.txt) for dependencies.
- [setup.py](setup.py) for installation setup.
- [main.py](deepseeker/main.py) as the main application entry point.
- [coder.py](deepseeker/coder.py) for core logic.
- [utils.py](deepseeker/utils.py) for utility functions.
- [model_loader.py](deepseeker/models/model_loader.py) for model handling.
- [data_processor.py](deepseeker/data/data_processor.py) for data processing.
- [api_handler.py](deepseeker/api/api_handler.py) for API handling.
- [main_window.py](ui/main_window.py) for the main window UI logic.
- [button.py](ui/components/button.py), [text_input.py](ui/components/text_input.py), [chat_box.py](ui/components/chat_box.py), [openai_chat.py](ui/components/openai_chat.py) for UI components.
- Test scripts in the [tests](tests) directory.
- Docker configuration in the [docker](docker) directory.
- Utility scripts in the [scripts](scripts) directory.

Enjoy using DeepSeek-Coder for your code enhancement needs!