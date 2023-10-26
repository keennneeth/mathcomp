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


#ellipitic curve result y^2 = x^3 + ax + b mod p
def generate(a,b,p):
    i = p-1
    fieldlist = []
    fieldlist.append((0,0))
    print(fieldlist)
    length_list = 1
    # y = pow(i,2)%p
    # math2 = pow(x,3)+(a*x)+b%p
    for x in range(p-1):
        for i in range(p-1):
            if (pow(i,2)%p == pow(x,3)+(a*x)+b%p):
                length_list += 1
                fieldlist.append((x,i))
    print(fieldlist, length_list)

# def add_fields():
#     P1 = (x1,y1)
#     P2 = (x2,y2)
#     if P1 != P2 and x1 == x2:
#         inf = P1^P2

#     elif P1 == P2 and y1 == 0:
#         inf = 2*P1 = P1^P2

#     elif P1 != P2 and x1 != x2:
#         lamb = (y2-y1)/(x2-x1)
#         nu = (y1*x2) - (y2*x1) / (x2-x1)

'''
END OF N + P
'''





'''
algo for nxP
'''
# def scalarproduct(e):
#     e = bin(e)[2:]      #turning into binary number
#     print(e)
    # for i in range(L-1):
    #     R = m
    #     y = inf
    #     if ai != 0:
    #         y = add_fields(y,R)
    #     R = add_fields(R,R)
    # return y

if __name__ == "__main__":
    # x=int(input("X = : "))
    # y=int(input("Y = : "))
    # EllipticCurveRoots(x,y,40,60,80)
    p = int(rd.choice(open("primes.txt").readlines()))
    # x1 = rd.randint(0, 9)
    # x2 = rd.randint(0, 9)
    # y1 = rd.randint(0, 9)
    # y2 = rd.randint(0, 9)
    myObj = ecc(0,9)
    generate(myObj.x, myObj.y,p)





    '''
    Alice and Bob agree on a large prime p, 
    an elliptic curve E, 
    and a point P which is a solution
    to the elliptic curve equation modulo p.
    '''
