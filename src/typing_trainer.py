import tkinter as tk

from src.graphic_editor import GraphicEditor


class TypingTrainer:
    def __init__(self):
        root = tk.Tk()
        GraphicEditor(root)
        root.mainloop()


TypingTrainer()
