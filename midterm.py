#Import Libraries
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt


#matplotlib.pyplot ('Agg')
#Declare variables
t = 0.
n = 0
x = np.zeros(50)
y = np.zeros(50)
average = 0.0
trap_result = 0.0

#Define the function
def v(a):
    return 100.*(np.sin(2.*np.pi*a) * a**2)

#Get the values to plot
for n in range(50):
    #n = float(n)
    t = n/50.
    x[n] = t
    y[n] = v(t)
    average += v(t)
 
    
#Make a plot
plt.plot(x,y,'ro')
plt.savefig('midterm.png')


#write a file
#np.savetxt(fname = 'sampled_velocities.dat')
#print to screen the average velocity

#Print Average velocity to terminal
print "Average velocity is %s m/s" %(abs(average/50))

#Trapezoidal Rule
n = 0
for n in range(49):
    dx = 1./50.
    trap_result += (.5 * (y[n+1] + y[n])*dx)
print "My Trapezoidal rule gives %s." %(trap_result)
print "Theirs gives %s" %(np.trapz(y, dx =1./50.))