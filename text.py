import json
import os
import pwd
import re
from pathlib import Path


class Text:
    def read_files(self):
        cur_path = Path(__file__).parent
        target = cur_path / 'texts'
        for file in target.rglob('*.txt'):
            self.sentences += file.read_text().split('.')

    def processing_file(self, file):
        with open(file, 'r') as f:
            data = f.read()

    def load_exercises(self):
        with open('default_exercises.json', 'r') as f:
            exercises = json.load(f)
        return exercises
