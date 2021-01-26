# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:31:00 2021

@author: pc
"""

listasw=[]
listart=[]
listaDispElec=[]
lista=["R1","R2",'R3',
       'S1','S2','S3',
       'R4','R5','PC',
       "Ps5",'Xbox','Laptop']
for i in lista:
    if 'S' in i:
         listasw.append(i)
    elif "R" in i:
         listart.append(i)
    else :
         listaDispElec.append(i)
print('Switches',listasw)
print('Routers',listart) 
print('Dispositivos',listaDispElec) 