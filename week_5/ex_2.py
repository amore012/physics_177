print "Welcome to Program"

#Import Libraries
import matplotlib
matplotlib.use('Agg')
import numpy as np
import math
import matplotlib.pyplot as plt

n = 1.
k = 1.
N = 1000.
xLength = np.linspace(0,1,num = N)
pi = np.pi
x_sin = xLength
y_sin = np.zeros(N)
x_square = xLength
y_square = np.zeros(N)
y_saw = np.zeros(N)
x_saw = xLength

def f_sin(n):
    return np.sin(pi*n/N)*np.sin(20*pi*n*N)
    
def f_square(k,n):
    return ((np.sin(2*pi*(2*k+1)*2*n))/(2*k+1))

def f_saw(k,n):
    return (np.sin(4*pi*k*n))/(k)

def coefficients(y):
    c = np.zeros(N//2+1,complex)
    for n in range(len(c)):
        for m in range(1000):
            c[n] += y[n]*np.exp(-2j*pi*n*m/N)
    return c

for n in range(len(y_sin)):
    y_sin[n] = f_sin(n)
    for k in range(1000):
        y_square[n] += (4/pi) * f_square(k,x_square[n])
        y_saw[n] += .5-(1/pi) * f_saw(k+1,x_saw[n])

c_sin = coefficients(y_sin)
c_square = coefficients(y_square)
c_saw = coefficients(y_saw)




plt.subplot(321)
plt.plot(x_sin,y_sin)
plt.subplot(322)
plt.plot(range(len(c_sin)),abs(c_sin)**2)

plt.subplot(323)
plt.plot(x_square, y_square)
plt.subplot(324)
plt.plot(range(len(c_square)),abs(c_square)**2)

plt.subplot(325)
plt.plot(x_saw, y_saw)
plt.subplot(326)
plt.plot(range(len(c_saw)),abs(c_saw)**2)

plt.savefig('Sin_Function.png')