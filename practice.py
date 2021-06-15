# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 19:47:10 2021

@author: Lenovo
"""

import math #To use tangent function, I need to first import the library "math"
n = int(input('Number of sides = ')) #define the number of sides in polygon
s = float(input('length of side = ')) #define the length of every side in polygon
def tan_1(n): #define tan_1(n) as tan(pi/n)
    return math.tan(math.pi/n)
def area_polygon(n, s): #define the area of polygon based on the formula in the problem description
    return 0.25 * n * s * s / tan_1(n)
def perimeter_polygon(n, s):
    return s * n #perimeter = s plus s totally n times
def polysum(n, s): #polysum = area + perimeter^2
    polysum = area_polygon(n, s) + perimeter_polygon(n, s) * perimeter_polygon(n, s)
    return round(polysum, 4) #make the answer round to 4 decimal places


    