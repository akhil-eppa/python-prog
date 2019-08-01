# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 11:44:23 2019

@author: Akhil
"""

x=0
l=[]
sum=0
print("Enter numbers. When you enter 0 accepting of numbers stops")
while (0 not in l):
    x=int(input("Enter a number: "))
    l.append(x)
    sum+=x
print("Sum of all numbers is: ",sum)
    
print("Enter words. When you enter \'END\' or \'end\' , accepting of words stops")
x=""
l=[]
word=""
while (("END" not in l) and ('end' not in l)):
    x=input("Enter a string: ")
    l.append(x)
    word=word+x
print("Concatenation of all words entered: ",word[0:-3])