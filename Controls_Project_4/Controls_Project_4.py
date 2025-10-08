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
c = 0.99
alpha = P/14


def ode_system(V, t):
    global throttle_pos
    alpha = V[0]
    alphadot = V[1]
    gamma = V[2]
    kp = 2
    alphac = vfin
    kd = 1e-10
    e = alphac - alpha
    alphacdot = 0
    edot = alphacdot - alphadot
    ki = 1e-10
    u = kp*e + kd*edot + ki*gamma
    throttle_pos = u
    if throttle_pos > 100:
        throttle_pos = 100
    if alpha > vfin or alpha == vfin:
        throttle_pos = 0
    F = (throttle_pos/100)*(P/alpha)
    D = 0.5*rho*S*CD*alpha**2
    alphaddot = F/m - D/m
    gammadot = e
    system = [alphadot, alphaddot, gammadot]
    return system


def ode_system_linear(V, t):
    global throttle_pos
    v = V
    kp = 10
    vtilde = v
    e = vfin - vtilde
    throttle_pos = kp*e
    if throttle_pos > 100:
        throttle_pos = 100
    if v > vfin or v == vfin:
        throttle_pos = 0
    F = (throttle_pos/100)*alpha
    D = c*v
    vd = F/m - D/m
    return vd


tvec = linspace(0, 45, 1000)
vvec = odeint(ode_system, [vint, 0, 0], tvec)
vvec2 = odeint(ode_system_linear, vint, tvec)
#vvec2 = [v - (max(vvec2) - max(vvec)) for v in vvec2]

error = []
for i in range(len(tvec)):
    error.append((abs(vvec[i] - vvec2[i])/vvec[i])*100)


yticks = linspace(min(vvec[:, 0]), max(vvec[:, 0]), 9)
plt.figure()
plt.plot(tvec, vvec[:, 0], 'k', linewidth=3, label='Non-Linear')
plt.plot(tvec, vvec2, '-.r', linewidth=2, label='Linear')
plt.xlabel('Time (sec)', fontsize=20)
plt.ylabel('Velocity (m/s)', fontsize=18)
plt.title('Velocity vs. Time', fontsize=18)
#plt.xlim([min(tvec), max(tvec)])
#plt.ylim([min(vvec), max(vvec2) + 0.1])
plt.yticks(yticks)
plt.legend()
plt.grid(b=True, linestyle='--')
plt.show()

plt.figure()
plt.plot(tvec, error, 'k', linewidth=3)
plt.title('Percent Error', fontsize=20)
plt.xlabel('Time (sec)', fontsize=18)
plt.ylabel('Absolute Error (%)', fontsize=18)
#plt.xlim([min(tvec), max(tvec)])
#plt.ylim([min(error), max(error) + 0.1])
plt.grid(b=True, linestyle='--')
plt.show()
