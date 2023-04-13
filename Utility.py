# Cryptography Assignment - 2

import hashlib
import random

# Using SHA256 as the hashing function
def useSha256(input: str) -> str:
    result = hashlib.sha256(input.encode())
    return result.hexdigest()

def getDiffStr(difficulty: int) -> str:
    return '0' * difficulty

# Zero Knowledge Proof implementation
def ZeroKnowledgeProof(y1: int) -> bool:
    
    print('\nUser Verification(Please confirm yourself as a user)')
    print('Using Zero Knowledge Proof(ZKP)')
    print('Pick a random number 'r' from 0 to 9')
    h = int(input('Calculate h = (2^r) mod 11 and Enter h: '))
    print('The value of h is ' + str(h))
    b = random.randint(0, 1)
    print('Random bit(b) generated is: ' + str(b))
    s = int(input('''
    Compute s = (r + b*x) mod 10.
    Here x is the password(i.e. the value that you need to prove that you know while using ZKP): 
    '''))
    value1 = pow(2, s, 11)
    value2 = (h * pow(y1, b, 11)) % 11
    if value1 == value2:
        print('Zero Knowledge Proof is Successful.You are now verified as registered user\n')
        return True
    else:
        print('Zero Knowledge Proof has Failed.Please try again\n')
