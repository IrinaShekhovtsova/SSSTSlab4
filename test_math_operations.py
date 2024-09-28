import pytest
import math_operations

def test_modulo():
	assert math_operations.modulo(4,3) == 1
	with pytest.raises(ZeroDivisionError):
		math_operations.modulo(3,0)

def test_logarithm():
	assert math_operations.logarithm(10,100) == 2
	assert math_operations.logarithm(10,1) == 0
	with pytest.raises(ValueError):
		math_operations.logarithm(2,-1)
