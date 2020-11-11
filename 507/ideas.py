#ideas.py
'''
This file is used for exploring ideas
'''


import numpy as np
def f_add(f1, f2):
    '''Adds two lambda functions together
       Paramaters:
       (lambda) f1, f2
       Returns:
       (lambda) f1 + f2
    '''
    return lambda *args, **kwds: f1(*args, **kwds) + f2(*args, **kwds)

def c_mult(c, f):
    '''Multiplies a lambda by a constant
       Paramaters:
       (lambda) f1
       (int) c
       Returns:
       (lambda) c * f
    '''
    return lambda *args, **kwds: f(*args, **kwds) * c

def composition(f, g):
    ''' Composes two lambda functions f and g
        Paramaters:
        (lambda) f, g
        Returns:
        (lambda) f(g(x))
    '''
    return lambda *args, **kwds: f(g(*args, **kwds))

def matrix_mult(A, f):
    '''performs a change of basis on the functions f
       Paramaters:
       (np.array(p+1, p+1)) A: matrix containing the new coordinates
       (np.array(p+1,)) f: a vector containing the current lambda functions
       Returns:
       (np.array(p+1,)) a vector containing the new functions
    '''

    n,m = A.shape
    new_functions = []

    if n != m:
        raise ValueError('The Transition matrix is not square')

    for i in range(0, n):
        current = lambda x: 0
        for j in range(0, n):
            current = f_add(current, c_mult(A[i, j], f[j]))

        new_functions.append(current)

    return np.array(new_functions)
