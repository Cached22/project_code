import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from .components.button import Button
from .components.text_input import TextInput
from .components.chat_box import ChatBox
from .components.openai_chat import OpenAIChat

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('DeepSeeker Coder')
        self.setGeometry(100, 100, 800, 600)
        self.initUI()

    def initUI(self):
        # Main layout
        layout = QVBoxLayout()

        # Chat box for OpenAI interactions
        self.chat_box = ChatBox()

        # OpenAI chat feature
        self.openai_chat = OpenAIChat(self.chat_box)

        # Button to clone the repository
        self.clone_button = Button('Clone Repository', self.clone_repo)

        # Button to review codebase
        self.review_button = Button('Review Codebase', self.review_codebase)

        # Button to enhance code
        self.enhance_button = Button('Enhance Code', self.enhance_code)

        # Add widgets to layout
        layout.addWidget(self.clone_button)
        layout.addWidget(self.review_button)
        layout.addWidget(self.enhance_button)
        layout.addWidget(self.chat_box)

        # Set the central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def clone_repo(self):
        # Logic to clone the repository
        self.openai_chat.send_message("Cloning the repository...")

    def review_codebase(self):
        # Logic to review the codebase
        self.openai_chat.send_message("Reviewing the codebase...")

    def enhance_code(self):
        # Logic to enhance the code
        self.openai_chat.send_message("Enhancing the code...")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())