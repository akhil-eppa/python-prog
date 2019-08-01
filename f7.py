# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 10:25:25 2019

@author: Akhil
"""

def maximum_product_two_numbers(length,*argv):
    argv=list(argv)
    m1=max(argv[0:length])
    argv[0:length].remove(m1)
    m2=max(argv[0:length-1])
    return m1*m2

print(maximum_product_two_numbers(5,1,2,3,4,5))