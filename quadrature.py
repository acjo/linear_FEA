#quadrature.py
import numpy as np


def assembleQuadrature( n, elemN ):
    ''' assembles the quadrature points, weights, and the quadrature point to element index map
        Paramaters:
            n ( int ): number of quadrature points and weights
            elemN ( int ): the number of elements
        Returns:
            points ( ( elemN, n) ndarray ) matrix contain quadrature points
            weightss ( ( elemN, n) ndarray ) matrix contain quadrature weights
            pToE ( ( elemN, ) ndarray ) array containing the index map
        Raises:
            NotImplementedError: if n is not in [1, 2, 3]
    '''
    allowed = { 1, 2, 3 }
    if n not in allowed:
        raise NotImplementedError('Quadrature rule only given for rules 1, 2, and 3.')
    points = np.array( [ getQuadraturePoints( n ) for el in range( elemN ) ] )
    weights = np.array( [ getQuadratureWeights( n ) for el in range( elemN ) ] )
    pToE = [ 0 for i in range( elemN ) ]
    return points, weights, pToE

def getQuadraturePoints( n ):
    '''returns the quadrature points for a given n in [1, 2, 3]
       Paramaters:
           n ( int ): number of quadrature points
       return
           ( ( n, ) ndarray ): array containing all quadrature points
    '''

    if n == 1:
        return np.array( [ 0 ] )
    elif n == 2:
        return np.array( [ -1 / np.sqrt( 3 ), 1 / np.sqrt( 3 ) ] )
    else:
        return np.array( [ -np.sqrt( 3 / 5), 0, np.sqrt( 3 /5 ) ] )

def getQuadratureWeights( n ):
    '''returns the quadrature weights for a given n in [1, 2, 3]
       Paramaters:
           n ( int ): number of quadrature weights
       return
           ( ( n, ) ndarray ): array containing all quadrature weights
    '''

    if n == 1:
        return np.array( [ 2 ] )
    elif n == 2:
        return np.array( [ 1, 1 ] )
    else:
        return np.array( [ 5 / 9., 8 / 9., 5 / 9. ] )

