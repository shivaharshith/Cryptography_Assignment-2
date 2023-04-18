# Cryptography Assignment - 2

# Information stored in Record
from User import User
class Record:

    def __init__(self):
        self.__lender__ = ''
        self.__borrower__ = ''
        self.__info__ = []
        self.__userobject__: User

    def addUsers(self, lender: str, borrower: str) -> None:
        self.__lender__ = lender
        self.__borrower__ = borrower

    def addUser(self, user_object: User) -> None:
        self.__userobject__ = user_object

    def addInfo(self, transactionInfo: str) -> None:
        self.__info__.append(transactionInfo)

    def getLender(self) -> str:
        return self.__lender__

    def getBorrower(self) -> str:
        return self.__borrower__

    def printInfo(self) -> None:
        for data in self.__info__:
            print(data)

    def getTotal(self) -> int:
        return self.__userobject__.__total__
