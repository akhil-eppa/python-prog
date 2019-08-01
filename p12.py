# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 14:23:36 2019

@author: Akhil
"""

print("Given series is 3,10,21,36 and so on...")
print("Series starting from 1,2,3,4 and so on...")
x=int(input("Enter a number(1-100):"))
if (x>=1 and x<=100):
    print((x**2)+x*(x+1))
flag=1
while (flag==1):
    y=int(input("Do you want to enter another number?(1/0)" ))
    if (y==1):
        x=int(input("Enter a number(1-100):"))
        if (x>=1 and x<=100):
            print((x**2)+x*(x+1))
    else:
        flag=0