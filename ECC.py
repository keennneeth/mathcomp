import random as rd
import math

class ecc(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display_field(self):
        print('x = ', self.x, 'y = ', self.y)

def generate(a, b, p, ordval,m):
    temp = []
    length_list = 0
    for x in range(p):
        for i in range(p):
            if (pow(i, 2)) % p == ((pow(x, 3)) + (a * x) + b) % p:
                length_list += 1
                temp.append((x, i))
    print("Field List: ", temp, "\nRoots: ", length_list)
    P, Q = (3,4), (5,1)
    # P, Q = (rd.sample(temp, 2))
    print("P1 :", P, "\nP2 :", Q)
    

    return P, Q, temp

def add_fields(P, Q, a, b, p):
    X1, Y1 = P
    X2, Y2 = Q

    if P == (0,0):
        return Q
    if Q == (0,0):
        return P

    if X1 == X2:
        if (Y1 + Y2) % p == 0:
            return (0,0)
        else:
            slope = ((3 * X1**2 + a) * pow(2 * Y1, -1, p)) % p
    else:
        slope = ((Y2 - Y1) * pow(X2 - X1, -1, p)) % p


    X3 = (pow(slope, 2) - X1 - X2) % p
    Y3 = (slope * (X1 - X3) - Y1) % p
    base = (X3, Y3)
    return base




def double_point(P, a, p):
    if P == (0,0):
        return P
    else:
        return add_fields(P, P, a, 0, p)




def nXp(m, e, a, b, p):
    R = m
    y = (0,0)
    binary = bin(e)[2:]
    for bit in binary:
        y = double_point(y, a, p)
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





def ECC(base, ordval,temp):
    # nA = rd.choice(50)
    print("Message -",m)
    print("\n--------")
    EncodedM = []
    for i in ordval:
        EncodedM.append(temp[i])
    return EncodedM


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

    nA = rd.choice(range(0,100))
    nB = rd.choice(range(0,100))
   
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

    c2 = []
    for i in EncodedM:
        c2.append(add_fields(i, c1, a,b,p))
    print("c2 - ", c2)

    print("Alice recieves the 2 quantites", c1, "and", c2)

    nAc1 = nXp(c1, nA, a,b,p)
    print("Alice computes nAc1 -", nAc1)


    c2_m_nAc1 = []
    for i in c2:
        c2_m_nAc1.append(i[0] - nAc1[0])
    print("Alice decrypts the message using c2 - nAc1", c2_m_nAc1)










if __name__ == "__main__":
    e = rd.choice(range(0,20))
    m = "testing"
    ordval = ordmsg(m)
    a = 3
    b = 8
    p = 7
    P, Q, temp= generate(a,b,100, ordval,m)
    
    Pmult = 5
    Qmult = 2

    base = add_fields(P, Q, a,b,p)
    result_5P = nXp(P, Pmult, a,b,p)
    result_2Q = nXp(Q, Qmult, a,b,p)

    EncodedM = ECC(base, ordval, temp)

    main = mainstuff(P, e, a, b, p, ordval, EncodedM)


    # print(Pmult,"P",result_5P)
    # print(Qmult,"Q",result_2Q)
    # print("Elliptic Curve Addition - ", base)
