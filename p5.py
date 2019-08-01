# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 12:23:16 2019

@author: Akhil
"""
l=[1,1,2,6,4,2,2,4,2,8]
def digit(n):
    if n<10:
        return l[n]
    elif int(str(n)[-2])%2==0:
        return (6*digit(n//5)*digit(n%10))%10
    else:
        return (4*digit(n//5)*digit(n%10))%10
x=int(input("Enter a number: "))
print("first non zero digit of factorial is : ",digit(x))
