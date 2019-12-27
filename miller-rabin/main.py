#!/usr/bin/python3

import random
import sys

from time import sleep

#n - 1 = 2^r * d

def miller_rabin(n, k=40):
    if n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False
    r = 1
    d = (n - 1) / (pow(2, r))
    while(d % 2 == 0):
        r += 1
        d = (n - 1) / (pow(2, r))
    d = int((n - 1) / (pow(2, r)))

    for i in range(k):
        a = random.randrange(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for i in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
            elif x == 1:
                return False
        else:
            return False
        continue
    return True


def gen_prime_candidate(bits):
    p = random.getrandbits(bits)
    p |= (1 << bits - 1) | 1
    return p

def gen_prime(bits):
    p = gen_prime_candidate(bits)
    while not miller_rabin(p):
        p = gen_prime_candidate(bits)
    return p

try:
    bits = sys.argv[1]
except:
    bits = 60

print(gen_prime(int(bits)))
