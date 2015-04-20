print "Welcome to Program"

#Import Libraries
import matplotlib
matplotlib.use('Agg')
import numpy as np
import math as math
import matplotlib.pyplot as plt
import scipy
from scipy.integrate import simps

##Define the function to be integrated
x = 0.
def f(x):
    return (math.sin((100*x)**(.5)))**2
print f(1.4)
##Define the variable to compare our value to (and calculate error)
expected = 0.4558325
expected = round(expected, 6)
#print comparedTo

#Define new variables to be used.
result = 0.
n = 1
i = 0 
trapResult = 0.
b = 0.
output = 0.
closeEnough = False

#To-do:
##Get values for function w/ N slices
##Calculate trap rule
##Calculate error
##If the function is right, break the loop
##Else, increase N and return to step one

while closeEnough == False:
    a = float(n)
    print "Using %s slices," %(n)
    values = np.zeros(n+1)
    for i in range(n):
        i = i + 1
        values[i] = f(i/a)
    #print "The values I am using are %s" %(values)
    output = np.trapz(values, dx = 1/a)
    print "from the Trapezoidal rule, I get %s" %(output)
    output = round(output, 6)
    error = (abs(output-expected)/expected)*100.
    if error < .00001:
        print "%s is close enough to %s, with an error of %s" %(output, expected, error)
        closeEnough = True
    else:
        print "Error was too great: %%%s" %(error)
        print ""
        n = n * 2