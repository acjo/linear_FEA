#test_ElasticBar.py

import ElasticBar
import pytest
import numpy as np
import Bernstein_Basis


def test_compute_quadrature_points():
    assert len(ElasticBar.compute_quadrature_points(1)) == 1, 'Only one quadrature point was requested, a different number of points was given.'
    assert ElasticBar.compute_quadrature_points(1) == np.array([0]), 'The one quadrature point given is incorrect.'
    assert len(ElasticBar.compute_quadrature_points(2)) == 2, 'Two quadrature points were requested, a different number of points was given.'
    assert (ElasticBar.compute_quadrature_points(2) - np.array([-1/np.sqrt(3), 1/np.sqrt(3)]) < np.array([1e-6, 1e-6])).all(), 'At least one of the two quadrature points is incorrect.'
    assert len(ElasticBar.compute_quadrature_points(3)) == 3, 'Three quadrature points were requested, a different number of points were given.'
    assert (ElasticBar.compute_quadrature_points(3) - np.array([-np.sqrt(3/5),0, np.sqrt(3/5)]) < np.array([1e-6, 1e-6, 1e-6])).all(), 'At least one of the three quadrature points is incorrect.'
    with pytest.raises(TypeError) as excinfo:
        ElasticBar.compute_quadrature_points(3.6)
    assert excinfo.value.args[0] == 'The requested rule is not of integer value.'
    with pytest.raises(ValueError) as excinfo:
        ElasticBar.compute_quadrature_points(0)
    assert excinfo.value.args[0] == 'Out of range, the requested rule needs to be a positive integer less than four.'
    with pytest.raises(ValueError) as excifno:
        ElasticBar.compute_quadrature_points(4)
    assert excinfo.value.args[0] == 'Out of range, the requested rule needs to be a positive integer less than four.'
    return

def test_compute_quadrature_weights():
    assert len(ElasticBar.compute_quadrature_weights(1)) == 1 , 'Only one quadratrue weight was requested, a different number of weights was given.'
    assert ElasticBar.compute_quadrature_weights(1) == np.array([2]), 'The one quadrature weight was computed incorrectly.'
    assert len(ElasticBar.compute_quadrature_weights(2)) == 2, 'Two quadrature weights were requested, a different number of weights was given.'
    assert (ElasticBar.compute_quadrature_weights(2) == np.array([1,1])).all(), 'At least one of the two quadrature weights was computed incorrectly.'
    assert len(ElasticBar.compute_quadrature_weights(3)) == 3, 'Three quadrature weights were requested, a different number of weights was given.'
    assert (ElasticBar.compute_quadrature_weights(3) - np.array([5/9, 8/9, 5/9]) < np.array([1e-6, 1e-6, 1e-6])).all(), 'At least one of the three quadrature weights was computed incorrectly.'
    with pytest.raises(TypeError) as excinfo:
        ElasticBar.compute_quadrature_weights('3')
    assert excinfo.value.args[0] == 'The requested rule is not of integer value.'
    with pytest.raises(ValueError) as excinfo:
        ElasticBar.compute_quadrature_weights(0)
    assert excinfo.value.args[0] == 'Out of range, the requested rule needs to be a positive integer less than four.'
    with pytest.raises(ValueError) as excinfo:
        ElasticBar.compute_quadrature_weights(4)
    assert excinfo.value.args[0] == 'Out of range, the requested rule needs to be a positive integer less than four.'
    return

def test_segment_points():
    with pytest.raises(TypeError) as excinfo:
        ElasticBar.segment_positions(-2,2,3.2)
    assert excinfo.value.args[0] == 'The amount of wanted segments is not of integer value.'
    with pytest.raises(ValueError) as excinfo:
        ElasticBar.segment_positions(3, -2, 4)
    assert excinfo.value.args[0] == 'The left endpoint is larger than the right endpoint.'
    with pytest.raises(ZeroDivisionError) as excinfo:
        ElasticBar.segment_positions(-4, 4, 0)
    assert excinfo.value.args[0] == 'The amount of segments wanted is zero, divide by zero error.'
    assert (ElasticBar.segment_positions(-2, 2, 2) == np.array([-2, 0, 2])).all()
    return

'''
def test_bezier_extraction():
    basis_1 = Bernstein_Basis.BernsteinBasis(3)
    qp = ElasticBar.compute_quadrature_points(3)
    qw = ElasticBar.compute_quadrature_weights(3)
    for func in basis_1:

'''


















