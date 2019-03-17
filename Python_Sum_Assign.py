#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 12:16:23 2019

@author: James Kimani

Python Summative Assignment

git@github.com:JKimanik/Python_Summative.git

"""
import random 

"""
Problem 1:
Generate a dummy dataset that you can use to prove your solutions work with.
ACCEPTANCE CRITERIA
i. The order of the objects must be sequential, ( ie. 1,2,3...32. ) since each number references a different pipeline region.
ii. Your generated dataset needs to return a single set of data, that has 32 entries, with each entry returning 16 floats. 
ii. The 16 floats returned will be between 0 and 1
"""
Clustereadings= []
Sensor_Reading = []
for Cluster in range(0,32):
    for sensors in range(0,16):
        Sensor_Reading.append(float('%.4f'%random.random()))
        Clustereadings.append(Sensor_Reading)
        Sensor_Reading = []
print(Clustereadings)




    
        