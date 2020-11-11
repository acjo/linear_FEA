#test_Legendre_Basis.py

import pytest
import Legendre_Basis


@pytest.fixture
def set_up_basis():
    basis_1 = Legendre_Basis.LegendreBasis(4)
    return basis_1
