# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:15:31 2021

@author: pc
"""

acl=int(input("Ingrese el # de ACL:"))
if acl>=1 and acl<=99:
    print("Es una ACL estandar")
elif acl>=100 and acl<=199:
    print("Es una ACL extendida")
else:
    print("No es un # de ACl valido")