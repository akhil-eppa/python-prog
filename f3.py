# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 20:30:08 2019

@author: Akhil
"""

def complex_numbers_mult(l1,l2):
    if (len(l1)!=len(l2)):
        print("Error: Lists of unequal length")
        return False
    pro=[1,0]
    for i in range(len(l1)):
        p0=pro[0]*l1[i]-(pro[1]*l2[i])
        p1=pro[0]*l2[i]+(pro[1]*l1[i])
        pro=[p0,p1]
    return pro
l1=input("Enter list 1:").split(",")
l2=input("Enter list 2:").split(",")
l1=list(map(lambda i:int(i),l1))
l2=list(map(lambda i:int(i),l2))
res=complex_numbers_mult(l1,l2)
if res!=False:
    print("Complex numbers multiplication of",end=" ")
    for i in range(len(res)):
        print("(",l1[i],"+",l2[i],"j)*",end="",sep="")
    print("\b",end="")
    print(" is (",res[0],"+",res[1],"j)",sep="")
    
