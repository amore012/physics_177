print "Welcome to Program"

#Import Libraries
import matplotlib
matplotlib.use('Agg')
import numpy as np
import math as math
import matplotlib.pyplot as plt
import scipy
from scipy.integrate import simps

x = 0.
def f(x):
    return (math.sin((100*x)**(.5)))**2

comparedTo = 0.4558325
comparedTo = round(comparedTo, 6)
print comparedTo
result = 0.
n = 0
trapResult = 0.
n = n + 1
a = 0.
b = 0.
output = 0.
while output != comparedTo:
    for b in range(n):
        a += 1/n
        foxy = np.zeros(n)
        foxy[b] = f(a) 
    output = np.trapz(foxy, dx = 1/n)
    output = round(output, 6)
    error = abs(output-comparedTo/comparedTo)*100
    if output != comparedTo:
        print "Got %s, expected %s" %(output, comparedTo)
        print "Error is %s" %(error)
        n = n + 1