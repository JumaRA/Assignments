__author__ = 'rebecca'
from numpy import *
from geom_formulae import *
from validating import *
from nose.tools import *


def test_area_rectangle_int():
    assert area_rectangle(2,3) == 6
    assert area_rectangle(7,4) == 28
    length = 5
    width = 6
eps = 1e-6
def test_area_rectangle_double():
    assert 30/4 - eps < area_rectangle(1.5,5) < 30/4 + eps



def test_Area_Circle_int():
    assert Area_Circle(1) == pi
    assert Area_Circle(7) == 153.93804002589985
    radius = 14

eps = 1e-6
def test_Area_Circle_int():
     assert 307.8760800517997/2 - eps < Area_Circle(7) <307.8760800517997/2 + eps

def test_Circle_Perimeter_int():
    radius = 7
    assert Circle_Perimeter(radius) == 43.982297150257104
    assert Circle_Perimeter(4*radius) == Circle_Perimeter(radius)*4



def test_Volume_Cylinder_int():
    assert Volume_Cylinder(1,2) == 6.283185307179586
    assert Volume_Cylinder(3,4) == 113.09733552923255
    radius = 5
    height = 4

eps = 1e-6
def test_Volume_Cylinder_double():
    assert 628.3185307179587/2 - eps < Volume_Cylinder(5,4) < 628.3185307179587/2 + eps



def test_Cube_Volume_int():
    assert Cube_Volume(1) == 1
    assert Cube_Volume(2) == 8
    side = 3

eps = 1e-6
def test_square_area_double():
    assert 270/10 - eps < Cube_Volume(3) < 270/10 + eps

def test_Cube_Area_int():
    side = 5
    assert Cube_Area(side) == 150

def test_Cube_Area():
    assert Cube_Area(10) == 600



def test_Sphere_Area_int():
    assert Sphere_Area(2) == 50.26548245743669
    assert Sphere_Area(3) == 113.09733552923255
    radius = 7
eps = 1e-6
def test_Sphere_Area_double():
    assert 2463.0086404143976/4 - eps < Sphere_Area(7) < 2463.0086404143976/4 + eps



def test_Cone_Volume_int():
    assert Cone_Volume(1,4) == 4.1887902047863905
    assert Cone_Volume(2,6) == 25.132741228718345
    radius = 5
    height = 7

eps = 1e-6
def test_Cone_Volume_double():
    assert 733.0382858376184/4 - eps < Cone_Volume(5,7) < 733.0382858376184/4 + eps



def test_Cuboid_Volume_int():
    assert Cuboid_Volume(1,4,6) == 24
    assert Cuboid_Volume(2,6,5) == 60
    length = 5
    width =  8
    height = 7
eps = 1e-6
def test_Cuboid_Volume_double():
    assert 840/3 - eps < Cuboid_Volume(5,8,7) < 840/3 + eps



def test_Trapezium_Area_int():
    assert Trapezium_Area(2,8,6) == 30
    assert Trapezium_Area(1,7,2) == 8
    length1 = 5
    length2 = 7
    height =  12
eps = 1e-6
def test_Trapezium_Area_double():
    assert 288/4 - eps < Trapezium_Area(5,7,12) < 288/4 + eps



def test_Hexagon_Perimeter_int():
    assert Hexagon_Perimeter(10) == 60
    assert Hexagon_Perimeter(3) ==  18
    side = 7
    assert Hexagon_Perimeter(side*2) == 2*Hexagon_Perimeter(side)

eps = 1e-6
def test_Hexagon_Perimeter_double():
    assert 60/2 - eps < Hexagon_Perimeter(5) < 60/2 + eps


def test_triangle_area_int():
    assert triangle_area(11,2) == 11
    assert triangle_area(4,7) ==  14
    base =  5
    height = 6

eps = 1e-6
def test_triangle_area_double():
    assert 45/3 - eps < triangle_area(5,6) < 45/3 + eps




