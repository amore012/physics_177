import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import pdb

# Number of sample points
N = 600
# sample spacing
T = 1. / 800.
x = np.linspace(0., N*T, N)
y = np.sin(50. * 2. * np.pi * x) + 0.5*np.sin(80. * 2.0*np.pi*x)

plt.figure(1)
plt.plot(x,y,'-r',linewidth=3)

### discretize sin(2.*pi*f*x) with f=1,100 and compute correlation
plt.figure(2)
dphi = np.pi / 100.

correl = np.zeros(shape=(100,100))   #rows are phase, columns are f
for f in range(100):
	for phi in range(100):
		phi_aux = float(phi) * dphi 
		g = np.sin(np.pi * 2. * float(f) * x + phi_aux)
		correl[phi,f] = np.dot(g,y)
	
plt.imshow(correl)
plt.colorbar()
plt.xlabel('frequency')
plt.ylabel('phase')


