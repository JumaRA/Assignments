__author__ = 'rebecca'

from nose.tools import *
from numpy import *
from geom_formulae import *
from validating import *
from nose.tools import *


def test_area_rectangle_int():
    assert area_rectangle(2,3) == area_rectangle(1,6)

@raises(TypeError)
def test_area_rectangle():
    area_rectangle("amm",1)

@raises(ValueError)
def test_area_rectangle():
    area_rectangle(-4,1)

@raises(AttributeError)
def test_area_rectangle():
    area_rectangle(None,1)


def test_Area_Circle_int():
    assert Area_Circle(7) == Area_Circle(7.0)

@raises(TypeError)
def test_Area_Circle():
    Area_Circle("amm")

@raises(ValueError)
def test_Area_Circle():
    Area_Circle(-4)

@raises(AttributeError)
def test_Area_Circle():
    Area_Circle(None)


def test_Circle_Perimeter_int():
   assert Circle_Perimeter(7) == Circle_Perimeter(7.0)
@raises(TypeError)
def test_Circle_Perimeter():
    Circle_Perimeter("amm")

@raises(ValueError)
def test_Circle_Perimeter():
    Circle_Perimeter(-4)

@raises(AttributeError)
def test_Circle_Perimeter():
    Circle_Perimeter(None)


def test_Volume_Cylinder_int():
    assert Volume_Cylinder(2,4) == Volume_Cylinder(2,4)
@raises(TypeError)
def test_Volume_Cylinder():
    Volume_Cylinder("amm",1)

@raises(ValueError)
def test_Volume_Cylinder():
    Volume_Cylinder(-4,2)

@raises(AttributeError)
def test_Volume_Cylinder():
    Volume_Cylinder(None,1)


def test_Cube_Volume_double():
    assert Cube_Volume(1) == Cube_Volume(1.0)
@raises(TypeError)
def test_Cube_Volume():
    Cube_Volume("amm")

@raises(ValueError)
def test_Cube_Volume():
    Cube_Volume(-4)

@raises(AttributeError)
def test_Cube_Volume():
    Cube_Volume(None)

def test_Cube_Area():
    assert Cube_Area(10) == Cube_Area(10.0)

@raises(TypeError)
def test_Cube_Area():
    Cube_Area("amm")

@raises(ValueError)
def test_Cube_Area():
    Cube_Area(-4)

@raises(AttributeError)
def test_Cube_Area():
    Cube_Area(None)


def test_Sphere_Area_int():
    assert Sphere_Area(2) == Sphere_Area(2.0)
@raises(TypeError)
def test_Sphere_Area():
    Sphere_Area("amm")

@raises(ValueError)
def test_Sphere_Area():
    Sphere_Area(-4)

@raises(AttributeError)
def test_Sphere_Area():
    Sphere_Area(None)


def test_Cone_Volume_int():
    assert Cone_Volume(2,4) == Cone_Volume(2,4)
@raises(TypeError)
def test_Cone_Volume():
    Cone_Volume("amm",1)

@raises(ValueError)
def test_Cone_Volume():
    Cone_Volume(-4,2)

@raises(AttributeError)
def test_Cone_Volume():
    Cone_Volume(None,1)

def test_Cuboid_Volume_int():
    assert Cuboid_Volume(1,4,6) == Cuboid_Volume(2,2,6)
@raises(TypeError)
def test_Cuboid_Volume():
    Cuboid_Volume("amm",1,1)

@raises(ValueError)
def test_Cuboid_Volume():
    Cuboid_Volume(-4,2,1)

@raises(AttributeError)
def test_Cuboid_Volume():
    Cuboid_Volume(None,1,1)


def test_Trapezium_Area():
    assert Trapezium_Area(2,8,6) == Trapezium_Area(1,16,6)
def test_Trapezium_Area():
    Trapezium_Area("amm",1,1)

@raises(ValueError)
def test_Trapezium_Area():
    Trapezium_Area(-4,2,1)

@raises(AttributeError)
def test_Trapezium_Areae():
    Trapezium_Area(None,1,1)


def test_Hexagon_Perimeter_int():
    assert Hexagon_Perimeter(10) == Hexagon_Perimeter(10.0)

@raises(TypeError)
def test_Hexagon_Perimeter():
    Hexagon_Perimeter("amm")

@raises(ValueError)
def test_Hexagon_Perimeter():
    Sphere_Area(-4)

@raises(AttributeError)
def test_Hexagon_Perimeter():
    Hexagon_Perimeter(None)


def test_triangle_area_int():
    assert triangle_area(2,2) == triangle_area(4,1)
@raises(TypeError)
def test_triangle_area():
    triangle_area("amm",1)

@raises(ValueError)
def test_triangle_area():
    triangle_area(-4,2)

@raises(AttributeError)
def test_triangle_area():
    triangle_area(None,1)