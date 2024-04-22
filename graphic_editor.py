import tkinter as tk
from tkinter import simpledialog
from statistics import Statistics
import random
import time
import json


class TypingTrainer:
    def __init__(self, root):
        self.root = root
        self.stat = Statistics()
        self.setup_ui()
        self.load_exercise()

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
        try:
            with open('exercises.json', 'r') as f:
                self.all_exercises = json.load(f)
                self.exercises = random.choice(self.all_exercises)
        except FileNotFoundError:
            self.exercises = ["Пример текста для набора."]
        self.text_label.config(text=self.exercises)
        self.entry_var.set("")
        self.stat.start_exercise()

    def on_type(self, *args):
        current_text = self.entry_var.get()
        if not self.exercises.startswith(current_text):
            self.stat.total_errors += 1
            self.entry_var.set(current_text[:-1])
        if self.exercises == current_text:
            result_text = self.stat.finish_exercise(len(self.exercises))
            self.result_label.config(text=result_text)
            self.text_label.config(text="Упражнения завершены!")
            self.entry.config(state='disabled')  # Отключаем ввод, если упражнения закончились
