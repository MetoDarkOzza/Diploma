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
    afile.close()
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
    # print('hello')
    # print(checker)
    # print('hello')
    # print(signlist)
    if (checker == signlist):
        return 1
    else:
        return 0


def createSignature(filename,secretkey):

    signaturefile = open('./signatures/signature'+str(filename)+'.txt', 'w')
    filehash = getFileBinaryHash(filename)
    signature = sign(secretkey, filehash)
    for i in range(len(signature)):
        signaturefile.write(str(signature[i]) + '\n')

    signaturefile.close()

def writekeytofile(filename, openkeys):
    keyfile = open('./openkeys/' + str(filename)+'openkey.txt', 'w')

    for i in range(len(openkeys)):
        for j in range(len(openkeys[0])):
            keyfile.write(openkeys[i][j] + '\n')

    keyfile.close()

def readopenkey(filename):
    f = open('./openkeys/'+str(filename)+'openkey.txt','r')
    openkey = []
    buf = []
    buf = f.readlines()
    #print(buf)
    for i in range(len(buf)):
        buf[i] = buf[i].strip()
    #print(buf)
    for i in range(2,(len(buf)+2),2):
        buf1 = []
        buf1.append(buf[i-2])
        buf1.append(buf[i-1])
        openkey.append(buf1)


    f.close()
    return openkey


def readsignature(filename):
    f = open('./signatures/signature'+ str(filename)+'.txt')
    signature = []
    for line in f:
        signature.append(line)
    for i in range(len(signature)):
        signature[i] = int(signature[i])
    f.close()
    return signature

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