# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 20:17:56 2019

@author: Akhil
"""
l=[]
def elements_power(p):
    if p<1 or p>5:
        p=5
    for i in range(len(l)):
        l[i]=int(l[i])**p
l=input("Enter a few numbers:").split(",")
p=int(input("Enter the power to raise the numbers to:"))
elements_power(p)
print(l)
        
        