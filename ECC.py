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

    X3 = (pow(slope, 2) - X1 - X2) 
    Y3 = (slope * (X1 - X3) - Y1) 
    base = (X3, Y3)
    return base


def nXp(m, e, a, b, p):     #Algorithm to compute nXP
    R = m
    y = (0,0)
    binary = bin(e)[2:]
    for bit in binary:
        if bit != '0':
            y = add_fields(y, m, a, b, p)
        R = add_fields(R, m, a, b, p)
    return y

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


# def decrypt(c2, fieldlist, EncodedM, m, P, a, b, p, ordval):
#     original_message = m
#     e = rd.choice(range(150, 200))
#     while c2 != EncodedM:
#         e = rd.choice(range(150, 200))
#         c2 = mainstuff(P, e, a, b, p, ordval, EncodedM)
#Just in case the decryption is encorrect, it will reset and try again.


    print("decrypt c2 - ", c2)

    c = [fieldlist.index(x) for x in c2 if x in c2 and x in fieldlist]
    print(c)
    decryptedmessage = ''.join(chr(num) for num in c)

    print(decryptedmessage)

'''
(1) Alice and Bob agree on a large prime p, an elliptic curve E, and a point P which is a solution
to the elliptic curve equation modulo p.
(2) Alice chooses a private integer nA, computes QA = nA P, and sends QA to Bob.
(3) Bob chooses a large private integer nB, computes QB = nB P and sends QB to Alice.
(4) Assume Bob is the sender. Bob chooses a message m, which is a string. Bob encodes it using
a cipher into M, which is a list of roots of the elliptic curve E.
(5) Bob chooses a random ephemeral key e which is to be used for only one message and thrown
away.
(6) Bob computes the two quantities c1 = e P, which is a number, and the list of numbers
c2 = M + k QA. Bob sends (c1, c2) to Alice.
(7) Alice decrypts the message by computing (c2 − nA c1.)
'''
def mainstuff(P, e, a, b, p, ordval, EncodedM):

    # nA = rd.choice(range(0,100))
    # nB = rd.choice(range(0,100))
    nA = 5
    nB = 7


    '''
    P  = 3,4
    '''
   
    QA = nXp(P, nA, a,b,p)
    QB = nXp(P, nB, a,b,p)
    
    c1 = nXp(P, e, a, b, p)
    #2
    print("Alice's Private Integer -", nA)
    #3
    print("Bob's Private Integer -", nB)
    print("Alice's QA -", QA)
    print("Bob's QB -", QB)

    #4
    print("Bobs Encoded message (list of roots) - ", EncodedM)
    #5
    print("Bob's random ephemeral key e -", e)
    print("Bob computes c1 (eP) -", c1)

    # print("Alice recieves the 2 quantites", c1, "and", c2)

    nAc1 = nXp(c1, nA, a,b,p)
    print("Alice computes nAc1 -", nAc1)
    c2 = [add_fields(m, nXp(QA, e, a, b, p), a, b, p) for m in EncodedM]

    return c2


    # c2_m_nAc1 = []
    # for i in c2:
    #     c2_m_nAc1.append((i[0] - nAc1[0], i[1] - nAc1[1]))
    # print("Alice decrypts the message using c2 - nAc1", c2_m_nAc1)



    # # Step 7: Alice decrypts the message by computing c2 - nA * c1
    # nAc1 = nXp(c1, nA, a, b, p)
    # decrypted_message = [add_fields(m, nAc1, a, b, p) for m in c2]
    # print("Testing - ", decrypted_message)

if __name__ == "__main__":
    # e = rd.choice(range(0,20))
   
    e = 32
    m = "Hello World"
    ordval = ordmsg(m)
    a = 3
    b = 8
    p = 7

    fieldlist, length_list= generate(a,b,200, ordval,m)
    P, Q = (3,4), (5,1)
    #P, Q = (rd.sample(fieldlist, 2))

    Pmult = 5
    Qmult = 2

    base = add_fields(P, Q, a,b,p)
    result_5P = nXp(P, Pmult, a,b,p)
    result_2Q = nXp(Q, Qmult, a,b,p)

    EncodedM = ECC(base, ordval, fieldlist)

    c2 = mainstuff(P, e, a, b, p, ordval, EncodedM)

    # origmessage = decrypt(c2, fieldlist, EncodedM, m, P, a, b, p, ordval)
    # print(Pmult,"P",result_5P)
    # print(Qmult,"Q",result_2Q)
    # print("Elliptic Curve Addition - ", base)
