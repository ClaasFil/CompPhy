import math
import numpy as np
import math
import matplotlib.pyplot as plt


def dv(om0, th0, t0, g, l, q, fd, dr, linear):
    dth = om0
    if(linear):
        dom = -g/l*(th0)-q*om0+fd*np.sin(dr*t0)
        #
    else:
        dom = -g / l * np.sin(th0) - q * om0 + fd * sin(dr * t0)
    return dth, dom


        # Fixed Params
th = []
t = [0]
pi = 4 * math.atan(1)
g = 9.8
nmax = 50000


        #set Params
method = 3
linear = 2
rescale = 0
th0 = [0]
om = [10]
l = g
dt = 0.004       #time stamp (T
q = 0           #damping const
fd = g/100          #force amp (A0)
dr = 0.2          #force frequency (Td)

th.append(th0[0]*pi/180)
print("initial angle (in rad) = "+ str(th[0]))

period = 6.2831853/np.sqrt(g/l)

for i in range(1, nmax):
    t.append(t[i - 1] + dt)
    if(method == 1):
        dth, dom = dv(om[i-1],th[i-1],t[i-1],g,l,q,fd,dr,linear)
        om.append(om[i - 1] + dt * dom)
        th.append(th[i - 1] + dt * dth)
    if (method == 2):
        dth, dom = dv(om[i - 1], th[i - 1], t[i - 1], g, l, q, fd, dr, linear)
        om.append(om[i - 1] + dt * dom)
        th.append(th[i - 1] + dt * om[i])
    if(method == 3):
        dth, dom = dv(om[i - 1], th[i - 1], t[i - 1], g, l, q, fd, dr, linear)
        om1 = (om[i - 1] + dt/2 * dom)
        th1 = (th[i - 1] + dt/2 * dth)
        t1 = t[i - 1] + 0.5 * dt
        dth2, dom2 = dv(om1, th1, t1, g, l, q, fd, dr, linear)
        om.append(om[i - 1] + dt * dom2)
        th.append(th[i - 1] + dt * dth2)

if (rescale):
    for i in range(0, len(th)):
        th[i] = math.degrees(th[i]-2.0*pi*round(th[i]/(2.0*pi)))

                #plot
plt.figure(figsize=(6.5, 4))
plt.plot(t,th,  label='data')
plt.legend(loc='lower left', ncol=2)
plt.show()












