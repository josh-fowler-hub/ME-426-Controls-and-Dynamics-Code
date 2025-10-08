# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 08:30:10 2018

@author: jfowl
"""

import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt


def Derivatives(z, t):
    Tdot = z[1]
    T = z[0]
    zeta = 1
    wn = 0.1
    T_inf = 72
    T_bake = 350
    threshold = 1
    if T < T_bake + threshold:
        Qdot = 300
    elif T > T_bake - threshold:
        Qdot = 0
    Tddot = -wn**2 * (T - T_inf) - 2*zeta*wn*Tdot + wn**2*Qdot
    zdot = np.asarray([Tdot, Tddot])
    return zdot


tout = np.linspace(0, 500, 10000)
zinitial = np.asarray([72, 0])
zout = integrate.odeint(Derivatives, zinitial, tout)

plt.figure()
plt.plot(tout, zout[:, 0])
plt.grid()
plt.show()
