# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 12:17:27 2019

@author: Akhil
"""

l=[]
pos=[]
neg=[]
x=int(input("Enter a number: "))
while (x!=0):
    l.append(x)
    if x>0:
        pos.append(x)
    else:
        neg.append(x)
    x=int(input("Enter another number: "))
print(l)
print(pos+neg)