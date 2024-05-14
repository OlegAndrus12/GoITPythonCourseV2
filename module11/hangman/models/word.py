from __future__ import annotations

import random

from constants import FILENAME_MAPPING


class Word:
    def __init__(self, letters):
        word_file = FILENAME_MAPPING.get(letters, 5)
        with open(word_file, mode="r") as file_stream:
            word_string = random.choice(file_stream.readlines())

        word = list(word_string)

        self.__word = word
        self.__guessed_word = ["_"] * letters
        self.__guessed_letters = set([])
        self.__missed_letters = []

    def check_letter(self, letter):
        contains_letter = False

        for i in range(len(self.__word)):
            if self.__word[i] == letter:
                contains_letter = True
                self.__guessed_word[i] = letter

        if not contains_letter:
            self.__missed_letters.append(letter)

        self.__guessed_letters.add(letter)
        return contains_letter

    def if_won(self):
        return self.__guessed_word == self.__word

    def get_guessed_word(self):
        return self.__guessed_word

    def get_word(self):
        return self.__word

    def get_guessed_letters(self):
        return self.__guessed_letters

    def get_missed_letters(self):
        return self.__missed_letters  # and this is a list btw
