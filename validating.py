__author__ = 'rebecca'

from numpy import *
from numbers import Number
#from geom_formulae import *
def dim_validate(dim):
    """
    Test if dim is a Number and is >= 0.

    >>> dim_validate(5)
    True

    >>> dim_validate(-5)
    False

    >>> dim_validate("a string")
    False
    """
    return isinstance(dim, Number) and dim >= 0

def dim_sign(dim):
    """
    Tests if dim is a Number and is >=0

    >>> dim_sign(5)
    True
    >>> dim_sign(-5)
    False
    """
    return dim>=0

def dim_letter(dim):
    """
    Tests if dim is not a string
    >>> dim_letter(7)
    True
    """
    return isinstance(dim, Number)

def ddmm_validate(dim1,dim2):
    """
    Tests if ddmm is a Number and is >=0
    >>> ddmm_validate(2,3)
    True

    >>> ddmm_validate(-2,3)
    False

    >>> ddmm_validate(2,-3)
    False
    """
    return isinstance (dim1, Number) and isinstance (dim2, Number) and dim1>=0 and dim2>=0

def three_validate(dim1,dim2,dim3,):
    """
    Tests if three is a Number and is >=0

    >>> three_validate(1,2,3)
    True
    >>> three_validate(-1,2,3)
    False
    >>> three_validate(1,-2,3)
    False
    >>> three_validate(1,2,-3)
    False
    """
    return isinstance (dim1, Number) and isinstance (dim2, Number) and isinstance (dim3, Number) and dim1>=0 and dim2>=0 and dim3>=0

def dim_complete(dim):
    """
    Tests that dim is provided

    >>> dim_complete(1)
    True
      """
    if dim is not None:
        return True