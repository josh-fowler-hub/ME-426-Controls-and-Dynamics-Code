# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 14:06:46 2018

@author: jfowl
"""
from numpy import linspace
import matplotlib.pyplot as plt
from scipy.integrate import odeint

rho = 1.225
S = 8/9
CD = 0.36
P = 67000
m = 1235
vint = 22.352
vfin = 31.2928
c = rho*S*CD*(vfin - vint)
alpha = P/21


def ode_system(V, t):
    global tpos
    kp = 25
    kd = 140
    ki = 0.05
    v = V[0]
    vdot = V[1]
    gamma = V[2]
    vtilde = v
    vdotc = 0
    e = vfin - vtilde
    edot = vdotc - vdot
    tpos = kp*e + kd*edot + ki*gamma
    if tpos > 100:
        tpos = 100
    elif tpos < 0:
        tpos = 0
    else:
        tpos = tpos
    F = (tpos/100)*(P/v)
    D = 0.5*rho*S*CD*v**2
    gammadot = e
    vd = F/m - D/m
    return [vdot, vd, gammadot]


def ode_system_linear(V, t):
    global tpos
    kp = 10.1
    kd = 67
    ki = 0.025
    v = V[0]
    vdot = V[1]
    gamma = V[2]
    vtilde = v
    vdotc = 0
    e = vfin - vtilde
    edot = vdotc - vdot
    tpos = kp*e + kd*edot + ki*gamma
    if tpos > 100:
        tpos = 100
    elif tpos < 0:
        tpos = 0
    else:
        tpos = tpos
    D = c*v
    F = (tpos/100)*alpha
    gammadot = e
    vd = F/m - D/m
    return [vdot, vd, gammadot]


tvec = linspace(0, 30, 10000)
vvec = odeint(ode_system, [vint, 0, 0], tvec)
vvec2 = odeint(ode_system_linear, [vint, 0, 0], tvec)
error = []
for i in range(len(tvec)):
    error.append((abs(vvec[i, 0] - vvec2[i, 0])/vvec[i, 0])*100)


yticks = linspace(min(vvec[:, 0]), max(vvec[:, 0]), 9)
plt.figure()
plt.plot(tvec, vvec[:, 0], 'k', linewidth=3, label='Non-Linear')
plt.plot(tvec, vvec2[:, 0], '-.r', linewidth=2, label='Linear')
plt.xlabel('Time (sec)', fontsize=20)
plt.ylabel('Velocity (m/s)', fontsize=18)
plt.title('Velocity vs. Time', fontsize=18)
plt.xlim([min(tvec), max(tvec)])
if min(vvec[:, 0]) < min(vvec2[:, 0]):
    vminlim = vvec[:, 0]
else:
    vminlim = vvec2[:, 0]
if max(vvec[:, 0]) > max(vvec2[:, 0]):
    vmaxlim = vvec[:, 0]
else:
    vmaxlim = vvec2[:, 0]
yticks = linspace(min(vminlim), max(vmaxlim), 9)
plt.ylim([min(vminlim), max(vmaxlim) + 0.1])
plt.yticks(yticks)
plt.legend()
plt.grid()
plt.savefig('Controls_Project_4_tvv.png')
plt.show()

plt.figure()
plt.plot(tvec, error, 'k', linewidth=3)
plt.title('Percent Error', fontsize=20)
plt.xlabel('Time (sec)', fontsize=18)
plt.ylabel('Absolute Error (%)', fontsize=18)
plt.xlim([min(tvec), max(tvec)])
plt.ylim([min(error), max(error) + 0.1])
plt.grid()
plt.savefig('Controls_Project_4_pe.png')
plt.show()

print(sum(vvec[:, 0])/len(vvec[:, 0]))
print(vvec[-1, 0])
