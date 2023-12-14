
import math
import random as rd
#a and p have to be positive numbers
def inverse_mod_p(prime1, prime2):
 r,s = gcd(prime1, prime2) 
 if r != 1: 
 flag = False 
 else:
 flag = True
 return s, flag
#function used to find greatest common divisor by solving as+tp=r
def gcd(prime1, prime2):
 oldr, r = (prime1 , prime2 )
 olds, s = (1,0)
 oldt, t = (0,1)
 while r != 0:
 q = math.floor(oldr//r)
 oldr, r = r, oldr - q * r
 olds, s = s, olds - q * s
 oldt, t = t, oldt - q * t
 
 if olds < 0:
 olds = olds + prime2
 return olds, oldr
#Function to find LCM
def LCM(prime1, prime2):
 np1 = prime1 - 1
 np2 = prime2 - 1
 return (math.lcm(np1, np2))
if __name__ == '__main__':
#Generate two random primes from primes.txt file
 primeslist = "primes.txt"
 with open(primeslist) as primes:
 primenumbers = primes.read()
#Picking 2 random numbers from primes.txt file
 prime1 = int(rd.choice(open("primes.txt").readlines()))
 prime2 = int(rd.choice(open("primes.txt").readlines()))
 '''
 CALCULATIONS
 '''
 mult = (prime1-1) * (prime2 -1) #equation for lamb
 lamb = int(mult / gcd(prime1-1,prime2-1)[1]) #used to find public key
 
 e = rd.randint(3, lamb)
 while math.gcd(e, lamb) != 1: #generating public key, while it does not equal 1. Generate anoter key
 e = rd.randint(3, lamb)
 
 k = gcd(e, lamb)[0] #finding mod inverse, aka private key
 N = prime1*prime2 #finding N
 '''
 CALCULATIONS
 '''
 message = input("Message to Encrypt = ")
 print("_____________________")
 print("Private Key Values")
 print("Prime 1 = ", prime1)
 print("Prime 2 = " ,prime2)
 print("Mod Inverse (k) = ", k)
 print("_____________________")
 print("Public Key Values")
 print("N = ", N)
 print("Public Key (e) = ", e)
 print("_____________________")
 #Encryption
 original = []
 messageord = []
 #Bob encodes each character using the formula s(i) = int(m(i))e mod N
 for char in message:
 messageord1= ord(char)
 original.append(messageord1)
 y = pow(messageord1, e) % N
 messageord.append(y)
 print("Original Message: ", original)
 print("Encoded Message: ", messageord)
 #Decryption
 #Alice receives the message and decodes each character using the formula 
 #d(i) = char(s(i)k mod N)
 print("\nMessage Decrypted")
 for i in messageord:
 n = pow(i,k) % N 
