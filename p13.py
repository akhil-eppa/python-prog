# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 14:30:53 2019

@author: Akhil
"""
x=int(input("Enter a positive number: "))
while (x<0):
    x=int(input("Enter only a positive number: "))
sum=x
while (len(str(sum))>1):
    temp=0
    for i in str(sum):
        temp=temp+int(i)
    sum=temp
print(sum)
    