#BasisMesh.py
import numpy as np
import bernstein

class meshGreville( object ):
    ''' class containing the mesh where nodes are gotten from greville points
    '''
    def __init__( self, elemN, pVec, kVec, extraction, funcN, nodes, indexing, bound ):
        ''' Constructs a meshGreville object
            Paramaters:
                elemN ( int ): number of elements
                pVec ( ( elemN, ) ndarray ): An array containing the element degree for each element
                kVec ( ( elemN, ) ndarray ): An array containing the element continuity for each element
                extraction ( ( elemN, p + 1, p + 1 ) ndarray ): 3d matrix containing extraction operators
                funcN ( int ): number of global functions ( indexed from zero )
                nodes ( ( funcN, ) ndarray): equally spaced points across flex domain
                indexing ( ( eN, p + 1 ) ndarray ): local to global function index map
                bound ( ( elemN, ) ndarray ): upper and lower bounds for each element
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
    ''' Builds meshGreville object from a element degree, element numbers, and the flex geometry
        Paramaters:
            p ( int ): The ( uniform ) polynomial degree for each element
            elementN ( int ): the number of elements for the mesh
            flex_geom ( ( 1, 2 ) list ): containing the left and right endpoints of the flex geometry
        Returns:
            meshGreville object
    '''
    functionN = p + elementN - 1
    P = np.array( [ p for el in elementN ] )
    K = np.array( [ p-1 for el in elementN ] )
    operators = np.array( [ bernstein.extractionOperator( p, p-1, i, elementN )
                            for i in range( elementN ) ] )
    nodes = np.linspace( flex_geom[ 0 ], flex_geom[ 1 ], functionN + 1 )
    index_map = np.array( [ [ i+j for j in range( p + 1 ) ] for i in range( elementN ) ] )
    elemB = np.linspace( flex_geom[ 0 ], flex_geom[ 1 ], elementN + 1 )


    return meshGreville( elementN,
                         functionN,
                         [ p for el in elementN ],
                         [ p-1 for el in elementN ],
                         operators,
                         nodes,
                         index_map,
                         elemB )



