"""
Example to compute the discrete Fourier Transform coefficients
for two simple functions
Class: Apr. 28th
"""

import numpy as np
import matplotlib.pyplot as plt


def dft(y):
    N = len(y)
    c = np.zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*np.exp(-2j*np.pi*k*n/N)
    return c


x = np.linspace(0.,1.,20)
#y = np.ones(len(x))    #example for a function y(x) = constant
y = x                   #example for a function y(x) = x
y -= (np.sum(x)/float(len(x)))    #option to remove frequency "0" contribution

coeff = dft(y)
plt.plot(np.arange(len(coeff)),np.abs(coeff)**2,linewidth=3)
