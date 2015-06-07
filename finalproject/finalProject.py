"""
==============================================================================
==============  AARON MOREFIELD'S FINAL PROJECT: PHYSICS 177  ================
==============================================================================

From the paper: How supernova feedback turns dark matter cusps into cores

Purpose: To confirm the calculations of the paper written by A. Pontzen and
         F. Governato
"""

#================Section I & II: Abstract/Intro======================
"""
In summary:
- Obserbed kinematics point to a constant density core
- Simulations suggest that the CDM density should be increasing with
  density proportional to the radii
- Might also be violent baryonic processes
- Processes classified as Supernova Driven Flattening and dynamical friction
- From "Read & Gilmore(2005)", It was shown that many moderately violent bursts
  could be effective in creating a core
- Simulations from five years ago resolve individual star formation clumps
- That paper was in excellent agreement with the Cusp flattening idea
"""

#================Section III: Calculations==========================
"""
The calculations aim to make confirm the cusp flattening idea with energy arguments
The Calculations are based off of the following assumptions
(1) The potential is assumed to be spherically symmetric;
(2) The tracer particles are assumed to be massless,
    i.e. the potential is always external.
(3) The functional form of the potential is fixed
(4) The functional form is also a power law
"""

#--------Import libraries-------
import matplotlib
matplotlib.use('Agg')
import astropy
import numpy as np
import math as math
import matplotlib.pyplot as plt
import scipy
import scipy.signal as sp

#-----------------------Declare Variables-----------------------

t = 300        #Time [mYr]

v_o = 0.        #Initial potential

n = 2.          #Powers which determine orbit type; n == -1 would, for
                #example, describe a Keplerian orbit [integer]

i = 1

amp = 1

r = 10.          #Radial distance between particles [kPc]

j = 1.          #Conserved angular momentum

e_o = 1.        #The initial energy

del_e_1 = 1.    #Change in energy

del_v = 1.      #Change in potential

del_v_o = 5.    #Change in initial potential energy

a = 1.          #Amplitude coefficient

a_o = 1.        #Initial amplitude at each step

phi_0 = 0.      #Initial orbital phase

omega_1 = 1.    #The initial frequency

omega_0 = 10.  #The progressing frequency

afp = np.linspace(0,10,t) #The number of points the program should plot

#--------------------Define Arrays for Output-------------------

e_out = np.zeros(t)   #To output the energy as a function of time

v_out = np.zeros(t)   #To output the potential as a funciton of time

x_out = np.zeros(t*3)   #To output the position as a function of time


#--------------------Define Functions--------------------------

#Expected potential energy
def expectedPotential(e_o,n):
    v_exp = 2*e_o/(2+n) 
    return v_exp

#The time dependent physical potential
v = v_o * r

#The 1-D approximation of the orbit
v_eff = v + j**2 / (2*r**2)  

#Final energy assuming adiabatic change (intermediate step)
#e_f_a = e_o *((v_f/v_o)**(2/(2+n)))

#Determining the amplitude after each step
def stepAmplitude(a_o, omega_0, omega_1, m):
    a_1 = ((a_o**2) * (1 + ((omega_0**2 - omega_1**2)/(omega_0**2))*(np.sin(m*phi_0))**2))**.5
    return a_1

#Final energy function to be iterated recursively
def finalEnergy(e_o, del_v_o, del_v):
    e_f_t = e_o + ((del_v_o/del_v)**2) * (2 * n * e_o)/((2+n)**2)
    return e_f_t


#For the orbit, when n == 2, it becomes identical to a harmonic
#oscillator. Thus it can be analyzed as follows:
def orbitalOscillation(q, v_o, t, phi_0):
    x = a*np.cos(((2*v_o)**.5)*t + phi_0)
    return x


#=============Calculating The Final Energy Recursively=============
for i in range(4):
    if i == 2:
        amp = 2
    else:
        amp = 1
    
    if i == 1:
        omega_1 = omega_0
    elif i == 2:
        omega_1 = 2 * omega_0
    elif i == 3:
        omega_1 = omega_1    
    
    for m in range(t):

        #At each of the three steps, the energy exerted changes as a function of the previous
        z = finalEnergy(e_o, del_v_o, del_v)
        e_out[m] = z
        
        #Since the energy has changed, so too has the potential
        del_v_o = del_v
        v_o = expectedPotential(e_o, n)
        del_v = del_v_o - v_o + 1
        v_out[m] = v_o
        
        #The Amplitude for the oscillations then adjusts for the x value
        a = stepAmplitude(a_o, omega_0, omega_1, m)
        
        #With all this information, the x value is given, and the process repeats
        y = orbitalOscillation(a, v_o, afp[m]*i, phi_0)
        
        if i == 2:
            y = y * 2

        x_out[m*i] = y
        #print v_out
    

#-------Printing and output------------
plt.plot(x_out)
plt.title('Displacement of particles as a function of time')
plt.ylabel('Displacement [kPc]')
plt.xlabel('Time[Rel]')
plt.savefig('finalproject/timeOutput.png')
plt.show

#On the Plot, The periods of drastic change in oscilation correlate to the
#theorized energy release periods of the paper.

#===================References and Citations=======================
"""
A. Pontzen and F. Governato. How supernova feedback turns dark matter cusps into cores
F. Governato. At the heart of the matter: the origin of bulgeless dwarf galaxies and Dark Matter cores
Philip F. Hopkins. A New Class of Accurate, Mesh-Free Hydrodynamic Simulation Methods
"""