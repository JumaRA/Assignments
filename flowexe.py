__author__ = 'rebecca'
from numbers import Number
from geom_formulae import *
from numpy import*


def dim_validate(radius):
    if (dim_validate(radius)):
        return Area_Circle(radius)
    elif type(radius)== str:
        raise TypeError("value is a string")
    else:
        raise ValueError("side is less than 0: "+str(radius))

Area_Circle(-4)
