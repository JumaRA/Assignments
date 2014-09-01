__author__ = 'rebecca'

from numpy import*


if __name__ == "__main__":
    print("hallo ghana")
    print("hallo world")
    print("this is biriwa")
    print("i love travelling and visiting new places")

    print(pi)

    r=4.6595959
    print(type(r))

    for i in range(10):


        print(i)

    def area(l,w):
        x=l*w
        print(x)
    l = 4
    w= 5
    area(4,5)

def area(r):
    x=((pi)*r*r)
    print("the area of the circle is =",x)
r=10
area(10)

def absolute_value(n):
    if n<0:
        n=-n
        x=n

if __name__ == "__main__":
    a=10
    b=-10
    if absolute_value(a) == absolute_value(b):
        print("The absolute values of", a, "and", b, "are equal")
    else:
        print("The absolute values of", a, "and", b, "are different")


from numpy import*
def perimeter(r):
    p=(2*(pi)*r)
    print("circumference of the circle is=",p)
r=789.99
perimeter(789.99)

from numbers import Number
def square_perimeter(side : Number) -> Number:
    """
    Calculate perimeter of a square from side length.
    @param side: the side length
    @return: the perimeter (same units as side length)
    >>> square_perimeter(4)
    16
    """
    return 4*side

def rectangle_perimeter(length,width):
    """
    this formula gives the perimeter of a rectangle, two opposite sides are equal in a
    rectangle
    >>>rectangle_perimeter(2,1)
    6
    """
    return 2*(length+width)

import geom_formulae
print(geom_formulae.Sphere_Area(15))

from numbers import Number

def square_perimeter(side : Number) -> Number:
    """
    Calculate perimeter of a square from side length.

    @param side: the side length
    @return: the perimeter (same units as side length)

    >>> square_perimeter(4)
    16
    """
    return 4*side


def square_area(side):
    """
    Calculate area of a square from side length.
    @param side: the side length
    @return: the area (units^2 from side)
    >>> square_area(4)
    16
    """
    return side*side

from pylab import *

from HW import *

v_square_area = np.vectorize(square_area)
v_square_perimeter = np.vectorize(square_perimeter)

S = np.linspace(0,10) # our side lengths

A = v_square_area(S)  # the areas
P = v_square_perimeter(S)  # the perimeters

plot(S, A, '-r', label="Area")
plot(S, P, ':b', label="Perimeter")

xlabel('side length')
ylabel('geo values')
title('Square Geo Properties')
legend(loc='upper right')

show()

import geom_formulae
print(geom_formulae.Hexagon_Perimeter(20))


from HW import *
from nose.tools import *

def test_square_area_int():
    assert square_area(1) == 1
    assert square_area(4) == 16
    s = 5
    assert square_area(s*2) == 4*square_area(s)


eps = 1e-6
def test_square_area_double():
    assert 25/4 - eps < square_area(2.5) < 25/4 + eps

@raises(TypeError)
def test_square_area_other():
    square_area("a string")

def test_square_perimeter_int():
    s = 5
    assert square_perimeter(s) == 20
    assert square_perimeter(4*s) == square_perimeter(s)*4


def test_fail_square_perimeter():
    assert square_perimeter(4) == 20