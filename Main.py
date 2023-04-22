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
borrowers = []
lenders = []
p = 11
g = 2

# To ask the user if they want to import the previous data from the records
if exists('state'):
    while True:
        option = input('Previous data has been found... Would you like to import? (yes/no): ')
        if option == 'yes':
            with open('state', 'rb') as file:
                previousHash, blockchain, records, borrowers, lenders = pickle.load(file)
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

# for viewing the records of the borrowers(Lenders can view all of their borrowers' tramsaction records but the borrowers can only view their transaction data)
def viewUser() -> None:
    val = input('Are you a lender or borrower? (l/b): ')
    if val == 'l':
        lend = input('Enter your name: ')
        pwd = input('Enter your password: ')
        flag = False
        for lender in lenders:
            if lender.getName() == lend and lender.getPassword() == pwd:
                for block in blockchain:
                    if block.lender_name() == lend:
                        print(
                            'Time at which data was recorded: ' + str(block.getTimeStamp()))
                        print('Lender:' + lend)
                        print('Borrower:' + block.borrower_name())
                        print('Lender Transaction Information:')
                        #print('Total Amount Loaned until now' + str(block.total_amount_lender()))
                        print('Current Amount Loaned ')
                        block.printInfo()
                        for data in block.__curr_transaction_info__.__info__:
                            if(int(data)<0):
                                print(block.borrower_name() + ' returned ' + lend + ' Rs. ' + str((-1)*int(data)))
                        print()
                        flag = True
                print('Total Amount Loaned until now: ' + str(lender.__total__))
                if flag:
                    break
        if not flag:
            print('Lender Not Found')
    elif val == 'b':
        bor = input('Enter your name: ')
        y = 0
        bFlag = False
        for borrower in borrowers:
            if borrower.getName() == bor:
                bFlag = True
                x = int(borrower.getPassword())
                y = pow(g, x, p)
        if not bFlag:
            print('Borrower not found')
            return 
        if not ZeroKnowledgeProof(y):
            return
        flag = False
        for borrower in borrowers:
            if borrower.getName() == bor:
                for block in blockchain:
                    if block.borrower_name() == bor:
                        print('Time: ' + str(block.getTimeStamp()))
                        print('Lender:' + block.lender_name())
                        print('Borrower:' + bor)
                        print("Borrower's Transaction Data:")
                        #print('Total Amount Borrowed until now ' + str(block.total_amount_borrower()))
                        print('Current Amount Borrower ')
                        block.printInfo()
                        for data in block.__curr_transaction_info__.__info__:
                            if(int(data) < 0):
                                print(bor + ' returned ' + block.lender_name() +' Rs. ' + str((-1)*int(data)))
                        print()
                        flag = True
                print('Total Amount Borrowed until now: ' + str(borrower.__total__))
                if flag:
                    break
        if not flag:
            print('Borrower Not Found')
    else:
        print('Option is not recognized')


if __name__ == '__main__':

# Functionalities like add/register/view added for the user
    choice = 'yes'
    while choice == 'yes':
        option = input('Do you want to register or add or view? (r/a/v): ')

        if option == 'r':
            option1 = input('Do you want to register as lender or borrower? (l/b): ')
            if option1 == 'b':
                name = input('Enter name: ')
                pwd = input('Enter password (integer only): ')
                pwd_v = input('Verify password: ')
                if pwd == pwd_v:
                    new_borrower = User()
                    new_borrower.setName(name)
                    new_borrower.setPassword(pwd)
                    borrowers.append(new_borrower)
                else:
                    print('Password verification has failed')
            elif option1 == 'l':
                name = input('Enter name: ')
                pwd = input('Enter password (integer only): ')
                pwd_v = input('Verify password: ')
                if pwd == pwd_v:
                    new_lender = User()
                    new_lender.setName(name)
                    new_lender.setPassword(pwd)
                    lenders.append(new_lender)
                else:
                    print('Password verification has failed')
            else:
                print('Option is not recognised')

        elif option == 'a':
            lender_name = input('Enter the lender name: ')
            lender_pwd = input('Enter lender password: ')
            borrower_name = input('Enter borrower name: ')
            y = 0
            for borrower in borrowers:
                if borrower.getName() == borrower_name:
                    x = int(borrower.getPassword())
                    y = pow(g, x, p)
            if not ZeroKnowledgeProof(y):
                continue

            new_rec = Record()
            new_rec.addUsers(lender_name, borrower_name)

            flag = False
            lFlag = False
            for lender in lenders:
                if lender.getName() == lender_name and lender.getPassword() == lender_pwd:
                    lFlag = True
                    for borrower in borrowers:
                        if borrower.getName() == borrower_name:
                            while True:
                                ip = input('Do you want to enter transaction information (yes/no): ')
                                if ip == 'yes':
                                    newdata = input()
                                    borrower.setTotal(newdata)
                                    lender.setTotal(newdata)
                                    new_rec.addLender(lender)
                                    new_rec.addBorrower(borrower)
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
            if not lFlag: 
                print('You are not registered as lender')
            if lFlag and not flag:
                print('You are not registered as borrower')
            

        elif option == 'v':
            viewUser()

        choice = input('Do you want to continue? (yes/no): ')

    with open('state', 'wb') as file:
        dump = (previousHash, blockchain, records, borrowers, lenders)
        pickle.dump(dump, file)


