#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 14:40:08 2019

@author: sweta
"""
# LEARNING  : How to use Set, add, delete, search in Set
#S1 is a set defined as S1= [10, 20, 30, 40, 50, 60].
#S2 is a set defined as S2= [40, 50, 60, 70, 80, 90].
#(i) WAP to add 55 and 66 in Set S1.
#(ii) WAP to remove 10 and 30 from Set S1.
#(iii) WAP to check whether 40 is present in S1.
#(iv) WAP to find the union between S1 and S2.
#(v) WAP to find the intersection between S1 and S2.
#(vi) WAP to find the S1 - S2.

S1=set([10, 20, 30, 40, 50, 60])
S2= set([40, 50, 60, 70, 80, 90])
S1.add(55)
S1.add(66)
print("Set After Adding 55 and 66:", S1)
##############################################################################

S1=set([10, 20, 30, 40, 50, 60])
S2= set([40, 50, 60, 70, 80, 90])
S1.remove(10)
S1.remove(30)
print("Set After deleting 10 and 30:", S1)

###############################################################################
S1=set([10, 20, 30, 40, 50, 60])
S2= set([40, 50, 60, 70, 80, 90])
print("Is 40 present in S1:", 40 in S1)

###############################################################################

S1=set([10, 20, 30, 40, 50, 60])
S2= set([40, 50, 60, 70, 80, 90])
print ("Union of S1 and S2 ", S1.union(S2))

###############################################################################
S1=set([10, 20, 30, 40, 50, 60])
S2= set([40, 50, 60, 70, 80, 90])
print ("Intersection of S1 and S2 ", S1.intersection(S2))

###############################################################################
S1=set([10, 20, 30, 40, 50, 60])
S2= set([40, 50, 60, 70, 80, 90])
print ("Difference S1 - S2 ", S1.difference(S2))