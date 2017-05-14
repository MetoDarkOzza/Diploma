import secrets
import numpy as np
import cv2
import hashlib




#f = open('hash.txt', 'w')
#f.write(hasher.hexdigest())
#print(randnum)


def genKeys(keylength):
    keys = []
    secretkeys = []
    openkeys = []
    for i in range(keylength):
        buflist = []
        for j in range(2):
            buf = secrets.randbits(keylength)
            buflist.append(buf)
            #print(buf)

        secretkeys.append(buflist)
    print(secretkeys[0][0])
    print(len(secretkeys))

    for i in range(len(secretkeys)):
        bufkey = []
        for j in range(len(secretkeys[i])):
            hasher = hashlib.sha1()
            hasher.update(str(secretkeys[i][j]).encode('utf8'))
            bufkey.append(bin(int(hasher.hexdigest(), 16)))
            #print(bin(int(hasher.hexdigest(), 16)))
        openkeys.append(bufkey)

    keys.append(secretkeys)
    keys.append(openkeys)
    print(keys[1])
    print(len(keys[1]), len(keys[0]))
    return keys


def getFileBinaryHash(filename):
    BLOCKSIZE = 65536
    hasher = hashlib.sha1()
    with open(filename, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
   # print(hasher.hexdigest())
    b = bin(int(hasher.hexdigest(), 16))
    #print(b)
    #print(len(b))
    # b = int(hasher.hexdigest(), 16)
    # print(b)
    b = str(b)
    newstr = ""
    if (len(b) < 162):
        for i in range(162 - len(b)):
            newstr += "0"
        #print(newstr)
    j = 2
    while (j < len(b)):
        newstr += b[j]
        j += 1

    #print(newstr)
    return newstr


def sign(secretkeys, filehash):
    signature = []
    for i in range(len(filehash)):
        if(filehash[i] == '0'):
            signature.append(secretkeys[i][0])
        elif(filehash[i] == '1'):
            signature.append(secretkeys[i][1])

    return signature


def verify(signature, openkeys, filename):
    messhash = getFileBinaryHash(filename)
    checker = []
    signlist = []
    for i in range(len(messhash)):
        if (messhash[i] == '0' ):
            checker.append(openkeys[i][0])
        elif(messhash[i] == '1'):
            checker.append(openkeys[i][1])

    for i in range(len(signature)):
        hasher = hashlib.sha1()
        hasher.update(str(signature[i]).encode('utf8'))
        signlist.append(bin(int(hasher.hexdigest(), 16)))
        #print(bin(int(hasher.hexdigest(), 16)))
    print(checker)
    print(signlist)
    if (checker == signlist):
        return 1
    else:
        return 0


def createSignature(filename,secretkey):

    signaturefile = open('signature.txt', 'w')
    filehash = getFileBinaryHash(filename)
    signature = sign(secretkey, filehash)
    for i in range(len(signature)):
        signaturefile.write(str(signature[i]) + '\n')
    signaturefile.close()


def main():

    filehash = getFileBinaryHash('output0.avi')
    keys = genKeys(160)
    signa = createSignature('output0.avi',keys[0])
    # signature = sign(keys[0], filehash)
    # print(signature)
    # if(verify(signature, keys[1], 'output0.avi') == 1):
    #     print('All is good')
    # else:
    #     print('All is bad')


if __name__ == '__main__':
    main()