# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 17:22:25 2018

@author: jfowl

xdot + 7x = 5cos(2t)

Analytical Solution:
x = -35/53e^(-7t) + 35/53cos(2t) + 10/53sin(2t)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

nt = 1000
tstart = 0
tend = 20

tvec = np.linspace(tstart, tend, nt)


def analytic_sol(t):
    c1 = -35/53
    c2 = 35/53
    c3 = 10/53
    first = c1*np.exp(-7*t)
    second = c2*np.cos(2*t)
    third = c3*np.sin(2*t)
    x = first + second + third
    return x


def ode_model(x, t):
    c = 7
    c1 = 5
    c2 = 2
    dxdt = -c*x + c1*np.cos(c2*t)
    return dxdt


x0 = 0
x = odeint(ode_model, x0, tvec)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(tvec, [analytic_sol(t) for t in tvec], 'r', linewidth=5,
        label='Analytic Solution')
ax.plot(tvec, x, '-.k', linewidth=2, label='Numerical Solution')
plt.xlim([min(tvec), max(tvec)])
plt.ylim([min(x), max(x)])
handles, labels = ax.get_legend_handles_labels()
lgnd = ax.legend(handles, labels, loc='upper left',
                 bbox_to_anchor=(0.6, -0.05))
plt.xlabel('t-Value', fontsize=16)
plt.ylabel('x-Value', fontsize=16)
plt.title('Plot of x\'(t) + 7x(t) = 5cos(2t)', fontsize=18)
plt.grid(b=True, which='both')
fig.savefig('ME426_HW3_20a', bbox_extra_artists=(lgnd,), bbox_inches='tight')
plt.show()
