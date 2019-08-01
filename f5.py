# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 21:40:29 2019

@author: Akhil
"""

def square(start=1,end=100):
    l=[]
    for i in range(start,end+1):
        if i**0.5==int(i**0.5):
            l.append(i)
    return l
x=int(input("Enter number 1:"))
y=int(input("Enter number 2:"))
if ((x<0 or y<0) or x<y ):
    p=square(x,y)
    print("Perfect squares between",x,"and",y,"are",p,"and total count is",len(p) )