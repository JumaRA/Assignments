__author__ = 'rebecca'
print("hallo ghana")
print("hallo world")
print("this is biriwa")
print("i love travelling and visiting new places")

from numpy import*
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

from numpy import*
def area(r):
    x=((pi)*r*r)
    print("the area of the circle is =",x)
r=10
area(10)

def absolute_value(n):
    if n<0:
        n=-n
        x=n
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


