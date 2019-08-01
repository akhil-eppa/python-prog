# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 21:04:36 2019

@author: Akhil
"""
l=""
def buildr(x,d):
    global l
    if d==0:
        l=l+x
        return
    length=len(x)
    if length<d:
        return
    mini=0
    for i in range(d):
        if x[i]<x[mini]:
            mini=i
    l=l+x[mini]
    new=x[mini+1:length-mini]
    buildr(new,d-mini)
d=int(input("Enter number of digits:"))
x=input("Enter String:")
buildr(x,d)
print("The smallest number from \"",x,"\" is",l)