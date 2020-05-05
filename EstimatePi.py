import math
#import matplotlib.pyplot as plt
#from matplotlib import style
#style.use('seaborn-ticks')
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
    
    needleAmount = []
    errorAmount = []
    piValues = []
    
    line = int(np.floor(np.sqrt(NEEDLESMAX)))
    print(line)
    vals = np.linspace(0,2,line)
    
    for i in range(1,len(vals)):
        for j in range(1, len(vals)):
            x = vals[i]
            y = vals[j]
            
            if (x**2 + y**2 < 1):   #1 for radius of 1 (root(1))
                circleNeedles += 1
            
            pi = (circleNeedles/((i*line)+j))*SQUAREA
            error = math.fabs(PI-pi)

            needleAmount.append((i*line)+j)
            errorAmount.append(error)
            piValues.append(pi)
    
    return needleAmount, errorAmount, piValues

pivalue = 0
num = 100
for i in range (0,num):
        randomNeedle, randomError, randomPi = randomThrows(SQUARESIZE, RADIUS, SQUAREA, NEEDLESMAX)
        pivalue += randomPi[-1]
acPi = pivalue/num
#average pi values over 1000 simulations

#plt.plot(randomNeedle, randomError, ls = 'steps')
#plt.grid()
#plt.xlabel("Number of needles dropped")
#plt.ylabel("Error")
#plt.show()

print("Best Value of pi ",  acPi)
