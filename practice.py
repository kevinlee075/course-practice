# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 19:47:10 2021

@author: Lenovo
"""

import math
n = int(input('Number of sides = '))
s = float(input('length of polygon = '))
def tan_1(n):
    return math.tan(math.pi/n)
def area_polygon(n, s):
    return 0.25 * n * s * s / tan_1(n)
def perimeter_polygon(n, s):
    return s * n
def polysum(n, s):
    polysum = area_polygon(n, s) + perimeter_polygon(n, s) * perimeter_polygon(n, s)
    return round(polysum, 4)


    