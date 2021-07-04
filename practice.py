# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 19:47:10 2021

@author: Lenovo
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    expon = 0
    while base ** expon < num:
        expon += 1
    if abs(num - base ** expon) >= abs(num - base ** (expon-1)):
        result = expon - 1
    else:
        result = expon
    return result