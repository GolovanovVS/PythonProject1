import random

import texts.english


class Text:
    def load_exercise(self):
        while (True):
            print('Choose a language:')
            language = input('"en" if english, "ru" if russian \n')
            if language == 'en' or language == 'ru':
                break
        exercise = ''
        if language == 'en':
            exercise = random.choice(texts.english.Sentences)
        if language == 'ru':
            exercise = random.choice(texts.russian.Sentences)
        return exercise
