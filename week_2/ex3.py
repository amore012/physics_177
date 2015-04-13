"""
If you want multiple graphs on a sigle graph,
there is an ax=
"""
#Standard input library booklet
import matplotlib
matplotlib.use('Agg')
import numpy as np
import math as math
import matplotlib.pyplot as plt

constant = 22./5.


#Initial values to be recieved
plotPoints = 20
functionXValues = np.zeros(plotPoints)
functionYValues = functionXValues
pointsArray = np.zeros((plotPoints,2))

def f(x):
    return  x**4 - 2.*x + 1.

#Input values for the use in later calculations
for i in range(plotPoints):
    pointsArray[i][0] = i/10.
    pointsArray[i][1] = f(i/10.)
    

print pointsArray
#Using the trapezoidal rule1
trapIntegral = 0
midIntegral = 0

for j in range(plotPoints - 1):
    xbin = pointsArray[j + 1][0] - pointsArray[j][0]
    ybin = pointsArray[j + 1][1] + pointsArray[j][1]
    ymbin = (pointsArray[j + 1][1] + pointsArray[j][1])*.5
    #print xbin
    #print ybin
    midrule = xbin*ymbin
    trapRule = .5*xbin*ybin
    #print podobo
    trapIntegral = trapIntegral + trapRule
    midIntegral = midIntegral + midrule

simpsonRule = 2.*midIntegral+trapIntegral
simpsonRule = simpsonRule / 3.
    
print "By the trapezoidal rule, the area is %s." %(trapIntegral)
print "By Simpson\'s rule, the area is %s." %(simpsonRule)
    
