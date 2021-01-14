#Legendre_Basis.py
''' Contains a class with functions related to the Legendre Basis
'''

import math

f = math.factorial

def nCr(n, r):
    return factorial(n) / (facorial(r) * factorial(n-r))

def func(n):

    final = lambda x: 0
    for k in range(0, n+1):
        new = lambda x: 2^n * x^k * nCr(n, k) * nCr((n + k - 1 ) / 2, n)
        final = final + new

    return final

class LegendreBasis(n):
    '''legendre basis of degree n
    '''
    def __init__(self, n):
        '''initializes a legendre basis of degree n the basis will be of length n+1
        '''
        if type(n) != int:
            raise TypeError('Indexing variable is not an integer')
        else:
            self.basis = []
            for j in range(0, n+1):
                if j == 0 or j == 1:
                    self.basis.append(lambda x: 1)
                else:
                    self.basis.append(func(j))
