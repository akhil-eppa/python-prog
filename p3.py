# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 14:53:35 2019

@author: Akhil
"""
import tensorflow
x=int(input("Enter number of trailing zeroes in factorial: "))
if (x==1):
    print(5)
else:
    for i in range(5,(5*x)+1):
        temp=i
        f=5
        count=0
        while f<=temp:
            count+=temp//f
            f=f*5
        if (count==x):
            print(i)
            break