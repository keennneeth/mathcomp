import random as rd
import math

class ecc(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display_field(self):
        print('x = ', self.x, 'y = ', self.y)

def generate(a, b, p, ordval):
    temp = []
    length_list = 0
    for x in range(p):
        for i in range(p):
            if (pow(i, 2)) % p == ((pow(x, 3)) + (a * x) + b) % p:
                length_list += 1
                temp.append((x, i))
    print("Field List: ", temp, "\nRoots: ", length_list)
    P, Q = (5274,2841), (8669,740)
    print("P1 :", P, "\nP2 :", Q)
    for i in ordval:
        print([i], temp[i])

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
        # Slope calculation for different points
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
    y = (0,0)
    binary = bin(e)[2:]
    for bit in binary:
        y = double_point(y, a, p)
        if bit != '0':
            y = add_fields(y, m, a, b, p)

    return y

def ordmsg(m):
    ordmsg = []
    for i in m:
        ordmsg1 = ord(i)
        ordmsg.append(ordmsg1)
    return ordmsg

if __name__ == "__main__":
    num = 10
    e = bin(num)[2:]
    m = "testing"
    ordval = ordmsg(m)
    P, Q, temp = generate(3, 8, 100, ordval)

    Pmult = 25
    Qmult = 34

    base = add_fields(P, Q, 497, 1768, 9739)
    result_5P = nXp(P, Pmult, 497, 1768, 9739)
    result_2Q = nXp(Q, Qmult, 497, 1768, 9739)

    print(Pmult,"P",result_5P)
    print(Qmult,"Q",result_2Q)
    print("Elliptic Curve Addition - ", base)
