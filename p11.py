# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 13:43:47 2019

@author: Akhil
"""
l=[]
x=int(input("Enter number to find the square numbers:"))
while (x!=0):
    if (x<0):
        print("Please enter +ve number only or press 0 to exit")
        x=int(input("Enter number to find the square numbers:"))
        if (x==0):
            break
    for i in range(4,x+1):
        for j in range(2,int(i**0.5)+1):
            if (i%int(j**2)==0):
                l.append(i)
                break
    print("Square numbers are:",end='')
    for i in l:
        print(i,end=",")
    print()
    l.clear()
    x=int(input("Enter number to find the square numbers:"))
        