"""
Exercise 10.8
Application example of importance sampling to integrate f(x) = x^-1/2 / (e^x + 1).
Choose weight function w(x) = x^-1/2
"""
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import pdb

# define number of random samples to use
npoints = 1000000

## --- STEP 1: Choose weight function w(x) ---
# this step is done by the book, w(x) = x^-0.5

## define the function to integrate, this one is f(xi)/w(xi), i.e. the function without the singularity
def g(x):
	return (1./(np.exp(x) + 1.))    


## ---- STEP 2: -------------------
#draw random numbers from the distribution given by p(x) = w(x)/int(w(x))_valuated in 0-1.
# The cummulative distribution for that is int[ p(x) dx] = x^0.5, and is also normalized.
#Then, we draw y random numbers between 0 and 1 and invert the cummulative distribution function
#to find the x that satisfy the inverse equation. Keeps those x values.

y = np.random.rand(npoints)
x_sample = y**2

## plot distribution wanted ##
fig1 = plt.figure(1)
xx = np.linspace(0.,1,50)
plt.plot(xx,xx**(0.5),'ro')
plt.xlabel('x', fontsize=15)
plt.ylabel('Cumulative PDF',fontsize=15)

## plot distribution generated
fig2 = plt.figure(2)
nbins = 20
n, bins, patches = hist (x_sample, nbins)
plt.xlabel('x',fontsize=15)
plt.ylabel('Number',fontsize=15)

### --test cumulative(distribution generated) = distribution wanted
#fig1 = plt.figure(1)
#bins1 = bins[0 : nbins] + 0.5 * (bins[1] - bins[0])
#plt.plot(bins1,np.cumsum(n)/float(npoints), '-s',color='green')
### seems to work fine!



### ------ STEP 3 ------------
## compute integral
g_xi = g(x_sample)
integral = 1./float(npoints) * np.sum(g_xi) * 2.    #2 = int(w(x))_between(0,1)

print ''
print 'integral= ',integral
print ''




pdb.set_trace()
