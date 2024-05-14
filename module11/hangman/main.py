from __future__ import annotations

import random

import console_printing
from models.man import Man
from models.word import Word


def main():
    letters = random.randint(5, 7)

    word = Word(letters)
    man = Man()

    while not man.isGameOver() and not word.if_won():
        console_printing.refresh(word, man)
        guess = console_printing.get_guess(word, man)

        if word.check_letter(guess):
            console_printing.refresh(word, man)
            console_printing.correct_guess()

        else:
            man.addBodyPart()
            console_printing.refresh(word, man)
            console_printing.incorrect_guess()

    if word.if_won():
        console_printing.winning_message(word)

    else:
        console_printing.losing_message(word)


if __name__ == "__main__":
    main()
