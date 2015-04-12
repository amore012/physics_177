import numpy as np
import math as math

v_o = 10
x_o = 800
g = -9.8 #m/s

#x = 1/2 acceleration * time^2 + v*t + initial_height
t = (-v_o - ((v_o ** 2) - 2 * g * x_o)**(.5))/g
t = round(t, 2)
print "It takes %s seconds when thrown with initial velocity %s m/s" % (t, v_o)