"""
This routine shows an application of the Central Limit Theorem: 
when adding a large number of random numbers, the result is a normal-distribution
regardless the shape of the initial PDF from where we draw the numbers. 
#
Below, we compute each individual error as the sum of 100 uncorrelated
errors draw from a given PDF (triangular, uniform, normal) and then assume
that our data consist of 10000 measurements. What shape do we expect for the
distribution of our errors? 
"""

import numpy as np
import matplotlib.pyplot as plt
import pdb

ntrials = 10000   #all errors 
npts = 100    #individual error is composed of 100 small random errors

keep_err = np.zeros(ntrials)
for i in range(ntrials):
	s = 0.
	for j in range(npts):
		s += np.random.triangular(-1.,0.,1.)   #left, mode, right
	keep_err[i] = s
	#keep_err[i] = np.sum(np.random.triangular(-1.,0.,1.,size=npts))

plt.hist(keep_err,bins=50,alpha=0.9,color='blue')
plt.xlabel('Sum of individual errors')
plt.ylabel('Number of trials')
plt.title('Sum of 100 random points -- Triangular PDF 10000 trials')

## uniform distribution ##
keep_err[:] = 0.
for i in range(ntrials):
	xx = 2.*np.random.rand(npts) - 1.
	keep_err[i] = np.sum(xx)	
plt.hist(keep_err,bins=50,alpha=0.5,color='green')

## normal distribution ##
keep_err[:] = 0.
for i in range(ntrials):
	xx = np.random.normal(0.,1.,size=npts)    #mean, sigma, shape
	keep_err[i] = np.sum(xx)	
plt.hist(keep_err,bins=50,alpha=0.2,color='magenta')

