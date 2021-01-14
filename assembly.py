#assembly.py
import numpy as np
import evals

def assembleK( nodes, ops, EG, qp, qw, IE ):
    K = np.zeros((nodes.size, nodes.size))

    for i in range(qp.shape[0]):
            cElem = IE[i]
        for j in range(qp.shape[1]):

            #evaluate basis and geometry at gauss point [i, j]
            N, dNdxi = evals.computeBasis(e, ops[e], qp[e] )
            x, dxdxi = evals.computeGeom(e, nodes, EG, N, dNdxi)
            eps = evals.chi( x )

