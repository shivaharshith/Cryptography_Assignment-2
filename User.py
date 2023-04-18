# Cryptography Assignment - 2

# Information pertaining to a user
class User:

    def __init__(self):
        self.__userName__: str
        self.__password__: str
        self.__total__   = 0

    def getName(self) -> str:
        return self.__userName__

    def setName(self, name: str) -> None:
        self.__userName__ = name

    def getPassword(self) -> str:
        return self.__password__

    def setPassword(self, password: str) -> None:
        self.__password__ = password

    def setTotal(self, total: str) -> None:
        self.__total__ = self.__total__ + int(total)
    