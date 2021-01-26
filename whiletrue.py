# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:33:51 2021

@author: pc
"""

while True:
    x=input('Ingrese el numero a contar:')
    if x == 'q' or x =='quit':
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break