"""
Fit the data of our springs experiment to a straight line and later to a
cubic function (testing Terman's law). We later obtain "predictions" from these
models to points where we don't have data. We finish by removing the last points
from the data identifying that they belong to a different regime where the spring
doesn't behave like one but like a solid body (like a rope). 
"""

import numpy as np
import matplotlib.pyplot as plt
import pdb

g_const = 9.81   #kg m/s^2

filename = "Data/springData.txt"
data = np.loadtxt(filename)
dist = data[:,0]
mass = data[:,1]

x = mass * g_const   #force
plt.plot(x,dist,'ro') 
plt.xlabel('Force [Newton]')
plt.ylabel('extension [m]') 

coeff = np.polyfit(x,dist,1)
yfit = coeff[0]*x + coeff[1]
plt.plot(x,yfit,'b-',linewidth=3)

"""
## Terman's law --> cubic relation

coeff2 = np.polyfit(x,dist,3)
yfit = coeff2[0]*x**3 + coeff2[1]*x**2 + coeff2[2]*x + coeff2[3]
plt.plot(x,yfit,'g-',linewidth=3)

## ---- prediction for both models ---

mass = np.concatenate([mass,(1.1,1.2,1.3)])
x = mass * g_const   #force
yfit =  coeff[0]*x + coeff[1]
yfit2 = coeff2[0]*x**3 + coeff2[1]*x**2 + coeff2[2]*x + coeff2[3] 

plt.plot(x,yfit,'b-',linewidth=3)
plt.plot(x,yfit2,'g-',linewidth=3)
"""

mass = mass[0:-6]
dist = dist[0:-6]
x = mass * g_const   #force

coeff = np.polyfit(x,dist,1)
plt.figure(2)
plt.plot(x,dist,'ro')
plt.plot(x,coeff[0]*x+coeff[1],'-',color='magenta',linewidth=3)

pdb.set_trace()
