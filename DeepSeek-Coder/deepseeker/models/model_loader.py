```python
import torch
from transformers import AutoModel, AutoTokenizer

class ModelLoader:
    def __init__(self, model_name):
        self.model_name = model_name
        self.model = None
        self.tokenizer = None

    def load_model(self):
        """
        Loads the model and tokenizer for the given model name.
        """
        try:
            self.model = AutoModel.from_pretrained(self.model_name)
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            print(f"Model and tokenizer for '{self.model_name}' loaded successfully.")
        except Exception as e:
            print(f"An error occurred while loading the model: {e}")

    def get_model(self):
        """
        Returns the loaded model.
        """
        if self.model is None:
            self.load_model()
        return self.model

    def get_tokenizer(self):
        """
        Returns the loaded tokenizer.
        """
        if self.tokenizer is None:
            self.load_model()
        return self.tokenizer

# Example usage:
# model_loader = ModelLoader('bert-base-uncased')
# model = model_loader.get_model()
# tokenizer = model_loader.get_tokenizer()
```