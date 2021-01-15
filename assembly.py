#assembly.py
import numpy as np
import evals

def assembleK( nodes, ops, EG, qp, qw, IE ):
    ''' Algorithm for assembling the stiffness matrix of the system
        Paramaters:
            nodes ( (n, ) ndarray ): array containing nodal positions
            ops ( ( p + 1, p + 1, eN ) ndarray ): 3d array containing extraction operators
            EG ( ( p + 1, eN ) ndarray ): local to global function index map
            qp ( ( eN, order ) ndarray ): quadrature points for each element
            qw ( ( eN, order ) ndarray ): quadrature weights for each element
            IE ( ( eN, ) ndarray ): quadrature point to element index map
        Returns:
            K ( ( n, n ) ndarray ): The stiffness matrix for the system
    '''
    K = np.zeros((nodes.size, nodes.size))

    for i in range(qp.shape[0]):
            cElem = IE[i]
        for j in range(qp.shape[1]):

            #evaluate basis and geometry at gauss point [i, j]
            N, dNdxi = evals.computeBasis(e, ops[e], qp[e] )
            x, dxdxi = evals.computeGeom(e, nodes, EG, N, dNdxi)
            eps = evals.chi( x )

