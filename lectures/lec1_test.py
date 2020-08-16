#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 21:09:37 2020

@author: rkotelova
"""

pi = 3.14159
radius = 2.2

pi_approx = 22/7

area = pi * (radius**2)
print(area)

radius = radius+1
area = pi * (radius**2)
print(area)

diameter = 2.2
circ = pi * diameter
print(circ)

circ = round(circ, 1)
print(circ)

type(5)
print(3.0-1)


usa_gold = 46
uk_gold = 27
romania_gold = 1
    
total_gold = usa_gold + uk_gold + romania_gold
print(total_gold)
    
romania_gold += 1
print(total_gold)
