# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 13:17:02 2019

@author: Akhil
"""
i=[]
f=[]
s=[]
x=""
while ((0 not in i) and (0.0 not in f) and ("end" not in s) and ("END" not in s)):
    x=input("Enter something,(enter 0 or end or END to stop accepting inputs) : ")
    try:
        temp=int(x)
        if (temp!=0):
            i.append(temp)
        else:
            break
        #print(i) #For Testing
    except ValueError:
        try:
            temp=float(x)
            if (temp!=0.0):
                f.append(temp)
            else:
                break
            #print(f) #For Testing
        except ValueError:
            temp=x
            if (temp!="end" and temp!="END"):
                s.append(temp)
            else:
                break
            #print(s) #For Testing
print("All the integers entered are:")
print(i)
print("All the float values entered are:")
print(f)
print("All the strings entered are:")
print(s)