__author__ = 'Waimond_MAC'

import _hashlib
import time
import itertools
def hash():
    hash = '9D08FD0EE2B2CD5A5CCCB97DE9613E7D9ED894D6'
    salt = 'nO'
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-='
    Time = time.time()
    res = itertools.product(alpha, repeat=6)
    print ("starting brute")
    for i in res:
        h = _hashlib.openssl_sha1()
        word = ''.join(i)
        h.update(salt + word)
        if h.hexdigest() == hash:
            print ('word: ',word)
            print('time it took:', time.time()-Time)
            return
    print ("no word")
    return

if __name__ == '__main__':
    hash()
