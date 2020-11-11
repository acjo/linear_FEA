#ElasticBar.py

import numpy as np
from matplotlib import pyplot as plt
import Bernstein_Basis

#TODO: implement quadrature rule using legendre polynoimals
#computes quadrature points for a given integer value
def compute_quadrature_points(n):
    ''' computes quadrature points for a given integer value
        Paramaters:
        (int) n: how many quadrature points we want
        Returns:
        (list) containing the quadrature points
    '''
    if type(n) != int:
        raise TypeError('The requested rule is not of integer value.')
    elif n < 1 or n > 3:
        raise ValueError('Out of range, the requested rule needs to be a positive integer less than four.')
    else:
        if n == 1:
            return [0]
        elif n == 2:
            return [-1/np.sqrt(3), 1/np.sqrt(3)]
        else:
            return [-np.sqrt(3/5), 0 , np.sqrt(3/5)]
    return

#computes the quadrature weights for a given integer value
def compute_quadrature_weights(n):
    ''' computes quadrature points for a given integer value
        Paramaters:
        (int) n: how many quadrature weights we want
        Returns:
        (list) containing quadrature weights
    '''
    if type(n) != int:
        raise TypeError('The requested rule is not of integer value.')
    elif n < 1 or n > 3:
        raise ValueError('Out of range, the requested rule needs to be a positive integer less than four.')
    else:
        if n == 1:
            return [2]
        elif n == 2:
            return [1,1]
        else:
            return [5/9, 8/9, 5/9]
    return


def compute_bernstein_basis(n, le = 0, re = 1):
    '''Creates an instance of the BernsteinBasis class
       Paramters:
       (int) n: degree
       (float) le, re: left end point, right end point
    '''
    return Bernstein_Basis.BernsteinBasis(n, le, re)

def compute_spline_basis(p, k, le, re, i, en):
    '''Computes spline basis for a given element
       Paramaters:
       (int) p: polynomial degree
       (int) k: continuity level
       (float) le left endpoint of element domain
       (float) re right endpoint of element domain
       (int) i: element number
       (int) en: total number of elements
    '''
    return Bernstein_Basis.SplineBasis(p, k, le, re, i, en)

def element_positions(le, re, sn):
    '''gives the element positions given a left endpoint of the domain, right endpoint of the domain, an element numbers
       Paramaters:
       (float)le, re: left and right domain endpoints
       (int) sn: number of element numbers
       Raises:
       TypeError: if the element numbers is not an int
       ValueError: if the re endpoint is less than the left endpoint
       ZeroDivisionError: if the number of wanted elements is 0
       Returns:
       (list) containing the elements boundaries
    '''
    if type(sn) != int:
        raise TypeError('The amount of wanted segments is not of integer value.')
    elif re -le < 1e-6:
        raise ValueError('The left endpoint is larger than the right endpoint.')
    elif sn == 0:
        raise ZeroDivisionError('The amount of segments wanted is zero, divide by zero error.')
    else:
        total_length = abs(le) + abs(re)
        element_length = total_length / sn
        element_positions = [le + (element_length * i) for i in range(0, sn + 1)]
        return element_positions

#FIXME: understand omega and omega_hat paramaterization better

#define physical domain for our axial bar

#Omega_F
physical_start = -2
physical_end = 4

#Omega_C
#axial bar domain physical_start <= axial_bar_start and axial_bar_end <= physical_end
bar_start = 0
bar_end = 4

if bar_start - physical_start < 0 or physical_end - bar_end < 0:
    raise ValueError('The Cad domain is not contained in the physical domain')


'''
Inputs:
'''
#degrees (assume constant for now)
p = 3
#smoothness (assume cnstant for now)
k_continuity = 2
#quadrature rules for each element
rule =[3, 3, 3]
#penalty paramater
eps = 8e-8
#young's modulus
E = None
#cross sectional area
A = None
#penalty paramater
P = None
#the traction force at left endpoint
h_l = None
#u_o the displacement constraint
u_0 = None

#domain for parametric as well as element number
le, re, en = -1, 1, 2
#defines element degree p
#defines continuity for spline basis

#left and right endpoints for each element
element_boundaries = element_positions(le, re, en)

#basis functions for segments in parametric domain
bases = [compute_bernstein_basis(p, element_boundaries[i], element_boundaries[i+1]) for i in range(0, en)]

spline_bases = [compute_spline_basis(p, k_continuity, element_boundaries[i], element_boundaries[i+1], i, en) for i in range(0, en)]



'''
Visualization
'''
markers = ['-', '--', '-.', ':', '-o', '-*']

#visualizing parametric domain
ax1 = plt.subplot(121)
for i in range(0, en):
    domain = np.linspace(element_boundaries[i], element_boundaries[i+1], 100)
    for k in range(0, p + 1):
        rnge = bases[i].bernstein_functions[k](domain)
        #plot_label = 'B_' + str(k) +'^' + str(k) + str(element_boundaries[i]) + str(element_boundaries[i+1])
        ax1.plot(domain, rnge)
    marker = 'k' + markers[i]
    ax1.plot(np.linspace(element_boundaries[1 + i], element_boundaries[i + 1],10), np.linspace(-0.5, 1.5, 10), marker, ms = 4, label = 'Upper Element Boundary ' + str(i+1))
plt.title('Parametric Domain Bernstein Basis P' + str(p) )
plt.legend(loc='best', prop={'size': 6})
#bbox_to_anchor(1.1,1)
ax2 = plt.subplot(122)
for i in range(0, en):
    domain = np.linspace(element_boundaries[i], element_boundaries[i+1], 100)
    for k in range(0, p+1):
        rnge = spline_bases[i].spline_functions[k](domain)
        ax2.plot(domain, rnge)
plt.title('Paramateric Domain Spline Basis P' + str(p) + ' C' + str(k_continuity) )

'''
#FIXME: figure out a way to graph the global basis functions
ax3 = plt.subplot(133)
for i in range(0, en):
    domain = np.linspace(element_boundaries[i], element_boundaries[i+1], 100)
    for k in range(0, p+1):
        rnge = spline_bases[i].spline_functions[k](domain)
        ax2.plot(domain, rnge)
plt.title('Paramateric Domain Spline Basis P' + str(p) + ' C' + str(k_continuity) )
'''

plt.show()
