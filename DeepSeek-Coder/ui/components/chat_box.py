from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton

class ChatBox(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        # Create layout
        layout = QVBoxLayout()

        # Create chat history area
        self.chat_history = QTextEdit()
        self.chat_history.setReadOnly(True)

        # Create chat input area
        self.chat_input = QTextEdit()
        self.chat_input.setFixedHeight(100)

        # Create send button
        self.send_button = QPushButton('Send')
        self.send_button.clicked.connect(self.on_send_clicked)

        # Add widgets to layout
        layout.addWidget(self.chat_history)
        layout.addWidget(self.chat_input)
        layout.addWidget(self.send_button)

        # Set layout to the QWidget
        self.setLayout(layout)

    def on_send_clicked(self):
        # Get text from chat input
        message = self.chat_input.toPlainText().strip()
        if message:
            # Add message to chat history
            self.chat_history.append(f"You: {message}")
            # Clear chat input
            self.chat_input.clear()
            # TODO: Implement sending message to OpenAI API and receiving response

    def add_message_to_history(self, sender, message):
        self.chat_history.append(f"{sender}: {message}")