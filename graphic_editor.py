import tkinter as tk
from statistics import Statistics
from text import Text
import texts.english
import texts.russian
import random
import json


class TypingTrainer:
    def __init__(self, root):
        self.root = root
        self.stat = Statistics()
        self.setup_ui()
        self.text = Text()
        self.exercise = self.text.load_exercise()
        self.text_label.config(text=self.exercise)
        self.entry_var.set("")
        self.stat.start_exercise()

    def setup_ui(self):
        self.text_label = tk.Label(self.root, text="")
        self.text_label.pack()

        self.entry_var = tk.StringVar()
        self.entry_var.trace("w", self.on_type)
        self.entry = tk.Entry(self.root, textvariable=self.entry_var)
        self.entry.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def load_exercise(self):
        if self.language == 'en':
            self.exercise = random.choice(texts.english.Sentences)
        if self.language == 'ru':
            self.exercise = random.choice(texts.russian.Sentences)
        self.text_label.config(text=self.exercise)
        self.entry_var.set("")
        self.stat.start_exercise()

    def on_type(self, *args):
        current_text = self.entry_var.get()
        if not self.exercise.startswith(current_text):
            self.stat.total_errors += 1
            self.entry_var.set(current_text[:-1])
        if self.exercise == current_text:
            result_text = self.stat.finish_exercise(len(self.exercise))
            self.result_label.config(text=result_text)
            self.text_label.config(text="Упражнения завершены!")
            self.entry.config(state='disabled')  # Отключаем ввод, если упражнения закончились
