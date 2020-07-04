import math
import matplotlib.pyplot as plt
from matplotlib import style
style.use('seaborn-ticks')
import random
import numpy as np

PI = math.pi
SQUARESIZE = 2
RADIUS = SQUARESIZE/2
SQUAREA = SQUARESIZE*SQUARESIZE
NEEDLESMAX = 100000

def randomThrows(SQUARESIZE, RADIUS, SQUAREA, NEEDLESMAX):
    
    circleNeedles = 0
    
    needleAmount = []
    errorAmount = []
    piValues = []
    
    for i in range(1, NEEDLESMAX+1):
        #random.random returns 0 <= x < 1
        x = (random.random()*SQUARESIZE)-RADIUS #-1 <= x < 1
        y = (random.random()*SQUARESIZE)-RADIUS
        
        if (x**2 + y**2 < 1):   #1 for radius of 1 (root(1))
            circleNeedles += 1
            
        pi = (circleNeedles/i)*SQUAREA
        error = math.fabs(PI-pi)
    
        needleAmount.append(i)
        errorAmount.append(error)
        piValues.append(pi)
    
    return needleAmount,errorAmount,piValues

#maybe if there was a mesh of needles dropped with a linear spacing, it would increase the accuracy
def meshThrows(SQUARESIZE, RADIUS, SQUAREA, NEEDLESMAX):
    circleNeedles = 0
    totalNeedles = 0
    
    needleAmount = []
    errorAmount = []
    piValues = []
    
    line = int(np.floor(np.sqrt(NEEDLESMAX)))
    vals = np.linspace(-1,1,line)
    
    for x in vals:
        for y in vals:
            totalNeedles+=1
            if (x**2 + y**2 < 1):   #1 for radius of 1 (root(1))
                circleNeedles += 1
            pi = (circleNeedles/totalNeedles)*SQUAREA
            error = math.fabs(PI-pi)

            needleAmount.append(totalNeedles)
            errorAmount.append(error)
            piValues.append(pi)
    
    return needleAmount, errorAmount, piValues

pivalue = 0
num = 1
for i in range (0,num):
        randomNeedle, randomError, randomPi = meshThrows(SQUARESIZE, RADIUS, SQUAREA, NEEDLESMAX)
        pivalue += randomPi[-1]
acPi = pivalue/num
#average pi values over 1000 simulations

plt.plot(randomNeedle, randomError, ls = 'steps')
plt.grid()
plt.xlabel("Number of needles dropped")
plt.ylabel("Error")
plt.show()

print("Average Value of pi ",  acPi)
