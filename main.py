import math
import random as rd
import sys



'''
find gcd
m * n = 1
both numbers have to be co-prime

let a be a positive number and p is inverse mod p, we need
positive number s satisfying
as = 1 mod p -> a  = np+1
as + tp = 1
as + tp = r
'''


def inverse_mod_p(prime1, prime2):
    r,s = gcd(prime1, prime2)      #a and p have to be positive numbers
    if r != 1:          # a mod p == r
        flag = False
        e = rd.randrange(3, s)
    else:
        flag = True
    return s, flag



#function used to find gcd by solving as+tp=r

def gcd(prime1, prime2):
    oldr, r = (prime1, prime2)
    olds, s = (1,0)
    oldt, t = (0,1)

    while r != 0:
        q = math.floor(oldr//r)
        oldr, r = r, oldr - q * r
        olds, s = s, olds - q * s
        oldt, t = t, oldt - q * t
   
    if olds < 0:
        olds = olds + prime2
    return oldr, olds

def LCM(prime1, prime2):
    np1 = prime1 - 1
    np2 = prime2 - 1



    return (math.lcm(np1, np2))



if __name__ == '__main__':

        
    primeslist = "primes.txt"

    with open(primeslist) as primes:
        primenumbers = primes.read()

    print("Step 1  - Alice picking two primes 1-500")
    prime1 = input("Pick your first prime number - ") + "\n"
    if prime1 in primenumbers:
        prime1 = int(prime1)
    else:
        print("Not a prime number, try again")
        sys.exit()

    prime2 = input("Pick your second prime number - ") + "\n"
    if prime2 in primenumbers:
        prime2 = int(prime2)
    else:
        print("Not a prime number, try again")
        sys.exit()

print("\n\nStep 2 - LCM of",prime1,"and", prime2)  
print("λ = (prime1 − 1) (prime2 − 1)")
print("λ = ", LCM(prime1, prime2))  


print("\n\nStep 3 - Inverse multiplicative, (T/F)")  
print(inverse_mod_p(prime1, prime2))




'''
/* The pseudo-code begins below */
/* Python: we assume the two functions mentioned in Data above are in the
file Extended Euclidean Algorithm.py */
/* Python: begin by importing random as rd, and Extended Euclidean Algorithmas ee */
primeslist = load primes.txt /* Python: Use the commands described earlier in
this document. */

length primes = length(primeslist)
Choose random integers p, q from the list {2, · · · , length primes}
/* Alice selects two random primes next. */

prime1 = primeslist(p) and prime2 = primeslist(q)

/* Next task is to find the least common multiple of (prime1 − 1) (prime2 − 1)*/
(g, s) =gcd(prime1 − 1, prime2 − 1)
λ = (prime1 − 1) (prime2 − 1)/g /* LCM(a, b) = a b
GCD(a,b)
*/
found =False
while found is False do
Choose a random integer e between 3 and λ
(k, found) =inverse modulo n(e, λ)
N = prime1 × prime2
/* (N, e) is the public key Alice communicates to Bob. k is her private key.
*/
/* Bob selects a message m (through user input) which is a string of
characters. Bob encodes each character using the formula */
s(i) = int(m(i))e mod N /* MatLab: Use the mod command. Python: Use the %
command. */
/* MatLab: use (double(m(i)))e. For example, double(0H0) gives the number 72.
Python: Use ‘‘ord" to convert characters to integers. */
/* Bob concatenates the encoded characters into a message that is sent to
Alice. */
/* Alice receives the message and decodes each character using the formula */
d(i) =char(s(i)
k mod N)
/* MatLab: use ‘‘char" to convert integers to characters. Python: Use
‘‘chr" to convert integers to characters, and ’ ’.join() to concatenate
characters to a string */
/* Alice concatenates the decoded characters to retrieve the original
message.
    '''

