import random as rd
import math

class ecc(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display_field(self):
        print('x = ', self.x, 'y = ', self.y)

def generate(a, b, p, ordval,m):        #Algo #1, Finding Roots
    fieldlist = []       #create array for roots 
    length_list = 0 #initialize roots as 0
    for x in range(p):
        for i in range(p):
            if (pow(i, 2)) % p == ((pow(x, 3)) + (a * x) + b) % p:  #Pseudo Code math
                length_list += 1
                fieldlist.append((x, i))
    print("Field List: ", fieldlist, "\nRoots: ", length_list)
    return fieldlist, length_list

# fieldlist is the list of roots


def add_fields(P, Q, a, b, p):      #Algprithm to compute P + Q (Addition)
    X1, Y1 = P
    X2, Y2 = Q

    if P == (0, 0):
        return Q
    if Q == (0, 0):
        return P

    if X1 == X2:
        if (Y1 + Y2) % p == 0:
            return (0, 0)
        else:
            slope = ((3 * X1**2 + a) * pow(2 * Y1, -1, p)) % p
    else:
        if (X2 - X1) % p == 0:
            return (0, 0)
        slope = ((Y2 - Y1) * pow(X2 - X1, -1, p)) % p

    X3 = (pow(slope, 2) - X1 - X2) % p
    Y3 = (slope * (X1 - X3) - Y1) % p
    base = (X3, Y3)
    return base


def nXp(m, e, a, b, p):     #Algorithm to compute nXP
    R = (0, 0)
    binary = bin(e)[2:]

    for bit in binary:
        R = add_fields(R, R, a, b, p)
        if bit == '1':
            R = add_fields(R, m, a, b, p)

    return R

def ordmsg(m):
    ordmsg = []
    for i in m:
        ordmsg1 = ord(i)
        ordmsg.append(ordmsg1)
    return ordmsg

#ord val ^ is ord val to ec roots
#fieldlist is all the roots

def ECC(base, ordval,fieldlist):
    # nA = rd.choice(50)
    print("Message -",m)
    print("\n--------")
    EncodedM = []
    for i in ordval:
        print(i)
        EncodedM.append(fieldlist[i])
    return EncodedM


def calculate_c2(M, k, QA, a, b, p):
    kQA = nXp(QA, k, a, b, p)
    c2 = [add_fields(m, kQA, a, b, p) for m in M]
    return c2

def negate(point, p):
    # Negate the y-coordinate of the point in the finite field
    x, y = point
    negated_point = (x, (-y) % p)
    return negated_point


def mainstuff(P, a, b, p, EncodedM):

    '''
    (1) Alice and Bob agree on a large prime p, an elliptic curve E, and a point P which is a solution
    to the elliptic curve equation modulo p.
    '''

    '''
    (2) Alice chooses a private integer nA, computes QA = nA P, and sends QA to Bob.
    '''
    # nA = rd.choice(range(0,100))
    nA = 1194
    QA = nXp(P, nA, a,b,p)
    print("QA = ", QA)

    '''
    (3) Bob chooses a large private integer nB, computes QB = nB P and sends QB to Alice.
    '''
    # nA = rd.choice(range(0,100))
    nB = 1759
    QB = nXp(P, nB, a,b,p)
    print("QB = ", QB)


    '''
    (4) Assume Bob is the sender. Bob chooses a message m, which is a string. Bob encodes it using
    a cipher into M, which is a list of roots of the elliptic curve E
    '''
    print("Bobs Encoded message (list of roots) - ", EncodedM)




    '''
   (5) Bob chooses a random ephemeral key e which is to be used for only one message and thrown
    away.
    '''
    e = rd.choice(range(0,20))
    # e = 10
    print("e in main = ", e)


    '''
    (6) Bob computes the two quantities c1 = e P, which is a number, and the list of numbers
    c2 = M + k QA. Bob sends (c1, c2) to Alice.
    '''

    c1 = nXp(P, e, a,b,p)
    print("C1 = ", c1)


    c2 = calculate_c2(EncodedM, e, QA, a, b, p)
    print("C2 = ", c2)

    '''
    (7) Alice decrypts the message by computing (c2 − nA c1)
    '''
    nAc1 = nXp(c1, nA, a,b,p)
    print("nAc1 = ", nAc1)



    decrypted = []
    for point in c2:
        decrypted_point = add_fields(point, negate(nAc1, p), a, b, p)
        decrypted.append(decrypted_point)
    print("Decrypted Values = ", decrypted)

    # Find the indices of the decrypted points in the fieldlist
    indices = [fieldlist.index(point) for point in decrypted]

    # Print the ASCII values corresponding to the indices
    ascii_values = [point[0] for point in fieldlist]
    decrypted_ascii = [ascii_values[index] for index in indices]

    print("Indices of points in fieldlist:", indices)

    decrypyedmsg = []
    for i in indices:
        decrypyedmsg.append(chr(i))
    print(decrypyedmsg)

    string = ''.join(str(j) for j in decrypyedmsg)
    print("DECRYPTED MESSAGE = ", string)
if __name__ == "__main__":

    m = "i am testing my code, WORKING!!!!"
    ordval = ordmsg(m)
    a = 324
    b = 1287
    p = 3851

    # a = 3
    # b = 8
    # p = 7

    fieldlist, length_list= generate(a,b,p, ordval,m)
    # P, Q = (5274, 2841), (8669, 740)
    P, Q = (920, 303), (5,1)
    #P, Q = (rd.sample(fieldlist, 2))

    Pmult = 5
    Qmult = 2

    base = add_fields(P, Q, a,b,p)
    print("BASE = ",base)
    # result_5P = nXp(P, Pmult, a,b,p)
    # print("5P Result - ", result_5P)
    result_2Q = nXp(P, Qmult, a,b,p)
    print("2P Result - ", result_2Q)

    EncodedM = ECC(base, ordval, fieldlist)

    c2 = mainstuff(P, a, b, p, EncodedM)

    # origmessage = decrypt(c2, fieldlist, EncodedM, m, P, a, b, p, ordval)
    # print(Pmult,"P",result_5P)
    # print(Qmult,"Q",result_2Q)
    # print("Elliptic Curve Addition - ", base)
