import random as rd
import math

'''
Need large prime - p
Elliptic curve - E
point - P
^solution to the elliptic curve equation modulo p
'''



'''
FINDING N + P
'''
class ecc(object):
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def display_field(self):
        print('x = ', self.x, 'y = ', self.y)


'''
Algo To find Elliptic Curve Roots
'''
#ellipitic curve result y^2 = x^3 + ax + b mod p
def generate(a,b,p):
    temp = []
    length_list = 0
    for x in range(p):
        for i in range(p):
            if (pow(i,2))%p == ((pow(x,3))+(a*x)+b)%p:
                length_list += 1
                temp.append((x,i))
    print("Field List: ", temp,"\nRoots: ", length_list)
    P, Q = (rd.sample(temp, 2))
    print("P1 :", P,"\nP2 :",Q)
    X1 = P[0]
    Y1 = P[1]

    X2 = Q[0]
    Y2 = Q[1]
    print("X1: ",X1)
    print("Y1: ",Y1)

    print("X2: ",X2)
    print("Y2: ",Y2)

    add_fields(X1, X2, Y1, Y2, P, Q, a, b, p)


    # if (i[-1]) == 0:
    #     fieldlist.append((x,i))
    # else:
    #     fieldlist.append(temp[::2])
    # print(fieldlist)
    # fieldlist.append(temp[::2])
   

'''
END
'''



def add_fields(X1, X2, Y1, Y2, P, Q, a, b, p):
    if X2 - X1 == 0:
        print("Division by 0 // CANNOT CONTINUE")
        exit()
    else:
        slope = (Y2 - Y1)/(X2 - X1)
        print("Slope = ", slope)


    #Rule 1 - if P1 ̸= P2 and x1 = x2, then P1 ⊕ P2 = O
    if P != Q and X1 == X2:
        print("R1 - Elliptic Curve Addition: O - Infinite")

    #Rule 2 - If P1 = P2 and y1 = 0, then P1 ⊕ P2 = 2P1 = O
    elif P == Q and Y1 == 0:
        print("R2 - Elliptic Curve Addition: O - Infinite")


    #Rule 3 - If P1 ̸= P2 (and x1 ̸= x2), let λ and ν = x
    elif P != Q:
        slope = ((Y2 - Y1) * pow(X2 - X1, -1, p)) % p

    else:
        slope = ((pow(X1, 3) + a) * pow(2 * Y1, -1, p)) % p

    X3 = (pow(slope, 2) - X1 - X2) % p
    Y3 = (slope * (X1 - X3) - Y1) % p

    print("New Point ", X3,",", Y3)

    scalarproduct(X1, X2, Y1, Y2, P, Q, a, b, p)


'''
END OF N + P
'''





'''
algo for nxP
'''
def scalarproduct(X1, X2, Y1, Y2, P, Q, a, b, p):
    m = "Test"
    L = 25
    num = rd.randint(1, 50)
    e = bin(num)[2:]      #turning into binary number
    print("Random e for this encryption -",e)
    
    # for i in range(0, L-1):
    #     R = m
    #     y = 0
    #     if a != 0:
    #         y = add_fields(y, R)
    #     R = add_fields(R, R)
    # print("Scalar Product -",y)




if __name__ == "__main__":
    #ellipitic curve result y^2 = x^3 + ax + b mod p
    # A // B // P
    generate(3, 8, 7)





    '''
    Alice and Bob agree on a large prime p, 
    an elliptic curve E, 
    and a point P which is a solution
    to the elliptic curve equation modulo p.
    '''
