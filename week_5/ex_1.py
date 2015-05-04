print "Welcome to Program"

#Import Libraries
import matplotlib
matplotlib.use('Agg')
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy
from scipy.integrate import simps

##Define the function to be integrated
x = 0.
def f(x):
    return 924*x**6-2772*x**5+3150*x**4-1680*x**3+420*x**2-42*x+1

def f_prime(x):
    return 5544*x**5-13860*x**4+12600*x**3-5040*x**2+840*x-42

x1 = np.linspace(0,1,10000)
y = np.zeros(len(x1))
n = 0


for n in range(len(x1)):
    q = x1[n]
    y[n] = f(q)


x_min = 0
x_max = 1
initial = 0.0
guess = 0.1
for r in range(6):
    while abs(guess - initial) > 0.00005:
        initial = guess
        guess = guess - (f(guess) / f_prime(guess))
    print "Root %s is %s." %(r, round(guess,6))
    initial = guess
    guess = initial + .20



plt.plot(x1, y)
plt.plot([0,0],[0,0.5])
plt.savefig('Newton_Method.png')
