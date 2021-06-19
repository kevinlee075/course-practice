# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 19:47:10 2021

@author: Lenovo
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    x = None
    biggestvalue = 0
    Key = aDict.keys()
    for i in Key:
        if len(aDict[i]) > biggestvalue:
            x = i
            biggestvalue = len(aDict[i])
    return x

print(biggest(animals))