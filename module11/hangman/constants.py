# https://docs.python.org/3/library/enum.html
from __future__ import annotations

from enum import Enum


class BodyPart(Enum):
    HEAD: "0"


FILENAME_MAPPING = {
    5: "words/fiveLetterWords.txt",
    6: "words/sixLetterWords.txt",
    7: "words/sevenLetterWords.txt",
}

SIGNS = ["0", "|", "/", "\\", "/", "\\"]
BODY_PARTS = {index: value for index, value in enumerate(SIGNS)}
