import numpy as np
import matplotlib.pyplot as plt
import pdb
from random import random

def f(x):
	return np.sin(1./(x*(2.-x)))**2

N = 10000
x= np.linspace(0.,2.,500)
plt.plot(x,f(x),'-',linewidth=3)

n = 0
for i in range(N):
	x = 2.*random()
	y = random()
	if y < f(x):
		n+= 1

integral = float(n) / float(N) * 2. 
print 'integral=',integral
pdb.set_trace()
