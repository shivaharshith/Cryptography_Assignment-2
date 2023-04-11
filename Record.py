# Cryptography Assignment - 2
# Group - 40
# Isha Gohel - 2018B4A70454H
# Divyani Srivastava - 2018B4A71050H
# Shreya Srirampur - 2018B4A70886H

# Information stored in Record
class Record:

    def __init__(self):
        self.__doctor__ = ''
        self.__patient__ = ''
        self.__info__ = []

    def addUsers(self, doctor: str, patient: str) -> None:
        self.__doctor__ = doctor
        self.__patient__ = patient

    def addInfo(self, medicalInfo: str) -> None:
        self.__info__.append(medicalInfo)

    def getDoctor(self) -> str:
        return self.__doctor__

    def getPatient(self) -> str:
        return self.__patient__

    def printInfo(self) -> None:
        for data in self.__info__:
            print(data)
