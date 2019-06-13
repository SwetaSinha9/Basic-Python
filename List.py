#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:59:14 2019

@author: sweta
"""
# WAP to create two lists of 10 random numbers between 10 and 30; Find 
#(i) Common numbers in the two lists
#(ii) Unique numbers in both the list
#(iii) Minimum in both the list
#(iv) Maximum in both the list
#(v) Sum of both the lists

import random as r
L1=[]
L2=[]
for i in range(10, 30):
    L1.append(r.randint(10,30))
    L2.append(r.randint(10,30))
print("List L1:",L1)
print("List L2:",L2)
print ("max L1: ", max(L1))
print ("min L1: ", min(L1)) 
print ("max L2: ", max(L2))
print ("min L2: ", min(L2))
print("Common numbers in the two lists:",set(L1) & set(L2))
print("Sum of both the lists:",L1+L2)
mysetL1 = set(L1)
mysetL2=set(L2)
print("Unique numbers in the list L1:",mysetL1)
print("Unique numbers in the list L2:",mysetL2)
