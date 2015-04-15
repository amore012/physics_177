"""
Example of solution for Problem 2, Lab 2
"""

import numpy as np
import matplotlib.pylab as plt

#read data from file
filein = 'velocities.txt'
data = np.loadtxt(filein)
t = data[:,0]
v = data[:,1]

xfinal = np.trapz(v,x=t)
print 'final position= ',xfinal

## position as a function of time

pos = np.zeros(len(t))
dist = np.zeros(len(t))

pos[0] = 0.
dist[0] = 0.
for i in range(1,len(t)):
	x1 = np.trapz(v[0:i], x=t[0:i])
	x2 = np.trapz(np.abs(v[0:i]), x=t[0:i])
	pos[i] = x1
	dist[i] = x2

ax1 = plt.subplot(3,1,1)
plt.plot(t,v)
plt.ylabel('V [m/s]')
ax2 = plt.subplot(3,1,2)
plt.plot(t,pos)
plt.ylabel('Pos [m]')
ax2 = plt.subplot(3,1,3)
plt.plot(t,dist)
plt.ylabel('Distance [m]')
plt.xlabel('time [s]')

