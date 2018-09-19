# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 16:34:58 2018

@author: ryan-pc

Created By: Ryan Boldi
"""
import math
import matplotlib.pyplot as plt
import random

PI = math.pi
SQUARESIZE = 2
RADIUS = SQUARESIZE/2
SQUAREA = SQUARESIZE*SQUARESIZE
NEEDLESMAX = 100000

circleNeedles = 0


needleAmount = []
errorAmount = []


for i in range(0, NEEDLESMAX):
    #random.random returns 0 <= x < 1
    x = (random.random()*SQUARESIZE)-RADIUS #-1 <= x < 1
    y = (random.random()*SQUARESIZE)-RADIUS
    
    if (x**2 + y**2 < 1):   #1 for radius of 1 (root(1))
        circleNeedles += 1
        
    pi = (circleNeedles/NEEDLESMAX)*SQUAREA
    error = math.fabs(PI-pi)
    
    
    needleAmount.append(i)
    errorAmount.append(error)



plt.plot(needleAmount, errorAmount, ls = 'steps')
plt.show()