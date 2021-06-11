# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 19:47:10 2021

@author: Lenovo
"""

print('Please think of a number between 0 and 100!')
print('Please think of a number between 0 and 100!')
x = 100
low = 0
high = x
ans = int((low + high)/2)
while abs(ans - x) >= 0:
    print('Is your secret number ' + str(ans) + '?')
    print("Enter 'h' to indicate the guess is too high. \
     Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    s = str(input(''))
    if s == 'h':
        high = ans
    elif s == 'l':
        low = ans
    elif s == 'c':
        break
    else:
        print('Sorry, I did not understand your input.')
    ans = int((low + high)/2)
print('Game over. Your secret number was: ' + str(ans))