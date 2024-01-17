# DeepSeek-Coder/ui/__init__.py

from .main_window import MainWindow
from .components.button import Button
from .components.text_input import TextInput
from .components.chat_box import ChatBox
from .components.openai_chat import OpenAIChat

# Initialize the UI components when the package is imported
def init_ui():
    main_window = MainWindow()
    return main_window

# This allows the UI to be run with `python -m DeepSeek-Coder.ui`
if __name__ == "__main__":
    main_window = init_ui()
    main_window.run()