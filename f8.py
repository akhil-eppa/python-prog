# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 10:48:39 2019

@author: Akhil
"""

def max_zeroes_cnt(x):
    if (x==0 or x&(x-1)==0):
        return -1
    x=bin(x)[2:]
    max=0
    count=0
    flag=0
    for i in range(len(x)):
        if x[i]=='1':
            flag=1
        if (flag==1 and x[i]=='0'):
            count+=1
        if i>1:
            if (x[i]=='1' and x[i-1]=='0'):
                if count>max:
                    max=count
                    count=0
    return max
x=int(input("Enter number:"))
print("Maximum zeros between two 1\'s for number",x,"is",max_zeroes_cnt(x)) 
        