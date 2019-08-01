# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 12:00:32 2019

@author: Akhil
"""

x=int(input("Enter a number:"))
arm=0
d=0
temp=x
l=len(str(x))
while (temp!=0):
    d=temp%10
    arm+=pow(d,l)
    temp=temp//10
    
if (arm==x):
    print(x," is an armstrong number.")
else:
    print(x," is not an armstrong number.")