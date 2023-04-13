# Cryptography Assignment - 2
#Evanston

import pickle
from os.path import exists

from Block import Block
from Record import Record
from User import User
from Utility import ZeroKnowledgeProof

# Defining necessary variables
difficulty = 4
previousHash = '0'
blockchain = []
records = []
users = []
doctors = []
p = 11
g = 2

# To ask the user if they want to import the previous data from the records
if exists('state'):
    while True:
        option = input('Previous data has been found... Would you like to import? (yes/no): ')
        if option == 'yes':
            with open('state', 'rb') as file:
                previousHash, blockchain, records, users, doctors = pickle.load(file)
            print('Import is Successful')
            break
        elif option == 'no':
            break
        else:
            print('Option is not recognised\n')


# To verify the transaction
def verifyTransaction(record_list: list, prevHash: str, info: Record) -> str:
    print('Trying to mineBlock...')
    block = Block(record_list, prevHash, info)
    block.mineBlock(difficulty)
    if verifyChain(block):
        blockchain.append(block)
    return block.getBlockHash()

# To verify if the previous block's hash is the previous hash for the next block
def verifyChain(block: Block) -> bool:
    for i in range(1, len(blockchain)):
        if not blockchain[i].getPrevHash() == blockchain[i-1].getBlockHash():
            return False
    if len(blockchain) > 0 and not blockchain[-1].getBlockHash() == block.getPrevHash():
        return False
    return True

# for viewing the records of the patients(Doctors can view all of their patient's medical records but the patient can only view their medical data)
def viewUser() -> None:
    val = input('Are you a doctor or patient? (doctor/patient): ')
    if val == 'doctor':
        doc = input('Enter your name: ')
        pwd = input('Enter your password: ')
        flag = False
        for doctor in doctors:
            if doctor.getName() == doc and doctor.getPassword() == pwd:
                for block in blockchain:
                    if block.doc_name() == doc:
                        print(
                            'Time at which data was recorded: ' + str(block.getTimeStamp()))
                        print('Doctor:' + doc)
                        print('Patient:' + block.patient_name())
                        print('His Medical Information:')
                        block.printInfo()
                        print()
                        flag = True
                if flag:
                    break
        if not flag:
            print('Doctor Not Found')
    elif val == 'patient':
        pat = input('Enter your name: ')
        y = 0
        for user in users:
            if user.getName() == pat:
                x = int(user.getPassword())
                y = pow(g, x, p)
        if not ZeroKnowledgeProof(y):
            return
        flag = False
        for user in users:
            if user.getName() == pat:
                for block in blockchain:
                    if block.patient_name() == pat:
                        print('Time: ' + str(block.getTimeStamp()))
                        print('Doctor:' + block.doc_name())
                        print('Patient:' + pat)
                        print("Patient's Medical Data:")
                        block.printInfo()
                        print()
                        flag = True
                if flag:
                    break
        if not flag:
            print('Patient Not Found')
    else:
        print('Option is not recognized')


if __name__ == '__main__':

# Functionalities like add/register/view added for the user
    choice = 'yes'
    while choice == 'yes':
        option = input('What do you want to do? (add/register/view): ')

        if option == 'register':
            option1 = input('Do you want to register as doctor or patient? (d/p): ')
            if option1 == 'p':
                name = input('Enter name: ')
                pwd = input('Enter password (integer only): ')
                pwd_v = input('Verify password: ')
                if pwd == pwd_v:
                    new_patient = User()
                    new_patient.setName(name)
                    new_patient.setPassword(pwd)
                    users.append(new_patient)
                else:
                    print('Password verification has failed')
            elif option1 == 'd':
                name = input('Enter name: ')
                pwd = input('Enter password (integer only): ')
                pwd_v = input('Verify password: ')
                if pwd == pwd_v:
                    new_doctor = User()
                    new_doctor.setName(name)
                    new_doctor.setPassword(pwd)
                    doctors.append(new_doctor)
                else:
                    print('Password verification has failed')
            else:
                print('Option is not recognised')

        elif option == 'add':
            doc_name = input('Enter the doctor name: ')
            doc_pwd = input('Enter doctor password: ')
            pat_name = input('Enter patient name: ')
            y = 0
            for user in users:
                if user.getName() == pat_name:
                    x = int(user.getPassword())
                    y = pow(g, x, p)
            if not ZeroKnowledgeProof(y):
                continue

            new_rec = Record()
            new_rec.addUsers(doc_name, pat_name)

            flag = False

            for doctor in doctors:
                if doctor.getName() == doc_name and doctor.getPassword() == doc_pwd:
                    for user in users:
                        if user.getName() == pat_name:
                            while True:
                                ip = input('Do you want to enter medical information (yes/no): ')
                                if ip == 'yes':
                                    newdata = input()
                                    new_rec.addInfo(newdata)
                                elif ip == 'no':
                                    records.append(new_rec)
                                    previousHash = verifyTransaction(
                                        records, previousHash, new_rec)
                                    flag = True
                                    break
                                else:
                                    print('Option is not recognized')
                        if flag:
                            break
                if flag:
                    break
            if not flag:
                print('Something is Wrong!!!')

        elif option == 'view':
            viewUser()

        choice = input('Do you want to continue? (yes/no): ')

    with open('state', 'wb') as file:
        dump = (previousHash, blockchain, records, users, doctors)
        pickle.dump(dump, file)



