import random
import texts.english
import texts.russian
import texts.digits


class Text:
    @staticmethod
    def load_exercise_en():
        exercise = random.choice(texts.english.Sentences)
        return exercise

    @staticmethod
    def load_exercise_ru():
        exercise = random.choice(texts.russian.Sentences)
        return exercise

    @staticmethod
    def load_exercise_dig():
        exercise = random.choice(texts.digits.Sentences)
        return exercise
