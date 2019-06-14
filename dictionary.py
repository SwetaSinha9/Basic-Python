#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 14:33:47 2019

@author: sweta
"""
# LEARNING  : How to use Dictionary, add, delete, search in Dictionary
# D is a dictionary defined as D= {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}.
#(i) WAP to add new entry in D; key=8 and value is 8.8
#(ii) WAP to remove key=2.
#(iii) WAP to check weather 6 key is present in D.
#(iv) WAP to count the number of elements present in D.
#(v) WAP to add all the values present D.
#(vi) WAP to update the value of 3 to 7.1.
#(vii) WAP to clear the dictionary.


D= {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
D[8] = 8.8
print ("Dictionary After Adding (8): ", D)  
##############################################################################

D= {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
del D[2]
print ("Dictionary After deleting (2): ", D)
###############################################################################

D= {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
print ("Is Key  Present: ", 6 in D)
###############################################################################

D= {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
print ("Number of element present: ", len(D))
###############################################################################

D= {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
print ("Sum of Value: ", sum(D.values()))
###############################################################################

D= {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
D[3] = 7.2
print ("Dictionary After Updating (3): ", D)

###############################################################################
D= {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
D.clear()
print ("Dictionary after clear: ", D)