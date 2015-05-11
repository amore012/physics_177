print "Welcome to Program"

#Import Libraries
import matplotlib
matplotlib.use('Agg')
import numpy as np
import math
import matplotlib.pyplot as plt

#Space reserved for defining variables

#Import data from sunspots.txt
retrieve = open('extra_info_labs/sunspots.txt', 'r')
data = np.loadtxt(retrieve)

#Seperate out the data so that it is useful
month = data[:,0]
spotNumber = data[:,1]

#Make a graph of the sunspots as a function of time
plt.plot(month, spotNumber)
plt.xlabel('Months')
plt.ylabel('Number of Sunspots')
plt.title('Sunspot Periodicity')
plt.savefig('week_5/ex_3_out.png')
#From looking at the graph, I assume a periodicity
#of about 100 months



#Using the same function as the previous example
def coefficients(y):
    N = len(month)
    c = np.zeros(N//2+1,complex)
    for n in range(len(c)):
        for m in range(1000):
            c[n] += y[n]*np.exp(-2j*np.pi*n*m/N)
    return c



#Calculate the coefficients, and plot them
spotFunction = coefficients(spotNumber)
print spotFunction
x = np.linspace(0,10,len(spotFunction))
plt.plot(x ,np.abs(spotFunction)**2)
plt.savefig('week_5/ex_3_out_2.png')
