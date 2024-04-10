import tkinter as tk
from tkinter import simpledialog
import time
import json


class TypingTrainer:
    def __init__(self, root):
        self.root = root
        self.setup_ui()
        self.load_exercises()
        self.current_exercise_index = 0  # Добавляем индекс для текущего упражнения
        self.display_current_exercise()
        self.start_time = 0
        self.total_errors = 0

    def setup_ui(self):
        self.text_label = tk.Label(self.root, text="")
        self.text_label.pack()

        self.entry_var = tk.StringVar()
        self.entry_var.trace("w", self.on_type)
        self.entry = tk.Entry(self.root, textvariable=self.entry_var)
        self.entry.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def load_exercises(self):
        try:
            with open('exercises.json', 'r') as f:
                self.exercises = json.load(f)
        except FileNotFoundError:
            self.exercises = ["Пример текста для набора."]

    def display_current_exercise(self):
        self.current_exercise = self.exercises[self.current_exercise_index]
        self.text_label.config(text=self.current_exercise)
        self.entry_var.set("")
        self.start_exercise()

    def on_type(self, *args):
        current_text = self.entry_var.get()
        if not self.current_exercise.startswith(current_text):
            self.total_errors += 1
            self.entry_var.set(current_text[:-1])
        if self.current_exercise == current_text:
            self.finish_exercise()

    def start_exercise(self):
        self.start_time = time.time()
        self.total_errors = 0

    def finish_exercise(self):
        end_time = time.time()
        typing_speed = len(self.current_exercise) / (end_time - self.start_time) * 60
        result_text = f"Ошибок: {self.total_errors}, Скорость: {typing_speed:.2f} символов в минуту."
        self.result_label.config(text=result_text)
        self.current_exercise_index += 1  # Переходим к следующему упражнению
        if self.current_exercise_index < len(self.exercises):
            self.display_current_exercise()
        else:
            self.text_label.config(text="Упражнения завершены!")
            self.entry.config(state='disabled')  # Отключаем ввод, если упражнения закончились


if __name__ == "__main__":
    root = tk.Tk()
    trainer = TypingTrainer(root)
    root.mainloop()
