__author__ = 'Waimond_MAC'
import _hashlib
import time

def hash():
    hash = 'CC9E6E4C4CDCAE06C669BDA492981B00929D9AF8'
    salt = 'hz'
    f = open('hashes.txt', 'w')
    Time = time.time()
    for i in range(0, 9999):
        h = _hashlib.openssl_sha1()
        number = str(i).zfill(4)
        h.update(salt+number)
        result = h.hexdigest()
        f.write(result.upper())
        f.write('\n')
        if hash == result.upper():
            print('pin: ', i)
            f.close()
            print('time it took:', time.time()-Time)
            return
    f.close()
    print ('cant find pin')
    return

if __name__ == '__main__':
    hash()