# Cryptography Assignment - 2
# Group - 40
# Isha Gohel - 2018B4A70454H
# Divyani Srivastava - 2018B4A71050H
# Shreya Srirampur - 2018B4A70886H

import datetime;

import implementDES
import Utility
from Record import Record


class Block:

# To create a block in the blockchain
    def __init__(self, record_list: list, prevHash: str, curr_transaction_info: Record, non=0):
        self.__non__ = non
        self.__curr_transaction_info__ = curr_transaction_info
        self.__prevHash__ = prevHash
        self.__timeStamp__ = datetime.datetime.now()
        self.__recordObject__ = record_list
        self.__hashBlock__ = self.hashCalculation()
        self.__desHash__ = ''

# Calculate hash using SHA256
    def hashCalculation(self) -> str:
        computedHash = Utility.useSha256(
            self.__prevHash__ + str(self.__non__))
        return computedHash

# Mining the block using Data encryption Standard(DES) 
    def mineBlock(self, difficulty: int) -> None:
        target = Utility.getDiffStr(difficulty)
        while not self.__hashBlock__[0:difficulty] == target:
            self.__non__ += 1
            self.__hashBlock__ = self.hashCalculation()
        computedHash = self.__hashBlock__.upper()
        firstTime = implementDES.encrypt(computedHash[0:16])
        secondTime = implementDES.encrypt(computedHash[16:32])
        thirdTime = implementDES.encrypt(computedHash[32:48])
        fourthTime = implementDES.encrypt(computedHash[48:64])
        self.__desHash__ = firstTime + secondTime + thirdTime + fourthTime
        print("Block has been mined!!!  DES is : " + self.__desHash__)

# Function for getting the previous Hash
    def getPrevHash(self) -> str:
        return self.__prevHash__

# Function for getting the hash for the block
    def getBlockHash(self) -> str:
        return self.__hashBlock__

# To find the time when the transaction information was stored
    def getTimeStamp(self) -> int:
        return self.__timeStamp__

# To get the lender's name from the block
    def lender_name(self) -> str:
        return self.__curr_transaction_info__.getLender()

# To get the patient's name from the block
    def borrower_name(self) -> str:
        return self.__curr_transaction_info__.getBorrower()

# To print the information
    def printInfo(self) -> None:
        self.__curr_transaction_info__.printInfo()
