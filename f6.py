# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 21:50:03 2019

@author: Akhil
"""
def bin_diff(num1,num2):
    #num1=bin(num1)
    #num2=bin(num2)
    num1 = '{:08b}'.format(num1)
    num2 = '{:08b}'.format(num2)
    num1=list(num1)
    num2=list(num2)
    l=[i for i in range(0,len(num1))]
    for i in range(len(num1)):
        if num1[i]==num2[i]:
            l.remove(i)
    return len(l)
    #return len(set(num1)^set(num2))
x=int(input("Enter Number 1:"))
y=int(input("Enter Number 2:"))
print("The number of bits to be flipped is:",bin_diff(x,y))
    