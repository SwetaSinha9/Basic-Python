#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 14:53:04 2019

@author: sweta
"""

#D is a dictionary defined as D={1:"One",2:"Two",3:"Three",4:"Four", 5:"Five"}. 
# WAP to read all the keys and values from dictionary and write to the file in the given below                                                                                                          
# format: 
#	Key1, Value1
#	Key2, Value2
#   Key3, Value3 

#Learning: How to write into a text files

D={1:"One",2:"Two",3:"Three",4:"Four", 5:"Five"}
fp=open('result2.txt','w')
for k in D:
    print ("Key ", k, " --> ", D[k])
    fp.write(str(k)+ ", " + str(D[k]) + "\n")
fp.close()
print ("Writing done !! \nOpen result.txt to view the content") 
