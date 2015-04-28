#Import Libraries
import matplotlib
matplotlib.use('Agg')
import numpy as np
import math as math
import matplotlib.pyplot as plt
import scipy
from scipy import constants
from numpy.linalg import solve


#==============================PART A==============================
system = np.array([[4.,-1.,-1.,-1.],
                   [-1.,+3.,0.,-1.],
                   [-1., 0.,3.,-1.],
                   [-1.,-1.,-1.,4.]]) #coefficients

result = np.array([5,0,5,0]) #in volts

#==============================PART B==============================
i=0
j=0
k=0

for i in range(len(result)): #Start a loop to solve the implied system of equations
    x = system[i][i]        #find each i-th diagonal element
    system[i][:] /= x
    result[i] /= x

#print system       #Test to make sure the vector is good



for j in range(len(result) - 1):
    mult = system[j][j]
    system /= mult
    print system
    
print system
 



#==============================PART C==============================
"""solution = solve(system,result)

for k in range(len(solution)):
    print "Across point %s, the voltage is %s Volts" %(k + 1, solution[k]) 
"""