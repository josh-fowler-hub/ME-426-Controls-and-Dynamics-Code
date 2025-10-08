# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 17:23:37 2018

@author: jfowl

x''(t) + 2x'(t) + 2x = sin(2t)
with initial conditions:
    x(0) = 2
    x'(0) = -3

with analytic solution:
    x = e^-t(-3/5sin(t) + 11/5cos(t)) - 1/10sin(2t) - 1/5cos(2t)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

nt = 1000
tstart = 0
tend = 20

tvec = np.linspace(tstart, tend, nt)


def analytic_sol(t):
    c = -3/5
    c1 = 11/5
    c2 = -1/10
    c3 = -1/5
    first = np.exp(-t)
    second = c*np.sin(t)
    third = c1*np.cos(t)
    fourth = c2*np.sin(2*t)
    fifth = c3*np.cos(2*t)
    x = first*(second + third) + fourth + fifth
    return x


def ode_model(X, t):
    xdot1 = X[1]
    xdot2 = -2*X[1] - 2*X[0] + np.sin(2*t)
    return [xdot1, xdot2]


x0 = [2, -3]
x = odeint(ode_model, x0, tvec)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(tvec, [analytic_sol(t) for t in tvec], 'r', linewidth=5,
        label='Analytic Solution')
ax.plot(tvec, x[:, 0], '-.k', linewidth=2, label='Numerical Solution')
plt.xlim([min(tvec), max(tvec)])
plt.ylim([min(x[:, 0]), max(x[:, 0])])
handles, labels = ax.get_legend_handles_labels()
lgnd = ax.legend(handles, labels, loc='upper right',
                 bbox_to_anchor=(1, 1))
plt.xlabel('t-Value', fontsize=16)
plt.ylabel('x-Value', fontsize=16)
plt.title('Plot of x\'\'(t) + 2x\'(t) + 2x = sin(2t)', fontsize=18)
plt.grid(b=True, which='both')
fig.savefig('ME426_HW3_21a', bbox_extra_artists=(lgnd,), bbox_inches='tight')
plt.show()
