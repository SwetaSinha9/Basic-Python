#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 14:10:03 2019

@author: sweta
"""
#LEARNING : How to use list, add, delete, search in list
#  List indexing starts from 0 to n-1
# L is a list defined as L= [11, 12, 13, 14].
#(i) WAP to add 50 and 60 to L. 
#(ii) WAP to remove 11 and 13 from L.
#(iii) WAP to sort L in ascending order.
#(iv) WAP to sort L in descending order.
#(v) WAP to search for 13 in L.
#(vi) WAP to count the number of elements present in L.
#(vii) WAP to sum all the elements in L.
#(viii) WAP to sum all ODD numbers in L.
#(ix) WAP to sum all EVEN numbers in L.
#(x) WAP to sum all PRIME numbers in L.
#(xi) WAP to clear all the elements in L.
#(xii) WAP to delete L.

L= [11, 12, 13, 14]
L.append(50) # to add element in a list we use append   
L.append(60)
print("List after adding:", L) 

##############################################################################  
L = [11, 12, 13,14]
del L[0] # to deleat element in a list we use del
del L[2]
print("List after deleting:", L)   

#Note : append is used to add elements in list. Only one argument can given at a time. del is used to delete elements from the list.    

###############################################################################
L= [11, 12, 13, 14]
L.sort()
print("List in accending order:", L)  

############################################################################### 
L= [11, 12, 13, 14]
L.sort(reverse=True)
print("List in decending order:",L)   
###############################################################################
  
L= [11, 12, 13, 14]
index= [11, 12, 13, 14].index(13)
print("The number 13 exist at index:", index)

#Note: If element exist in list then index function help us to find the location of element present in list. 
###############################################################################
  
L= [11, 12, 13, 14]
print ("Number of elements in list: ", len(L))
#Note: len function is used to find number of elements in a list 
###############################################################################
L= [11, 12, 13, 14]
print ("Sum of element in list  : ", sum(L))
###############################################################################
L= [11, 12, 13, 14]
s=0
for i in L:
    if i%2 !=0:
        s+=i
print ("Sum of odd numbers in a list: ", s)

###############################################################################

L= [11, 12, 13, 14]
s=0
for i in L:
    if i%2 ==0:
        s+=i
print ("Sum even numbers in a list: ", s)

###############################################################################
#Note: Find the sum of prime numbers by defining a function
def IsPrime(n):
	for i in range(2,int(n/2)+1):
		if n%i==0:
			return 0
	return 1
s=0
L=[11, 12, 13, 14]
for i in L:
    if IsPrime(i):
        s+=i
print("sum of prime numbers is:", s)

###############################################################################
L=[11, 12, 13, 14]
del L[0:4] #deletes elements indexing from 0 to 4
print("New list:", L)
###############################################################################
L=[11, 12, 13, 14]
del L #Completely deleat the list 
