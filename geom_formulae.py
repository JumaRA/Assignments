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

from numbers import Number
from numpy import*
def Volume_Cylinder(radius,height: Number) -> Number:
    """
    Calculates the volume of a cylinder with a given radius and height
    :param radius: base radius of cylinder
    :param height: height of the cylinder
    :return:the volume of the cylinder
    >>>Volume_Cylinder(7,1)
    153.93804
    """
    return (pi*radius*radius*height)

def Cube_Volume(side: Number) -> Number:
    """
    calculates the volume of a cube given the side, all sides are equal
    :param side: the length of the side of the cube
    :return:the volume of the cube
    >>>Cube_Volume(2)
    8
    """
    return side*side*side

def Cube_Area(side: Number) -> Number:
    """
    calculates the area of a cube given the length of any side, all sides are equal
    :param side: length of the side
    :return:the surface area of the cube
    >>>Cube_Volume(4)
    96
    """
    return 6*side*side

from numbers import Number
from numpy import*
def Sphere_Area(radius: Number) -> Number:
    """
    calculates the surface area of a sphere with a given radius
    :param radius: radius of the sphere
    :return:the surface area of the sphere
    >>>Sphere_Area(3)
    113.097334
    """
    return (4*pi*radius*radius)

from numbers import Number
from numpy import*
def Cone_Volume(radius,height: Number) -> Number:
    """
    calculates the volume of cone with a given radius and height
    :param radius: base radius of the cone
    :param height: height of the cone
    :return:the volume of the cone
    >>>Cone_Volume(7,2)
    102.625
    """
    return (1/3)*pi*radius*radius*height

def Cuboid_Volume(length,width,height: Number) -> Number:
    """
    calculates the volume of cube given the length, width and radius
    :param length: the base length
    :param width: the base width
    :param height: height of the cuboid
    :return:the volume of the cuboid
    >>>Cuboid_Volume(2,3,4)
    """
    return length*width*height

def Trapezium_Area(length1,length2,height: Number) -> Number:
    """
    calculates the area of a trapezium using a given length of the parallel sides and the height
    :param length1: length of the shorter parallel side
    :param length2: length of the longer parallel side
    :param height: height of the trapezium
    :return:the area of the trapezium
    >>>Trapezium_Area(2,4,6)
    18
    """
    return (1/2)*(length1+length2)*height

def Hexagon_Perimeter(side: Number) -> Number:
    """
    calculates the perimeter of a regular hexagon, the length of the six sides are all equal
    :param side: length of the side of the hexagon
    :return:perimeter of the hexagon
    >>>Hexagon_Perimeter(10)
    60
    """
    return 6*side

def triangle_area(base,height: Number) -> Number:
    """
    calculates the area of a triangle using a given base and height
    :param base: the base length of the triangle
    :param height: height of the triangle
    :return:the area of the triangle
    >>>triangle_area(2,9)
    9
    """
    return (1/2)*base*height


