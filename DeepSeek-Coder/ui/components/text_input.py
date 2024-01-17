from tkinter import Entry, Frame, Label

class TextInput(Frame):
    def __init__(self, parent, label_text, entry_var, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.label = Label(self, text=label_text)
        self.label.pack(side="left", padx=(0, 10))

        self.entry = Entry(self, textvariable=entry_var)
        self.entry.pack(side="right", expand=True, fill="x")

    def get(self):
        return self.entry.get()

    def set(self, text):
        self.entry.delete(0, "end")
        self.entry.insert(0, text)

    def clear(self):
        self.entry.delete(0, "end")