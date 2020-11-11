#test_Berstein_Basis.py
'''
Tests the BersteinBasis.py class
'''

import Bernstein_Basis
import pytest
import numpy as np
from matplotlib import pyplot as plt

@pytest.fixture
def set_up_basis():
    basis_1 = Bernstein_Basis.BernsteinBasis(4)
    return basis_1

def test_constructor(set_up_basis):
    basis_1 = set_up_basis
    with pytest.raises(TypeError) as excinfo:
        Bernstein_Basis.BernsteinBasis("3")
    assert excinfo.value.args[0] == 'The Bernstein polynomials are not of an integer degree'
    assert len(basis_1.basis_functions) == 5, 'The amount of basis functions is incorrect'
    assert (basis_1.coefficients == np.array([1, 4, 6, 4, 1])).all(), 'Basis coefficients calculated incorrectly'
    assert basis_1.basis_functions[0](0) == 1., 'Basis function 0 out of 4 computed incorrectly'
    assert basis_1.basis_functions[1](0.2) - 0.4096 < 1e-6, 'Basis function 1 out of 4 computed incorrectly'
    assert basis_1.basis_functions[2](0.4) - 0.6144 < 1e-6, 'Basis function 2 ouf of 4 computed incorrectly'
    assert basis_1.basis_functions[3](0.6) - 0.3456 < 1e-6, 'Basis function 3 out of 4 computed incorrectly'
    assert basis_1.basis_functions[4](0.8) - 0.4096 < 1e-6, 'Basis function 4 out of 4 computed incorrectly'

    #REMOVE COMMENT TO GRAPH BERNSTEIN POLYNOMIALS
    '''
    x = np.linspace(0,1,100)
    plt.plot(x, basis_1.basis_functions[0](x), label='B_0^4')
    plt.plot(x, basis_1.basis_functions[1](x), label='B_1^4')
    plt.plot(x, basis_1.basis_functions[2](x), label='B_2^4')
    plt.plot(x, basis_1.basis_functions[3](x), label='B_3^4')
    plt.plot(x, basis_1.basis_functions[4](x), label='B_4^4')
    plt.title("Bernstein Functions of Degree 4", fontsize=14)
    plt.legend(loc = 'upper left')
    plt.show()

    '''

    return

#test_constructor(Bernstein_Basis.BernsteinBasis(4))
