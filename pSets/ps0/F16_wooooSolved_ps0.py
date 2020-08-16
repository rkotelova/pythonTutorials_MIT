#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 07:58:10 2020

@author: rkotelova
"""


##
# PSET 0
##
# Ask the user to enter a number "x"
# Ask the user to enter a number "y"
# Prints out number "x", raised to the power "y"
# Prints out the log (base 2) of "x"
##

import numpy as np

print ("Enter a number for x:")
x = input()
print ("Enter a number for y:")
y = input()

print ("x+y =", int(x) + int(y))

print("x**y = ", int(x) ** int(y))
print("log(x) =", np.log2(int(x)))
