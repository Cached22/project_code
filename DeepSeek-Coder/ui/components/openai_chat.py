import tkinter as tk
from tkinter import scrolledtext
import requests
import json

class OpenAIChatComponent:
    def __init__(self, master):
        self.master = master
        self.create_chat_ui()

    def create_chat_ui(self):
        self.chat_frame = tk.Frame(self.master, bg='white')
        self.chat_frame.pack(fill=tk.BOTH, expand=True)

        self.chat_box = scrolledtext.ScrolledText(self.chat_frame, state='disabled', wrap=tk.WORD)
        self.chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.message_entry = tk.Entry(self.chat_frame, bd=2, width=50)
        self.message_entry.pack(side=tk.LEFT, padx=(10, 0), pady=10, fill=tk.X, expand=True)

        self.send_button = tk.Button(self.chat_frame, text='Send', command=self.send_message)
        self.send_button.pack(side=tk.RIGHT, padx=(0, 10), pady=10)

    def send_message(self):
        user_input = self.message_entry.get()
        if user_input:
            self.display_message("You: " + user_input)
            self.message_entry.delete(0, tk.END)
            self.get_response_from_openai(user_input)

    def display_message(self, message):
        self.chat_box.config(state='normal')
        self.chat_box.insert(tk.END, message + '\n')
        self.chat_box.yview(tk.END)
        self.chat_box.config(state='disabled')

    def get_response_from_openai(self, user_input):
        # Replace 'your_openai_api_key' with your actual OpenAI API key
        api_key = 'your_openai_api_key'
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        data = {
            'model': 'text-davinci-003',  # or another model name
            'prompt': user_input,
            'max_tokens': 150
        }
        response = requests.post('https://api.openai.com/v1/engines/davinci/completions', headers=headers, json=data)
        if response.status_code == 200:
            openai_response = response.json()
            self.display_message("DeepSeeker: " + openai_response['choices'][0]['text'].strip())
        else:
            self.display_message("DeepSeeker: I'm sorry, I can't connect to the AI right now.")