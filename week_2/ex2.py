fromFile = open('extra_info_labs/velocities.txt', 'r')

#Standard input library booklet
import matplotlib
matplotlib.use('Agg')
import numpy as np
import math as math
import matplotlib.pyplot as plt

#Initial values to be recieved
#functionXValues = np.zeros(plotPoints)
#functionYValues = functionXValues
pointsArray = np.zeros((100,2))
solutionsArray = pointsArray

#Input values for the use in later calculations

pointsArray = np.loadtxt(fromFile, delimiter='\t', unpack=True)


#print pointsArray
#Using the trapezoidal rule1
trapIntegral = 0
midIntegral = 0

for j in range(199):
    xbin = 1
    ybin = pointsArray[j + 1][1] + pointsArray[j][1]
    ymbin = (pointsArray[j + 1][1] + pointsArray[j][1])*.5
    #print xbin
    #print ybin
    midrule = xbin*ymbin
    trapRule = .5*xbin*ybin
    #print podobo
    trapIntegral = trapIntegral + trapRule
    midIntegral = midIntegral + midrule
    solutionsArray[j+1][0] = pointsArray[0][2*j-1]
    solutionsArray[j+1][1] = pointsArray
    simpsonRule = 2.*midIntegral+trapIntegral
    simpsonRule = simpsonRule / 3.
    
header = ['Time','Trap Dist', 'Simpson Dist']


np.savetxt('Velocities.txt', simpsonRule, header='These are the students grades', footer='That is all')

print "By the trapezoidal rule, the area is %s." %(trapIntegral)
print "By Simpson\'s rule, the area is %s." %(simpsonRule)
    
