import matplotlib
matplotlib.use('Agg')
import numpy as np
import math as math
import matplotlib.pyplot as plt

print "Welcome to Example Three Part B."
print ""
print "Here you will be calculating the times it would take"
print "for a ball to hit the ground thrown off of a roof of"
print "some height. The positive direction is opposite gravity"
print ""

VelocityBin = np.zeros(10)
VelocityStep = np.zeros(10)

#Discrete values is the reason one might place bins
#Each value should show the individual time that the ball takes

vmin = float(raw_input ("Please enter a minimum velocity (m/s): "))
vmax = float(raw_input ("Please enter a maximum velocity (m/s): "))
x_init = float(raw_input ("Please enter an initial height (m): "))
g = -9.8 #m/s

dv = (vmax-vmin)/10 #This outlines the bin-step value,

print "The discrete step is %s" %(dv)

#x = 1/2 acceleration * time^2 + v*t + initial_height
#Using the quadratic formula above on the above

for i in range(len(VelocityBin)):
    v_o = vmin + i * dv
    VelocityStep[i] = v_o
    time = (-v_o - ((v_o ** 2) - 2 * g * x_init)**(.5))/g
    time = round(time, 2)
    #print "For v_o %s, the time will be %s" % (v_o, time)
    VelocityBin[i] = time
    
print VelocityBin
np.savetxt('VelocityBin.txt', VelocityBin, header='These are the students grades', footer='That is all')
#For plt.axis ([-1,1,Vmin,vmax)] corresponds to xmin,
#xmax, ymin, ymax
from numpy.random import rand

x = VelocityBin
y = VelocityStep
plt.scatter(x, y, c='red', label='Steps', alpha=1, edgecolors='none')
plt.xlabel('Time (s)')
plt.ylabel('Initial Velocity (m/s)')
plt.legend()
plt.grid(True)

plt.show()
plt.savefig('Example3Out.png')
"""
Notes
"""