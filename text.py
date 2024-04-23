import random

import texts


class Text:
    def load_exercise_en(self):
        exercise = random.choice(texts.english.Sentences)
        return exercise

    def load_exercise_ru(self):
        exercise = random.choice(texts.russian.Sentences)
        return exercise

    def load_exercise_dig(self):
        exercise = random.choice(texts.english.Sentences)
        return exercise
