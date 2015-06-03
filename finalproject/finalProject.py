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

t = 2000        #Time [mYr]

v_o = 1.        #Initial potential

n = 2.          #Powers which determine orbit type; n == -1 would, for
                #example, describe a Keplerian orbit [integer]

r = 1.          #Radial distance between particles [kPc]

j = 1.          #Conserved angular momentum

e_o = 1.        #The initial energy

del_e_1 = 1.    #Change in energy

del_v = 1.      #Change in potential

del_v_o = 1.    #Change in initial potential energy

a = 0.          #Amplitude coefficient

a_o = 1.        #Initial amplitude at each step

phi_0 = 0.      #Initial orbital phase

omega_1 = 10.    #The initial frequency

omega_0 = 10.*omega_1   #The progressing frequency

#--------------------Define Arrays for Output-------------------

e_out = np.zeros(t)   #To output the energy as a function of time

v_out = np.zeros(t)   #To output the potential as a funciton of time

x_out = np.zeros(t)   #To output the position as a function of time


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
def stepAmplitude(a_o):
    a_1 = ((a_o**2) * (1 + ((omega_0**2 - omega_1**2)/(omega_0**2))*(np.sin(phi_0))**2))**.5
    return a_1

#Final energy function to be iterated recursively
def finalEnergy(e_o):
    e_f_t = e_o + ((del_v_o/del_v)**2) * (2 * n * e_o)/((2+n)**2)
    return e_f_t


#For the orbit, when n == 2, it becomes identical to a harmonic
#oscillator. Thus it can be analyzed as follows:
def orbitalOscillation(a, v_o, t):
    x = a*np.cos(((2*v_o)**.5)*t + phi_0)
    return x


#=============Calculating The Final Energy Recursively=============
for n in range(t):
    #At each step, the energy exerted changes as a function of the previous
    e_o = finalEnergy(e_o)
    e_out[n] = e_o
    
    #Since the energy has changed, so too has the potential
    v_o = expectedPotential(e_o, n)
    v_out[n] = v_o
    
    #The Amplitude for the oscillations then adjusts for the x value
    a_o = stepAmplitude(a_o)
    
    #With all this information, the x value is given, and the process repeats
    x = orbitalOscillation(a_o, v_o, n)
    x_out[n] = x
    #print v_out
    

#-------Printing and output------------
plt.plot(range(t), x_out)
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