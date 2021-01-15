#bernstein.py

import numpy as np
from scipy.special import binom

def bernsteinFunc( n, k ):
    ''' returns the bernstein function for a given non-negative integer
        n and an integer 0 <= k <=  n
        Paramaters:
            n ( int ): degree of bernstein polynomials
            j ( int ): ranging integer
        Returns:
            func ( function ): the bernstein polynomial
        Raises:
            ValueError: if k < 0 or k > n
    '''
    if 0 < k or k > n:
        raise ValueError('k is not in range for the bernstein polynomials')
    def func( x ):
        ''' returns the bernstein function evaluated at x
            Paramaters:
                x ( float ): where to evaluate the function at
            Returns:
                ( float ): the value of the evaluation
        '''
        return binom( n, k ) * ( x ) ** k * ( 1 - x ) ** ( n - k )
    return func

def bernstenFuncD( n, k ):
    ''' returns the derivative of a bernstein function for a given non-negative integer
        n and an integer 0 <= k <=  n
        Paramaters:
            n ( int ): degree of bernstein polynomials
            j ( int ): ranging integer
        Returns:
            funcD ( function ): the derivative of the bernstein polynomial
        Raises:
            ValueError: if k < 0 or k > n
    '''
    if 0 < k or k > n:
        raise ValueError('k is not in range for the bernstein polynomial derivatives')
    def funcD( x ):
        ''' returns the derivative of the bernstein function evaluated at x
            Paramaters:
                x ( float ): where to evaluate the function at
            Returns:
                ( float ): the value of the evaluation
        '''
        return binom( n, k ) * x ** ( k - 1 ) * ( 1 - x ) ** ( n - k - 1) * ( k * ( 1 - x ) - ( n - k) * x)
    return funcD

def extractionOperator( p, k, c, eN ):
    ''' Gets the extraction operator for a given element
        Paramaters:
            p (int): polynomial degree
            k (int): continuity
            c (int): current element number
            eN (int): total element number
        Returns:
            oP ((p+1, p+1) ndarray): the extraction operator
        Raises:
            ValueError: if the c is larger or smaller than it should be for the number of elements
            NotImplementedError: if there is a mismatched P and K
    '''
    if p == 1 and k == 0:
        return np.eye( 2 )
    elif p == 2 and k == 1:
        if eN == 1:
            return np.eye( 3 )
        elif c == 0:
            return np.array([[1, 0, 0],
                             [0, 1, 1/2.],
                             [0, 0, 1/2.]])
        elif c == eN - 1:
            return np.array([[1/2., 0, 0],
                             [1/2., 1, 0],
                             [0, 0, 1]])
        elif 0 < c and c < eN - 1:
            return np.array([[1/2., 0, 0],
                             [1/2., 1, 1/2.],
                             [0, 0, 1/2.]])
        else:
            raise ValueError('c is not in range for ' + str(eN) + ', 2 degree elements.')

    elif p == 3 and k == 2:
        if eN == 1:
            return np.eye(4)
        elif eN == 2:
            if c == 0:
                return np.array([[1, 0, 0, 0],
                                 [0, 1, 1/2., 1/4.],
                                 [0, 0, 1/2., 1/2.],
                                 [0, 0, 0, 1/4.]])
            elif c == 1:
                return np.array([[1/4., 0, 0, 0],
                                 [1/2., 1/2., 0, 0],
                                 [1/4., 1/2., 1, 0],
                                 [0, 0, 0, 1]])
            else:
                raise ValueError( 'c is not in range for 2, 3 degree elements.' )
        elif eN == 3:
            if c == 0:
                return np.array([[1, 0, 0, 0],
                                 [0, 1, 1/2., 1/4.],
                                 [0, 0, 1/2., 7/12.],
                                 [0, 0, 0, 1/6.]])
            elif c == 1:
                return np.array([[1/4., 0, 0, 0],
                                 [7/12., 2/3., 1/3.,1/6.],
                                 [1/6., 1/3., 2/3., 7/12.],
                                 [0, 0, 0, 1/4.]])
            elif c == 2:
                return np.array([[1/6., 0, 0, 0],
                                 [7/12., 1/2., 0, 0],
                                 [1/4., 1/2., 1, 0],
                                 [0, 0, 0, 1]])
            else:
                raise ValueError('c is not in range for 3, 3 degree elements.')
        else:
            if 1 < c and c < eN - 2:
                return np.array([[1/6., 0, 0, 0],
                                 [2/3., 2/3., 1/3., 1/6.],
                                 [1/6., 1/3., 2/3., 2/3.],
                                 [0, 0, 0, 1/6.]])
            elif c == 0:
                return np.array([[1, 0, 0, 0],
                                 [0, 1, 1/2., 1/4.],
                                 [0, 0, 1/2., 7/12.],
                                 [0, 0, 0, 1/6.]])
            elif c == 1:
                return np.array([[1/4., 0, 0, 0],
                                 [7/12., 2/3., 1/3., 1/6.],
                                 [1/6., 1/3., 2/3., 2/3.],
                                 [0, 0, 0, 1/6.]])
            elif c == eN - 2:
                return np.array([[1/6., 0, 0, 0],
                                 [2/3., 2/3., 1/3., 1/6.],
                                 [1/6., 1/3., 2/3., 7/12.],
                                 [0, 0, 0, 1/4.]])
            elif c == eN - 1:
                return np.array([[1/6., 0, 0, 0],
                                 [7/12., 1/2., 0, 0],
                                 [1/4., 1/2., 1., 0.],
                                 [0, 0, 0, 1.]])
            else:
                raise ValueError('c is not in range for ' + str(eN) + ', degree 3 elements.')
    else:
        raise NotImplementedError('Not Implemnted for p != 1, 2, 3 and k != p - 1.')

