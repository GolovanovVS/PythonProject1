import tkinter as tk
from tkinter import font
from statistics import Statistics
from text import Text
import texts.english
import texts.russian
import random
import json


class TypingTrainer:
    def __init__(self, root):
        self.root = root
        self.exercise = ''
        self.text = Text()
        self.root.title("Typing Trainer")
        window_width = 800
        window_height = 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.root.geometry(f'{window_width}x{window_height}+{x}+{y}')
        self.stat = Statistics()
        self.start_ui()

    def start_ui(self):
        label = tk.Label(self.root, text="Choose an exercise")
        button_en = tk.Button(self.root, text="English", command=lambda: self.load_exercise('en'), width=20, height=3)
        button_ru = tk.Button(self.root, text="Russian", command=lambda: self.load_exercise('ru'), width=20, height=3)
        button_dig = tk.Button(self.root, text="Digits", command=lambda: self.load_exercise('dig'), width=20, height=3)
        label.pack()
        button_en.pack()
        button_ru.pack()
        button_dig.pack()

    def setup_ui(self):
        self.text_label = tk.Label(self.root, text="")
        self.text_label.pack()

        self.entry_var = tk.StringVar()
        self.entry_var.trace("w", self.on_type)
        self.entry = tk.Entry(self.root, textvariable=self.entry_var)
        self.entry.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def load_exercise(self, line: str):
        if line == 'en':
            self.exercise = self.text.load_exercise_en()
        if line == 'ru':
            self.exercise = self.text.load_exercise_ru()
        if line == 'dig':
            self.exercise = self.text.load_exercise_dig()
        for widget in self.root.winfo_children():
            widget.destroy()
        self.setup_ui()
        custom_font = font.Font(family="Helvetica", size=20, weight="bold")
        self.text_label.config(text=self.exercise, width=200, height=10, font=custom_font)
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
            self.entry.config(state='disabled')
