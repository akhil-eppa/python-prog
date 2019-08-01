# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 13:35:59 2019

@author: Akhil
"""
i=1
fact=1
x=int(input("Enter a number:"))
for j in range(1,x):
    fact=fact*j
    if fact%x==0:
        break
print(j)