# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 19:47:10 2021

@author: Lenovo
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    mid_index = len(aStr)//2
    mid = aStr[mid_index]
    if char == mid:
        return True
    elif char < mid:
        x = aStr[:mid_index+1]
        return isIn(char, x)
    elif char > mid:
        x = aStr[mid_index+1:]
        return isIn(char, x)
    else:
        return False