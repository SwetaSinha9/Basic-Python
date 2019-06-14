#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 14:56:05 2019

@author: sweta
"""

#Write to the file 100 random strings whose length between 10 and 15.  


import string as s
import random as r
print ("String --> ",s.ascii_letters)
fp=open('result.txt','w')
for i in range(1, 100):
    passwd=r.sample(s.ascii_letters, r.randint(10,15))
    passwd="".join(passwd)
    fp.write(passwd+"\n")
fp.close()
print ("Writing done !! \nOpen result.txt to view the content") 