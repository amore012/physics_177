#Import Libraries
import matplotlib
matplotlib.use('Agg')
import numpy as np
import math as math
import matplotlib.pyplot as plt
import scipy
from scipy import constants

#Defining constants and useful variables
q = 1. #charge
pi = math.pi
q_1 = -1.
q_2 = 1.
x_1 = 45.
x_2 = 55.
r1 = 0.
r2 = 0.
e_o = scipy.constants.epsilon_0
q_1Field = np.zeros((100., 100.))
q_2Field = q_1Field
totalField = q_1Field
ePotential = q_2Field
location = q_2Field
x = 1.
y = 1.

for x in range(101):
    for y in range (101):
        y -= 50
        x -= 0
        r1 = ((x - x_1)**2 + y**2)**.5
        r2 = ((x - x_2)**2 + y**2)**.5
        if r1 != 0 and r2 != 0:    
            phi_1 = q_1/(4.*(r1) * pi * e_o)
            phi_2 = q_2 / (4*r2*pi*e_o)
            phi = phi_1 + phi_2
            phi = -phi
        #phi = phi + 50
        x += 0
        y += 50
        q_1Field[x - 1][y - 1] = phi
#print q_1Field
#totalField[:] = q_1Field[0][:]
#ePotential[:] = q_1Field[1][:]
#rint totalField
#print ePotential
yep = np.gradient(q_1Field)
#nope = np.gradient()

h = plt.quiver(yep, q_1Field);
plt.imshow(q_1Field,origin='lower')
plt.savefig('ex_1.png',format='png')