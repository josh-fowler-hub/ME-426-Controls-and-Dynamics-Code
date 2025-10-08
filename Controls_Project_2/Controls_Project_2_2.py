# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 14:43:09 2018

@author: jfowl
"""

import numpy as np
import matplotlib.pyplot as plt
import control as ctl
import scipy.signal as sig
import scipy.integrate as integrate
import os

cwd = os.getcwd()


h_h2o = np.genfromtxt(cwd + '\\Cooling_Thermocouple.csv', delimiter=',',
                      skip_header=1,
                      usecols=(0, 3))

Tinf = min(h_h2o[:, 1])
T0 = max(h_h2o[:, 1])
tau = []
i = 0

for T in h_h2o[:, 1]:
    if T < 0.632*max(h_h2o[:, 1]) + 0.1 and T > 0.632*max(h_h2o[:, 1]) - 0.1:
        tau.append(h_h2o[i, 0])
    else:
        pass
    i += 1

tau = sum(tau)/len(tau)


def ode_model(T, t):
    dTdt = (1/tau)*(Tinf - T)
    return dTdt


def analytic(t):
    Temp = T0*np.exp(-t/tau) + Tinf*(1 - np.exp(-t/tau))
    return Temp


tvec = np.linspace(min(h_h2o[:, 0]), max(h_h2o[:, 0]), 569)

ode = integrate.odeint(ode_model, max(h_h2o[:, 1]), tvec)

N, D = sig.zpk2tf([], [-1/tau, 0], [Tinf/tau])
sys = ctl.tf(N, D)
print('Transfer Function F(s):')
print(sys)
tout = np.linspace(min(h_h2o[:, 0]), max(h_h2o[:, 0]), 569)
ts, Tout = ctl.step_response(sys, tout)

plt.figure()
plt.plot(h_h2o[:, 0], h_h2o[:, 1], linewidth=2, label='Experimental Data')
plt.plot(tvec, ode, '--r', linewidth=2,
                label='Simulation')
plt.legend()
plt.xlabel('Time (sec)', fontsize=16)
plt.ylabel('Temperature (C)', fontsize=16)
plt.title('Temperature vs. Time in a Thermocouple', fontsize=18)
plt.xlim([min(h_h2o[:, 0]), max(h_h2o[:, 0])])
plt.ylim([min(h_h2o[:, 1]), max(h_h2o[:, 1])])
plt.grid()
plt.savefig(cwd + '\\tVT_Thermocouple.png')
plt.show()
