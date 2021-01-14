#main.py
import numpy as np
from matplotlib import pyplot as plt
#import utility modules
import basismesh
import quadrature



#number of elements
eN = 7
#degree
p = 2
#continuity
k = p - 1
#quadrature rule
rule = 3
#used for the indicator R.V.
eps = 1e-9
#Young's Modulus
E = None
#cross sectional area
A = None
#penalty peramater for constrains
pen = None
#traction froce
traction = None
#displacement constraint at the left endpoint
u0 = None

physical_geometry = [ 0, 3 ]
flex_geometry = [ 0, 4 ]


mesh = basismesh.buildMesh( p, en, flex_geometry )

points, weights, IE = quadrature.getQuadrature(rule, eN)
