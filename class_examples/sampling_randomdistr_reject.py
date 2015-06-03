"""
Produce a sample of points distributed homogeneously within
a sphere of given density profile.
Method: Rejection sampling

This program does the same than sampling_randomdistr.py but changes
the sampling part to use rejection method instead of inverse transform
"""

import numpy as np
import matplotlib.pyplot as plt
import pdb
import math
from pylab import *
from scipy import *
import sys

#generate distribution within rmin, rmax and using nbin bins. 
rmin = 0.0   
rmax = 5.
nbin = 50

dr = (rmax - rmin) / float (nbin)
rbin = rmin + np.arange (nbin) * dr

alpha = -2.5    #slope of DENSITY profile, rho
rho = rbin ** alpha
beta = alpha + 3  # slope of mass profile
mass = rbin ** beta / rmax ** beta
mmax = np.max(mass)

fig1 = plt.figure (1)
ax1 = plt.subplot (111)
plt.plot (rbin, mass,'r-o')

nran = 10000

## --- here is the uniform sampling. Given a M(r), find the distribution of r that
##generates that M(r)
fig2 = plt.figure(2)

nin = 0
keep_r = np.empty(nran)
nstep = 0
while nin < nran:
	nstep += 1
	rnew = np.random.uniform(0,rmax)
	ynew = np.random.uniform(0,1.)
	m_new = rnew ** beta / rmax ** beta

	if ynew < m_new:
		keep_r[nin] = rnew
		nin += 1

print "number of total steps",nstep
nbins = 20
n, bins, patches = hist (keep_r, nbins)
plt.xlabel('r [kpc]',fontsize=15)
plt.ylabel('Number',fontsize=15)

## -----
rho_ = np.zeros (nbins)
for i in range (nbins):
	rho_[i] = n[i] / ((bins[i + 1]**3 - bins[i]**3)*bins[i+1])

bins = bins[0 : nbins] + 0.5 * (bins[1] - bins[0])

xx = np.log (bins)
yy = np.log (rho_)

# plot density profile from generated sample
fig = plt.figure(3)
plt.plot(xx,yy,'ro',markersize=13)
plt.xlabel('log(r)',fontsize=15)
plt.ylabel(r'log($\rho$)',fontsize=15)

# fit obtained density profile and plot fit
coeff = np.polyfit(xx,yy,1) 
print 'coefficient from fit=', (coeff[0], alpha)

yy2 = xx*coeff[0] + coeff[1]
plt.plot(xx,yy2,'-b',linewidth=3)

pdb.set_trace()
