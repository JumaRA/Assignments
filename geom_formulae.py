__author__ = 'rebecca'

from numbers import Number
def area_rectangle(length,width: Number) -> Number:
    """
    calculates the area of a rectangle with given length and width
    :param length: the side length
    :param width: the side width
    :return:the area of a rectangle
    >>>area_rectangle(4,8)
    32
    """
    return (length*width)

from numbers import Number
from numpy import*
def Area_Circle(radius: Number) -> Number:
    """
    calculates the area of a circle with a given radius
    :param radius: radius of the circle
    :return:area of the circle
    >>> Area_Circle(10)
    314.15926
    """
    return (pi*radius*radius)

from numbers import Number
from numpy import*
def Circle_Perimeter(radius: Number) -> Number:
    """
    calculates the circumference of a circle with a given radius
    :param radius: radius of the circle
    :return:Perimeter of the circle
    >>> Circle_Perimeter(10)
    62.831853
    """
    return (2*pi*radius)

