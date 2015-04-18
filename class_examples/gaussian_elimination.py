"""
Example of Gaussian Elimination + Backsubstitution to solve a linear system of equations.
Class Apr. 16th. 
"""
import numpy as np
from numpy.linalg import solve
import pdb

# Define input arrays
A = np.array([[2,1,4,1],[3,4,-1,-1],[1,-4,1,5],[2,-2,1,3]],float)
v = np.array([-4,3,9,7], float)

N = len(v)

# start Gassian elimination
# for-loop in m-th column
for m in range(N):
	val = A[m,m]
	A[m,:] /= val
	v[m] /= val

# for-loop in m+1, N columns
	for i in range(m+1,N):
		mult = A[i,m]
		A[i,:] -= mult * A[m,:]
		v[i] -= v[m] * mult

# At this point A is an upper-triangle matrix, with 1 in the diagonal
#######
# Start Backsubstitution
x = np.array([0.,0.,0.,0.],float)
for m in range(N-1,-1,-1):
	x[m] = v[m]
	for i in range(m+1,N):
		x[m] -= A[m,i] * x[i]
	

#print result
print 'x=',x

#### Solve with numpy intrinsic function and compare:
x_np = solve(A,v)
print 'x numpy=',x_np


#########

