#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:49:31 2019

@author: sweta
"""

# Write the following program.
#(i) WAP to print 100 random strings whose length between 6 and 8.
#WAP to print all prime numbers between 600 and 800.
#(iii) WAP to print all numbers between 100 and 1000 that are divisible by 7 and 9.

import string as s
import random as r
print ("String --> ",s.ascii_letters)
for i in range(0, 100):
    passwd=r.sample(s.ascii_letters, r.randint(6,8))
    passwd="".join(passwd)
    print (passwd)
###############################################################################    
def IsPrime(n):
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return 0
        return 1
for i in range(600, 800):
    if IsPrime(i):
        print("List of all prime numbers between 600 to 800:",i)
       
###############################################################################
for i in range(100, 1000):
    if i%7==0:
        print("Number divisible by 7 is:",i)
    if i%9==0:
        print("Number divisible by 9 is:", i)