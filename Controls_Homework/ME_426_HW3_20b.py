# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 17:23:16 2018

@author: jfowl

xdbldot + 6xdot + 8x = 5sin(3t)

with analytic solution:
    x = 9/65e^-2t + 9/65e^-4t - 1/65sin(3t) - 18/65cos(3t)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

nt = 1000
tstart = 0
tend = 20

tvec = np.linspace(tstart, tend, nt)


def analytic_sol(t):
    c = 75/130
    c1 = -39/130
    c2 = -2/130
    c3 = -36/130
    first = c*np.exp(-2*t) + c1*np.exp(-4*t)
    second = c2*np.sin(3*t)
    third = c3*np.cos(3*t)
    x = first + second + third
    return x


def ode_model(X, t):
    xdot1 = X[1]
    xdot2 = -6*X[1] - 8*X[0] + 5*np.sin(3*t)
    return [xdot1, xdot2]


x0 = [0, 0]
x = odeint(ode_model, x0, tvec)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(tvec, [analytic_sol(t) for t in tvec], 'r', linewidth=5,
        label='Analytic Solution')
ax.plot(tvec, x[:, 0], '-.k', linewidth=2, label='Numerical Solution')
plt.xlim([min(tvec), max(tvec)])
plt.ylim([min(x[:, 0]), max(x[:, 0])])
handles, labels = ax.get_legend_handles_labels()
lgnd = ax.legend(handles, labels, loc='upper left',
                 bbox_to_anchor=(0.6, -0.05))
plt.xlabel('t-Value', fontsize=16)
plt.ylabel('x-Value', fontsize=16)
plt.title('Plot of x\'\'(t) + 6x\'(t) + 8x(t) = 5sin(3t)', fontsize=18)
plt.grid(b=True, which='both')
fig.savefig('ME426_HW3_20b', bbox_extra_artists=(lgnd,), bbox_inches='tight')
plt.show()
