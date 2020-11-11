#bernstein_basis.py

from math import factorial
import numpy as np
from matplotlib import pyplot as plt

def nCr(n,r, le = 0, re = 1):
    if le == 0 and re == 1:
        return factorial(n) / (factorial(r) * factorial(n-r))
    else:
        return (factorial(n) / (factorial(r) * factorial(n-r))) * (1/(re-le)) **(n-j) * ((1/re-le)) ** j

def func(n, j, le = 0, re = 1):
    if le == 0 and re == 1:
        return lambda x: nCr(n, j) * (x**j) * ((1 - x) ** (n-j))
    else:
        return lambda x: nCr(n, j) * ((re-x)/(re-le)) ** (n-j) * ((x-le)/(re-le))**(j)

def extraction_operator(p, k, i, en):
    ''' Gets the extraction operator for a given element
        Paramaters:
        (int) p polynomial degree
        (int) k continuity
        (int) i element number
        (int) en total element number
        Returns:
        (np.array((p+1), (p+1))) of th extraction operator
    '''
    if p == 2 and k == 1:
        if en == 1:
            return np.eye(3)
        elif i == 0:
            return np.array([[1, 0, 0],
                             [0, 1, 0.5],
                             [0, 0, 0.5]])
        elif i == en - 1:
            return np.array([[0.5, 0, 0],
                             [0.5, 1, 0],
                             [0, 0, 1]])
        elif 0 < i and i < en - 1:
            return np.array([[0.5, 0, 0],
                             [0.5, 1, 0.5],
                             [0, 0, 0.5]])
        else:
            raise ValueError('i is not in range')

    elif p == 3 and k == 2:
        if en == 1:
            return np.eye(4)
        elif en == 2:
            if i == 0:
                return np.array([[1, 0, 0, 0],
                                 [0, 1, 1/2., 1/4.],
                                 [0, 0, 1/2., 1/2.],
                                 [0, 0, 0, 1/4.]])
            elif i == 1:
                return np.array([[1/4., 0, 0, 0],
                                 [1/2., 1/2., 0, 0],
                                 [1/4., 1/2., 1, 0],
                                 [0, 0, 0, 1]])
            else:
                raise ValueError('i is not in range')
        elif en == 3:
            if i == 0:
                return np.array([[1, 0, 0, 0],
                                 [0, 1, 1/2., 0.25],
                                 [0, 0, 1/2., 7/12.],
                                 [0, 0, 0, 1/6.]])
            elif i == 1:
                return np.array([[1/4., 0, 0, 0],
                                 [7/12., 2/3., 1/3.,1/6.],
                                 [1/6., 1/3., 2/3., 7/12.],
                                 [0, 0, 0, 1/4.]])
            elif i == 2:
                return np.array([[1/6., 0, 0, 0],
                                 [7/12., 1/2., 0, 0],
                                 [1/4., 1/2., 1, 0],
                                 [0, 0, 0, 1]])
            else:
                raise ValueError('i is not in range')
        else:
            if i == 0:
                return np.array([[1, 0, 0, 0],
                                 [0, 1, 1/2., 1/4.],
                                 [0, 0, 1/2., 7/12.],
                                 [0, 0, 0, 1/6.]])
            elif i == 1:
                return np.array([[1/4., 0, 0, 0],
                                 [7/12., 2/3., 1/3., 1/6.],
                                 [1/6., 1/3., 2/3., 2/3.],
                                 [0, 0, 0, 1/6.]])
            elif 1 < i and i < en - 2:
                return np.array([[1/6., 0, 0, 0],
                                 [2/3., 2/3., 1/3., 1/6.],
                                 [1/6., 1/3., 2/3., 2/3.],
                                 [0, 0, 0, 1/6.]])
            elif i == en - 2:
                return np.array([[1/6., 0, 0, 0],
                                 [2/3., 2/3., 1/3., 1/6.],
                                 [1/6., 1/3., 2/3., 7/12.],
                                 [0, 0, 0, 1/4.]])
            elif i == en - 1:
                return np.array([[1/6., 0, 0, 0],
                                 [7/12., 1/2., 0, 0],
                                 [1/4., 1/2., 1., 0.],
                                 [0, 0, 0, 1.]])
            else:
                raise ValueError('i is not in range')

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

def func_comp(f, g):
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
    m, n = A.shape
    new_functions = []
    q = f.shape[0]

    if q != n:
        raise ValueError('The function vector f is not of the correct size')
    if n != m:
        raise ValueError('The extraction matrix is not square')
    for i in range(0, n):
        current = lambda x: 0
        for j in range(0, n):
            current = f_add(current, c_mult(A[i, j], f[j]))
        new_functions.append(current)
    return np.array(new_functions)

class BernsteinBasis(object):
    '''This file contains a class that will make a basis of bernstein polynomials of degree n
      Attribute(s):
       basis(np.array): containing the coefficients of the bernstein basis ordered in ascending degree for x^j
                 of power
    '''

    def __init__(self, n, le = 0, re = 1):
        '''uses the definition for bernstein basis as B_j^n(x) = (n choose j)x^j(1-x)^(n-j) (j, 0-> n)
        '''
        if type(n) != int:
            raise TypeError('The Bernstein polynomials are not of an integer degree')
        elif type(le) != float and type(le) != int:
            raise TypeError('The left end point is not of numerical value')
        elif type(re) != float and type(re) != int:
            raise TypeError('The right end point is not of numerical value')
        elif(re < le):
            raise ValueError('The right endpoint is less than the left endpoint')
        else:
            self.coefficients = np.array([nCr(n, j) for j in range(0,n+1)])
            self.bernstein_functions = np.array([func(n, j, le, re) for j in range(0,n+1)])

class SplineBasis(BernsteinBasis):
    ''' This class inherits from the Bernstein basis class and uses the bernstein basis to create a spline basis
    '''

    def __init__(self, p, k, le, re, i, en):
        ''' Constructs the spline basis object from a BernsteinBasis object using Bezier Extraction
                Paramaters:
                (int) p degree number (could also find with len(self.basis_functions) - 1)
                (int) k continuity
                (float) le left endpoint of element domain
                (float) re right endpoint of element domain
                (int) i current element number
                (int) en total element number
        '''
        BernsteinBasis.__init__(self, p)
        if p == 1 and k == 0:
            functions = self.bernstein_functions
            self.operator = np.eye(2)
        elif p == 2 and k == 1:
            if en == 1:
                self.operator = extraction_operator(p, k, i, en)
                functions = self.bernstein_functions
            else:
                print('Here')
                self.operator = extraction_operator(p, k, i, en)
                functions = matrix_mult(self.operator, self.bernstein_functions)
        elif p == 3 and k == 2:
            if en == 1:
                functions = self.bernstein_functions
                self.operator = None
            else:
                self.operator = extraction_operator(p, k, i, en)
                functions = matrix_mult(self.operator, self.bernstein_functions)
        else:
            raise ValueError('Either P or K is incorrect')

        #perform change of coordinates to map the current functions defined over [0,1] -> [le, re] assuming
        #le != 0 and re != 1 This will be done using the composition function defined above this is found
        #using the equations x(xi) = c(xi) + d , x(0) = le, x(1) = re giving a solution of
        #c = -1/(le-re) and d = le/(le-re)
        if le != 0 and re != 1:
            self.coordinates = lambda xi: (-1/(le-re)) * xi + (le/(le-re))
            self.spline_functions = np.array([func_comp(functions[j], self.coordinates) for j in range(0, p + 1)])
        else:
            self.coordinates = None
            self.spline_functions = functions






'''
bst = BernsteinBasis(4, 2, 6)
x1 = np.linspace(2, 6, 100)
bst1 = BernsteinBasis(4, 6, 10)
x2 = np.linspace(6, 10, 100)
plt.plot(x1, bst.basis_functions[0](x1), label='B_0^4')
plt.plot(x1, bst.basis_functions[1](x1), label='B_1^4')
plt.plot(x1, bst.basis_functions[2](x1), label='B_2^4')
plt.plot(x1, bst.basis_functions[3](x1), label='B_3^4')
plt.plot(x1, bst.basis_functions[4](x1), label='B_4^4')
plt.plot(x2, bst1.basis_functions[0](x2), label='B_0^4')
plt.plot(x2, bst1.basis_functions[1](x2), label='B_1^4')
plt.plot(x2, bst1.basis_functions[2](x2), label='B_2^4')
plt.plot(x2, bst1.basis_functions[3](x2), label='B_3^4')
plt.plot(x2, bst1.basis_functions[4](x2), label='B_4^4')
plt.title("Bernstein Functions of Degree 4", fontsize=14)
plt.legend(loc = 'upper left')
plt.show()
'''

