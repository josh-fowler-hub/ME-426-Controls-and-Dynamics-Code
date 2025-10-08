# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 19:27:50 2018

@author: jfowl

Analysis of the response of a thermocouple to sudden temperature change.
Starting with the thermocouple submerged in ice water, we waited until the
thermocouple reached steady state. Then the thermocouple was quickly submerged
in boiling water until it reached steady state. The system was then analyzed
using the following code, and compared against a simulation of the system
using the following first order equation:
    dT/dt + 1/tau * T = 1/tau * Tinf
"""
# %%

import numpy as np
import matplotlib.pyplot as plt
import control as ctl
import scipy.signal as sig
import scipy.integrate as integrate
import os
import My_Scripts.Python_Tools.timer_tools as tt

# %%

print(__doc__)
print('\n')

timer = tt.start_timer()
timer.start()
fid1 = '\\First_Thermocouple.csv'
print('Working Directory: {}'.format(os.getcwd()))
print('\n')

cwd = os.getcwd()

print('Converting File {} to an array .....'.format(cwd + fid1))
h_h2o = np.genfromtxt(cwd + fid1, delimiter=',',
                      skip_header=1,
                      usecols=(2, 0))

print('..... File Converted.')
timer.show()
timer.incrmt()
print('Parameters:')
Tinf = max(h_h2o[:, 1])
T0 = min(h_h2o[:, 1])
tau = []
i = 0
print('\tTinf: {} C\n\tT0: {} C'.format(Tinf, T0))

for T in h_h2o[:, 1]:
    if T < 0.632*max(h_h2o[:, 1]) + 1.5 and T > 0.632*max(h_h2o[:, 1]) - 1.5:
        tau.append(h_h2o[i, 0])
    else:
        pass
    i += 1

tau = sum(tau)/len(tau)
print('\tTime Constant: {} sec'.format(tau))
print('\n')

# %%


def ode_model(T, t):
    dTdt = (1/tau)*(Tinf - T)
    return dTdt


def analytic(t):
    Temp = T0*np.exp(-t/tau) + Tinf*(1 - np.exp(-t/tau))
    return Temp


# %%

print('Computing Solutions .....')

tvec = np.linspace(min(h_h2o[:, 0]), max(h_h2o[:, 0]), 569)

ode = integrate.odeint(ode_model, min(h_h2o[:, 1]), tvec)

N, D = sig.zpk2tf([], [-1/tau, 0], [Tinf/tau])
w, mag, phase = sig.bode(([], [-1/tau, 0], [Tinf/tau]))
sys = ctl.tf(N, D)
tout = np.linspace(min(h_h2o[:, 0]), max(h_h2o[:, 0]), 569)
ts, Tout = ctl.impulse_response(sys, tout)

print('..... Solutions Computed')
timer.show()
timer.incrmt()
print('Transfer Function F(s):')
print(sys)
print('Displaying Plots .....')

# %%

[p, z] = ctl.pzmap(sys, True)

plt.figure()
plt.plot(h_h2o[:, 0], h_h2o[:, 1], linewidth=2, label='Experimental Data')
plt.plot(tvec, [analytic(t) for t in tvec], '--r', linewidth=2,
         label='Simulation')
plt.legend()
plt.xlabel('Time (sec)', fontsize=16)
plt.ylabel('Temperature (C)', fontsize=16)
plt.title('Response of a Thermocouple: Analytic', fontsize=18)
plt.xlim([min(h_h2o[:, 0]), max(h_h2o[:, 0])])
plt.ylim([min(h_h2o[:, 1]), max(h_h2o[:, 1])])
plt.grid()
plt.savefig(cwd + '\\tVT_Thermocouple_analytic.png')
plt.show()

plt.figure()
plt.plot(h_h2o[:, 0], h_h2o[:, 1], linewidth=2, label='Experimental Data')
plt.plot(tvec, ode, '--k', linewidth=2, label='Simulation')
plt.legend()
plt.xlabel('Time (sec)', fontsize=16)
plt.ylabel('Temperature (C)', fontsize=16)
plt.title('Response of a Thermocouple: odeint', fontsize=18)
plt.xlim([min(h_h2o[:, 0]), max(h_h2o[:, 0])])
plt.ylim([min(h_h2o[:, 1]), max(h_h2o[:, 1])])
plt.grid()
plt.savefig(cwd + '\\tVT_Thermocouple_odeint.png')
plt.show()

plt.figure()
plt.plot(ts, Tout, '--g', linewidth=2, label='Simulation')
plt.plot(h_h2o[:, 0], h_h2o[:, 1], linewidth=2, label='Experimental Data')
plt.legend()
plt.xlabel('Time (sec)', fontsize=16)
plt.ylabel('Temperature (C)', fontsize=16)
plt.title('Response of a Thermocouple: impulse_response', fontsize=18)
plt.xlim([min(h_h2o[:, 0]), max(h_h2o[:, 0])])
plt.ylim([min(h_h2o[:, 1]), max(h_h2o[:, 1])])
plt.grid()
plt.savefig(cwd + '\\tVT_Thermocouple_impulse.png')
plt.show()

plt.figure()
plt.semilogx(w, mag)
plt.xlabel('Frequency', fontsize=16)
plt.ylabel('Magnitude', fontsize=16)
plt.title('Frequency vs. Magnitude', fontsize=18)
plt.xlim([min(w), max(w)])
plt.ylim([min(mag), max(mag)])
plt.grid()
plt.savefig(cwd + '\\wvmag_Thermocouple.png')
plt.show()

plt.figure()
plt.semilogx(w, phase)
plt.xlabel('Frequency', fontsize=16)
plt.ylabel('Amplitude', fontsize=16)
plt.title('Frequency vs. Amplitude', fontsize=18)
plt.xlim([min(w), max(w)])
plt.ylim([min(phase), max(phase)])
plt.grid()
plt.savefig(cwd + '\\wvphase_Thermocouple.png')
plt.show()

print('..... Plots Displayed')
# %%
timer.show()
timer.incrmt()
timer.end()
