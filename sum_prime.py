#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:46:02 2019

@author: sweta
"""

# WAP to add all prime numbers from 1 to n and n is given by user.

n = int(input("Enter a No: "))
p=0
for j in range(2, n+1):
    f=0
    for i in range(2, int(j/2) + 1):
        if j % i == 0:
            f=1
            break
    if f==0:
       p=p+j
print("Sum of all prime numbers are:",p)       