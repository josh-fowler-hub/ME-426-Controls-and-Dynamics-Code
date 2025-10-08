# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 08:33:15 2018

@author: jfowl
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as scI


def Derivatives(z, t):
    global w1, w2
    J = 0.00367319330305115
    kt = 0.0335291245362469
    w0 = 800
    d = 0.7283465
    phi = z[0]
    phid = z[1]
    phi_c = 2*np.pi*3
    e = phi - phi_c
    kp = -80
    dw = kp*e
    phid_c = 0
    edot = phid - phid_c
    kd = -100
    dw = kp*e + kd*edot
    w1 = w0 + dw
    w2 = w0 - dw
    if w1 > 1250:
        w1 = 1250
    if w2 > 1250:
        w2 = 1250
    if w1 < 0:
        w1 = 0
    if w2 < 0:
        w2 = 0
    T1 = kt*w1**2
    T2 = kt*w2**2
    phidd = T1*d - T2*d
    return [phid, phidd]


tout = np.linspace(0, 10, 1000)
zinitial = [0, 0]
zout = scI.odeint(Derivatives, zinitial, tout)

w1out = 0*tout
w2out = 0*tout
for idx in range(len(tout)):
    Derivatives(zout[idx, :], tout[idx])
    w1out[idx] = w1
    w2out[idx] = w2


plt.figure()
plt.plot(tout, zout)
plt.title('Angle, Rate vs. Time')
plt.xlabel('Time')
plt.ylabel('Angle, Rate')
plt.grid()
plt.show()

plt.figure()
plt.plot(tout, w1out)
plt.plot(tout, w2out)
plt.show()
