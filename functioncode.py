#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 09:41:32 2019

@author: sweta
"""
import math as m 
import random as r
def FitnessFunction(x):
    s=x[0]*x[0] +2*x[1]*x[1]-0.3*m.cos(3*m.pi*x[0])-0.4*m.cos(4*m.pi*x[1])+0.7
    return round(s,2)
C1=[10,40]
C2=[-20,30]
C3=[50,-90]
C4=[81,-81]
print("C1",FitnessFunction(C1))
print("C2",FitnessFunction(C2))
print("C3",FitnessFunction(C3))
print("C4",FitnessFunction(C4))
BestFitness=999999
BestChromosome=None
iterations=10000
for i in range(iterations):
    x=[]
    x.append(round(r.randint(-100,100)))
    x.append(round(r.randint(-100, 100)))
    fitness=FitnessFunction(x)
    if fitness<BestFitness:
        BestFitness=fitness
        BestChromosome=x
    if i%100 ==0:
        print(i,BestFitness, BestChromosome) 
print(BestFitness, BestChromosome)         
        
    
 