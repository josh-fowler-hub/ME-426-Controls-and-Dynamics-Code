# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 17:24:06 2018

@author: jfowl

x''(t) + 4x = t^2
with initial conditions:
    x(0) = 1
    x'(0) = 2

with analytic solution:
    x = 9/8cos(2t) + sin(2t) + 1/4t^2 - 1/8
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

nt = 1000
tstart = 0
tend = 20

tvec = np.linspace(tstart, tend, nt)


def analytic_sol(t):
    c = 9/8
    c1 = 1/4
    c2 = -1/8
    first = c*np.cos(2*t)
    second = np.sin(2*t)
    third = c1*t**2
    fourth = c2
    x = first + second + third + fourth
    return x


def ode_model(X, t):
    xdot1 = X[1]
    xdot2 = -4*X[0] + t**2
    return [xdot1, xdot2]


x0 = [1, 2]
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
                 bbox_to_anchor=(0, 1))
plt.xlabel('t-Value', fontsize=16)
plt.ylabel('x-Value', fontsize=16)
plt.title('Plot of x\'\'(t) + 4x = t^2', fontsize=18)
plt.grid(b=True, which='both')
fig.savefig('ME426_HW3_21c', bbox_extra_artists=(lgnd,), bbox_inches='tight')
plt.show()
