# Cryptography Assignment - 2
# Group - 40
# Isha Gohel - 2018B4A70454H
# Divyani Srivastava - 2018B4A71050H
# Shreya Srirampur - 2018B4A70886H

# Information pertaining to a user
class User:

    def __init__(self):
        self.__userName__: str
        self.__password__: str

    def getName(self) -> str:
        return self.__userName__

    def setName(self, name: str) -> None:
        self.__userName__ = name

    def getPassword(self) -> str:
        return self.__password__

    def setPassword(self, password: str) -> None:
        self.__password__ = password
