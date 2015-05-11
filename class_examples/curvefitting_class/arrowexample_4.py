"""
This programs reads in data from an experiment of an arrow thrown at 
a target. The experiments measure distance from target and height above
the ground for the arrow (i.e. trayectory). It fits a linear and a quadratic
equation and estimates the goodness of these fits through the "coeff. of determination"
or R^2 parameter. 
"""

import numpy as np
import matplotlib.pyplot as plt
import pdb


def err(y,yfit):
	return np.sum((y-yfit)**2)

g_const = 9.81   #kg m/s^2

filename = "Data/launcherData.txt"
data = np.loadtxt(filename)
dist = data[:,0]
h1 = data[:,1]
h2 = data[:,2]
h3 = data[:,3]
h4 = data[:,4]

dist *= 36.   #now is in feet

plt.plot(dist,h1,'ro') 
plt.plot(dist,h2,'bo') 
plt.plot(dist,h3,'go') 
plt.plot(dist,h4,'mo') 
plt.xlabel('D [ft]')
plt.ylabel('Height [ins]') 

### ---
## mean at each distance 
mh = np.zeros(len(dist))
for i in range(len(dist)):
	mh[i] = (h1[i] + h2[i] + h3[i] + h4[i]) / 4.
	
### ---
#create a single array with all measurements -- compare with fit from mean mh
mega_dist = np.concatenate([dist,dist,dist,dist])
mega_h = np.concatenate([h1,h2,h3,h4])

## ----
coeff0 = np.polyfit(dist,mh,1)
coeff1 = np.polyfit(dist,mh,2)
coeff2 = np.polyfit(mega_dist,mega_h,2)
## you can check that using all points (mega_h) and using 
## the mean at each point (mh) gives the same fit!

x = dist    #original "sampling
#x = np.linspace(0.,1100,1000)   #make it smoother
yfit0 = coeff0[0]*x + coeff0[1]
yfit1 = coeff1[0]*x**2 + coeff1[1]*x + coeff1[2]

## -----
ave = np.sum(mh)/float(len(mh))
err_data = np.sum((mh - ave)**2)
err_lin = err(mh,yfit0)
err_qua = err(mh,yfit1)

# -- compute coeff. of determination for goodness of fit
r2_lin = (1. - err_lin/err_data)
r2_qua = (1. - err_qua/err_data)

print 'R**2 linear=',(1. - err_lin/err_data)
print 'R**2 quad=',(1. - err_qua/err_data)


plt.plot(x,yfit0,'g-',linewidth=3)
plt.plot(x,yfit1,'b-',linewidth=3)

text = 'R2 linear=' + str(round(r2_lin,4))
plt.text(50,22,text,color='green',fontsize=12)
text = 'R2 linear=' + str(round(r2_qua,4))
plt.text(50,19,text,color='blue',fontsize=12)
pdb.set_trace()
