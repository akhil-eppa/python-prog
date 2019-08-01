# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 12:28:54 2019

@author: Akhil
"""
'''
l=[1,2,3,4,5,6,7,8]
print(l)
#x=len(l)
temp=l[-1]
for i in range(len(l)-1):
    l[-i-1]=l[-i-2]
l[0]=temp
print(l)
'''
l=[]
l=input("Enter few numbers:  ").split(",")
for i in range(len(l)):
    l[i]=int(l[i])
count=1
while (len(l)>1):
    temp=l[-1]
    for i in range(len(l)-1):
        l[-i-1]=l[-i-2]
    l[0]=temp
    try:
        l.remove(l[-count])
    except IndexError:
        l.remove(l[0])
    count+=1
print(l[0])
        