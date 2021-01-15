#evals.py
import numpy as np


def computeBasis( e, op, qp ):
    '''evaluates the basis at the quadrature point
       Paramaters:
           e ( int ): the current element
           op ( ( p + 1, p + 1 ) ndarray ): the extraction operator for the current element
           qp ( float ): the quadrature point to evaluate the basis at
       Returns:
           N ( ( p + 1, ) ndarray ): The basis functions evaluated at the point
           dNdxi( ( p + 1, ) ndarray ): The derivatives evaluated at the point
    '''

    return None


def computeGeom( e, nodes, EG, N, dNdxi ):
    '''Evaluates the geometry at the gauss point in computeBasis
       Paramaters:
           e ( int ): element id
           nodes ( ( funcN, ) ndarray ): nodal points to evaluate geometry at
           EG ( ( elemN, ) ) ndarray ): element to global basis function
           N ( ( p + 1, ) ndarray ): basis functions evaluated at the gauss point
           dNdxi( ( p + 1, ) ndarray ): The derivatives evaluated at the point
       Returns:
           x ( float ): quadrature point with change of coordinates applied
           dxdxi ( ): The differential for the quadrature point
    '''


    return None


def chi( x ):
    ''' Detemines if the quadrature point is in the CAD domain
        Paramaters:
             x ( float ): point to test
        Returns:
             eps ( float ): penalty value ( penalty if no, 1 if yes )
    '''

    return None
