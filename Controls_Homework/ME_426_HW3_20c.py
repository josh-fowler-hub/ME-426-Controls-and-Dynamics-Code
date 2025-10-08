# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 17:23:27 2018

@author: jfowl

x''(t) + 8x'(t) + 25x(t) = 10u(t)
with analytic solution:
    x = -e^-4t(10/25cos(3t) + 8/15sin(3t)) + 10/25
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

nt = 1000
tstart = 0
tend = 20

tvec = np.linspace(tstart, tend, nt)


def analytic_sol(t):
    c = 10/25
    c1 = 8/15
    first = -np.exp(-4*t)
    second = c*np.cos(3*t)
    third = c1*np.sin(3*t)
    x = first*(second + third) + c
    return x


def ode_model(X, t):
    xdot1 = X[1]
    xdot2 = -8*X[1] - 25*X[0] + 10
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
lgnd = ax.legend(handles, labels, loc='best',
                 bbox_to_anchor=(0.5, 0.5))
plt.xlabel('t-Value', fontsize=16)
plt.ylabel('x-Value', fontsize=16)
plt.title('Plot of x\'\'(t) + 8x\'(t) + 25x(t) = 10u(t)', fontsize=18)
plt.grid(b=True, which='both')
fig.savefig('ME426_HW3_20c', bbox_extra_artists=(lgnd,), bbox_inches='tight')
plt.show()