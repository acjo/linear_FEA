#BasisMesh.py
import numpy as np
import bernstein

class meshGreville( object ):
    ''' class containing the mesh where nodes are gotten from greville points
    '''
    def __init__( self, elemN, pVec, kVec, extraction, funcN, nodes, indexing, bound ):
        ''' constructor
        '''
        self.elemN = elemN #number of elements
        self.funcN = funcN #global function number
        self.pVec = pVec #polynomial degree for each element
        self.kVec = kVec #continuity for each element
        self.extraction = extraction #extraction operator for each element
        self.nodes = nodes #nodes (evenly space)
        self.map = indexing #element to global basis function index map
        self.boundaries = bound #bounds for element


def buildMesh( p, elementN, flex_geom ):
    functionN = p + elementN
    P = np.array( [ p for el in elementN ] )
    K = np.array( [ p-1 for el in elementN ] )
    operators = np.array( [ bernstein.extractionOperator( p, p-1, i, elementN )
                            for i in range( elementN ) ] )
    nodes = np.linspace(flex_geom[0], flex_geom[1], functionN)
    index_map = np.array( [ [ i+j for j in range( p + 1 ) ] for i in range( elementN ) ] )
    elemB = np.linspace(flex_geom[0], flex_geom[1], elementN + 1)


    return meshGreville( elementN,
                         functionN,
                         [ p for el in elementN ],
                         [ p-1 for el in elementN ],
                         operators,
                         nodes,
                         index_map,
                         elemB )



