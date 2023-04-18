# Cryptography Assignment - 2

# Information stored in Record
from User import User

class Record:

    def __init__(self):
        self.__lender__ = ''
        self.__borrower__ = ''
        self.__info__ = []
        self.__lender_object__: User
        self.__borrower_object__: User

    def addUsers(self, lender: str, borrower: str) -> None:
        self.__lender__ = lender
        self.__borrower__ = borrower

    def addLender(self, user_object: User) -> None:
        self.__lender_object__ = user_object

    def addBorrower(self, user_object: User) -> None:
        self.__borrower_object__ = user_object

    def addInfo(self, transactionInfo: str) -> None:
        self.__info__.append(transactionInfo)

    def getLender(self) -> str:
        return self.__lender__

    def getBorrower(self) -> str:
        return self.__borrower__

    def printInfo(self) -> None:
        for data in self.__info__:
            print(data)

    def getLenderTotal(self) -> int:
        return self.__lender_object__.__total__

    def getBorrowerTotal(self) -> int:
        return self.__borrower_object__.__total__
