import numpy as np
import matplotlib.pyplot as plt
import pdb
from math import *

def f(x):
	fout = np.ones(len(x[:,0]))  #how many rows = how many points i have
	ff = np.sqrt(np.sum(x**2,axis=1))
	aux = ff > 1.
	fout[aux] = 0.
	return fout


npoints = 1e7 #10000 
ndim =10 

# compute the multiplicative constant that depend on the number of dimensions
# Because integral goes from -1 to 1 in each dimension, then is a factor 2 for each dimension
c_dim = 2.**ndim 

x = np.empty(shape=(npoints,ndim))   #individual vectors should go like rows
for j in range(ndim):
	x[:,j] = np.random.rand(npoints)



y = f(x)
integral = c_dim / float(npoints) * np.sum(y)

print ''
print 'integral =',integral
print ''

#print 'expected value=',(np.pi)
expected = np.pi**(float(ndim)/2.) / gamma(float(ndim)/2.+1.)
print 'expected value=',expected
pdb.set_trace()
