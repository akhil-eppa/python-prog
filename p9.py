# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 12:57:13 2019

@author: Akhil
"""

a=int(input("Enter Start Number:"))
b=int(input("Enter End Number:"))
prime=[]
pro=1
for i in range(a,b+1):
    if i!=1:
        flag=1
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                flag=0
                break
        if flag==1:
            prime.append(i)
            pro=pro*i
print(prime)
print(pro)
print("The primes between",a,"and",b,"are",prime,"and their product is",pro,".") 