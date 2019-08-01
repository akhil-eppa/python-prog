# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 12:49:56 2019

@author: Akhil
"""

min=int(input("Enter the mintablenum: "))
max=int(input("Enter the maxtablenum: "))
for i in range(min,max+1):
    for j in range(1,11):
        print(i*j,end=' ')
    print()