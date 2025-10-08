# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 17:23:58 2018

@author: jfowl

x''(t) + 2x'(t) + x = 5e^-2t + t
with initial conditions:
    x(0) = 2
    x'(0) = 1

with analytic solution:
    x = -e^-t + 9te^-t + 5e^-2t + t - 2
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

nt = 1000
tstart = 0
tend = 20

tvec = np.linspace(tstart, tend, nt)


def analytic_sol(t):
    first = -np.exp(-t)
    second = 9*t*np.exp(-t)
    third = 5*np.exp(-2*t)
    fourth = t
    fifth = -2
    x = first + second + third + fourth + fifth
    return x


def analytic_sol_fun(t, a, b, c):
    first = -np.exp(-a*t)
    second = a*t*np.exp(-b*t)
    third = b*np.exp(-c*t)*np.sin(c*t)
    fourth = t
    fifth = -c
    sixth = -a*np.cos(b*t)
    x = first + second + third + fourth + fifth + sixth
    return x


plt.figure(1)
ax = plt.gca()
ax.set_facecolor((0, 0, 0))
for a in range(10, 20):
    for b in range(10, 20):
        for c in range(10, 20):
            tout = np.linspace(0, 1, 1000)
            vout = analytic_sol_fun(tout, a, b, c)
            plt.plot(tout, vout, 'g')
#            plt.xlim([min(tout), max(tout)])
#            plt.ylim([min(vout), max(vout)])
            plt.xticks([])
            plt.yticks([])
            plt.pause(0.005)


#def ode_model(X, t):
#    xdot1 = X[1]
#    xdot2 = -2*X[1] - X[0] + 5*np.exp(-2*t) + t
#    return [xdot1, xdot2]


#x0 = [2, 1]
#x = odeint(ode_model, x0, tvec)

#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.plot(tvec, [analytic_sol(t) for t in tvec], 'r', linewidth=5,
#        label='Analytic Solution')
#ax.plot(tvec, x[:, 0], '-.k', linewidth=2, label='Numerical Solution')
#plt.xlim([min(tvec), max(tvec)])
#plt.ylim([min(x[:, 0]), max(x[:, 0])])
#handles, labels = ax.get_legend_handles_labels()
#lgnd = ax.legend(handles, labels, loc='upper left',
#                 bbox_to_anchor=(0, 1))
#plt.xlabel('t-Value', fontsize=16)
#plt.ylabel('x-Value', fontsize=16)
#plt.title('Plot of x\'\'(t) + 2x\'(t) + x = 5e^-2t + t', fontsize=18)
#plt.grid(b=True, which='both')
#fig.savefig('ME426_HW3_21b', bbox_extra_artists=(lgnd,), bbox_inches='tight')
#plt.show()
