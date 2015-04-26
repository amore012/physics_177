import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt


def f(r):
	g = 6.674e-11  #m^3/(kg * s^2)
	M = 5.974e24   #kg
	m = 7.348e22   #kg
	R = 3.844e8    #m
	w = 2.662e-6   #s^-1
	return g*M/r**2 - g*m/(R-r)**2 - w**2*r

def f_prim(r):
	g = 6.674e-11  #m^3/(kg * s^2)
	M = 5.974e24   #kg
	m = 7.348e22   #kg
	R = 3.844e8    #m
	w = 2.662e-6   #s^-1
	return -2.*g*M/r**3 - 2. * g*m/(R-r)**3 - w**2



g = 6.674e-11  #m^3/(kg * s^2)
M = 5.974e24   #kg
m = 7.348e22   #kg
R = 3.844e8    #m
w = 2.662e-6   #s^-1

# our own Newton's method
# x_new = x - f(x)/f'(x)

x_old = R/2.
i = 0
eps = 1.

while eps > 1.e-4:
	x = x_old - f(x_old)/f_prim(x_old)
	print 'x new=', (x/1000.)
	eps = abs(x_old - x)
	x_old = x
	i +=1

print 'solution with our method (in km)= ',(x/1000.)   
print 'number of steps=',i


## ---------------------------------------------
# with scipy
x0 = R /2.
#sol = opt.newton(f, x0, fprime=f_prim, tol=1.e-04, maxiter=50)
sol = opt.newton(f, x0, tol=1.e-04, maxiter=50)   #we can also call it without knowing the derivative


print 'sol=',(sol/1.e3)   #distance in km

## --- plot function ---

x = np.linspace(6.e6,2.*R,250)
y = f(x)


ax = plt.subplot(111)
plt.plot(x,y,'r',linewidth=3)
ax.set_xscale('log')
xx=([R,R])
yy=([-2.,10.])
plt.plot(xx,yy,'--')
plt.xlabel('r [m]')
plt.ylabel('f(r)')

