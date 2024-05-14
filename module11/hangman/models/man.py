from __future__ import annotations

from constants import BODY_PARTS


class Man:
    def __init__(self):
        self.__body = []

    def addBodyPart(self):
        print(BODY_PARTS)
        self.__body.append(BODY_PARTS[len(self.__body)])

    def isGameOver(self):
        return len(self.__body) == 6

    def head(self):
        if len(self.__body) > 0:
            return self.__body[0]

        return " "

    def abdomen(self):
        if len(self.__body) > 1:
            return self.__body[1]

        return " "

    def leftArm(self):
        if len(self.__body) > 2:
            return self.__body[2]

        return " "

    def rightArm(self):
        if len(self.__body) > 3:
            return self.__body[3]

        return " "

    def leftLeg(self):
        if len(self.__body) > 4:
            return self.__body[4]

        return " "

    def rightLeg(self):
        if len(self.__body) > 5:
            return self.__body[5]

        return " "
