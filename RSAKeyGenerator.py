import random
import numpy as np

def generate_prime_list(listOfPrimes):
    '''
    Generates a list of prime numbers from a text document.
    :param listOfPrimes: a text documents containing a list of prime numbers
    :return primeList: a list of prime numbers
    '''
    primeList = []
    with open(listOfPrimes) as file:
        for line in file:
            prime = int(line.strip())
            primeList.append(prime)
    return primeList

def find_p_q_n(primeList):
    '''
    Finds two random numbers, p and q, from the list of prime numbers. Computes n by multiplying
    p and q together.
    :param primeList: a list of prime numbers
    :return p: a random prime number
    :return q: a random prime number
    :return n: p times q
    '''
    p = primeList[random.randint(1, len(primeList) - 1)]
    q = primeList[random.randint(1, len(primeList) - 1)]
    n = p*q
    return p, q, n


def main():
    primeFile = "primeNumbers.txt"
    primeList = generate_prime_list(primeFile)
    p, q, n = find_p_q_n(primeList)

    if n < 65537: #establishes value of e
        e = 17
    else:
        e = 65537

    lam = np.lcm(p-1, q-1) #calculates lamdba

    print("Found a valid key pair:")
    print("Public Key: (" + hex(n)[2:] + ", " + hex(e)[2:] + ")")

    for d in range(lam): #calculates d
        if (d*e) % lam == 1:
            print("Private Key: (" + hex(n)[2:] + ", " + hex(d)[2:] + ")")
            break

main()