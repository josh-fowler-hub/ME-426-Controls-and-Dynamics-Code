# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 23:01:47 2018

@author: jfowl
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def analytic_sol_fun(t, a, b, c):
    x = a*np.sin(b*t) + a*np.cos(c*t)
    return x


plt.figure(1)
ax = plt.gca()
ax.set_facecolor((0, 0, 0))
for a in range(0, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            plt.clf()
            tout = np.linspace(-5, 5, 100)
            vout = analytic_sol_fun(tout, a, b, c)
            plt.plot(tout, vout)
#            plt.xlim([min(tout), max(tout)])
#            plt.ylim([min(vout), max(vout)])
            plt.xticks([])
            plt.yticks([])
            plt.pause(0.005)