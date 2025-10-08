# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 20:05:03 2018

@author: jfowl
"""
# %% Imports

import numpy as np
import matplotlib.pyplot as plt
import My_Scripts.Stats_Practice.Regression as regress

# %% RC Circuit 1

t1 = [0, 4e-05, 6e-05, 8e-05, 0.0001, 0.00013, 0.00016, 0.00019, 0.00024,
      0.00029, 0.00031, 0.00034, 0.0004, 0.00048, 0.00056, 0.00061, 0.00068,
      0.00095, 0.00107]

v1 = [-1.02, -0.64, -0.36, -0.14, 0.06, 0.28, 0.46, 0.58, 0.74, 0.86, 0.88,
      0.92, 0.96, 1, 1.02, 1.02, 1.04, 1.04, 1.04]

v1 = [v - min(v1) + 1e-10 for v in v1]
vlog1 = [np.log(v) for v in v1]
tau1_inv, lnvo1 = regress.regression_eq1(t1, vlog1)
tau1 = 1/tau1_inv
vo1 = np.exp(lnvo1)
v1 = [v - 1e-10 for v in v1]

tvec1 = np.linspace(min(t1), max(t1), 1000)
vout1 = [max(v1)*(1 - np.exp(-t/tau1)) for t in tvec1]


# %% RC Circuit 2

t2 = [0, 1.2e-05, 2.8e-05, 4e-05, 6e-05, 7.6e-05, 9.2e-05, 0.000112, 0.000136,
      0.000168, 0.000192, 0.000216, 0.000236, 0.000268, 0.000312, 0.000352,
      0.000388, 0.000424, 0.000468, 0.000508, 0.000584, 0.000716, 0.000808]

v2 = [1.88, 1.7, 1.48, 1.34, 1.12, 0.98, 0.86, 0.72, 0.58, 0.44, 0.36, 0.3,
      0.26, 0.2, 0.14, 0.1, 0.08, 0.06, 0.06, 0.04, 0.04, 0.02, 0.02]

v2 = [v - min(v2) + 1e-10 for v in v2]
vlog2 = [np.log(v) for v in v2]
tau2_inv, lnvo2 = regress.regression_eq1(t2, vlog2)
tau2 = -1/tau2_inv
vo2 = np.exp(lnvo2)
v2 = [v - 1e-10 for v in v2]

tvec2 = np.linspace(min(t2), max(t2), 1000)
vout2 = [max(v2)*(np.exp(-t/tau2)) for t in tvec2]


# %% RC Circuit 3

t3 = [0, 0.0002, 0.0003, 0.0004, 0.0005, 0.0007, 0.0009, 0.0011, 0.0019,
      0.0031, 0.0059996, 0.0059998, 0.0059999, 0.006, 0.0060001, 0.0060002,
      0.0060006, 0.0072, 0.0081, 0.0097, 0.0112]

v3 = [1.04, 0.48, 0.02, -0.3, -0.5, -0.78, -0.9, -0.98, -1.02, -1.02, -1.02,
      -0.56, -0.1, 0.24, 0.48, 0.66, 0.94, 1.02, 1.04, 1.04, 1.04]

v32 = [v - min(v3) + 1e-10 for v in v3]
v32 = v32[:10]
t32 = t3[:10]
vlog3 = [np.log10(v) for v in v32]
tau3_inv, lnvo3 = regress.regression_eq1(t32, vlog3)
tau3 = -1/tau3_inv
vo3 = np.exp(lnvo3)
v32 = [v - 1e-10 for v in v32]
tvec3 = np.linspace(min(t32), max(t32), 1000)
vout3 = [max(v32)*(np.exp(-t/tau3)) for t in tvec3]


# %% Op-Amp Circuit 1

t4 = [0, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009, 0.01, 0.011,
      0.012, 0.013, 0.014, 0.015, 0.016, 0.017, 0.018, 0.019, 0.02, 0.021,
      0.022, 0.023, 0.024, 0.025, 0.026, 0.027, 0.028, 0.029, 0.03, 0.031,
      0.032, 0.033, 0.034, 0.035, 0.036, 0.037, 0.038, 0.039, 0.04, 0.041,
      0.042, 0.043, 0.044, 0.046, 0.047, 0.048, 0.049, 0.05, 0.051, 0.052,
      0.053, 0.054, 0.055, 0.056, 0.057, 0.058, 0.059, 0.06, 0.061, 0.062,
      0.063, 0.064, 0.065]

v4 = [5.24, 4.08, 2, 0.88, 1.48, 2.92, 3.96, 3.84, 2.88, 2, 1.88, 2.48, 3.16,
      3.4, 3.08, 2.56, 2.28, 2.44, 2.8, 3.04, 3, 2.8, 2.56, 2.52, 2.68, 2.84,
      2.92, 2.84, 2.68, 2.64, 2.68, 2.76, 2.84, 2.8, 2.76, 2.68, 2.68, 2.72,
      2.8, 2.8, 2.76, 2.72, 2.72, 2.72, 2.76, 2.76, 2.76, 2.72, 2.72, 2.76,
      2.76, 2.76, 2.76, 2.76, 2.76, 2.76, 2.76, 2.76, 2.76, 2.76, 2.76, 2.76,
      2.76, 2.76]


tvec4 = np.linspace(min(t4), max(t4), 1000)

R1 = 10e3
R2 = 10e3
RA = 10e3
RB = 5e3
C1 = 0.1e-6
C2 = 0.1e-6

Vin = 2.76
M = C1*C2*(R1*R2*RB)/(RA + RB)
K = RB/(RA + RB)
wn = (K/M)**0.5
zeta = 0.5*((R1*C2/(R2*C1))**0.5 + (R2*C2/(R1*C1))**0.5 -
            (RA/RB)*(R1*C1/(R2*C2))**0.5)
wd = wn*(1 - (zeta**2))**0.5


def vout_opa1(tvec):
    phi = 10*np.pi/9
    A1 = 1/(1 - 0.09**2)**0.5
    vout = []
    for t in tvec:
        vout.append(Vin*(1 - A1*np.exp(-0.09*wn*t)*np.sin(wd*t + phi)))
    return vout


vout4 = vout_opa1(tvec4)

# %% Plots

plt.figure()
plt.plot(t1, v1, label='Experimental Data', linewidth=2)
plt.plot(tvec1, vout1, label='Regression Time Constant Estimate Tau={}'.format(
        round(tau1, 5)), linewidth=2)
plt.title('RC Circuit 1', fontsize=18)
plt.xlabel('Time (sec)', fontsize=16)
plt.ylabel('Voltage (V)', fontsize=16)
plt.legend()
plt.grid()
plt.savefig('Lab4_RC_Circuit1.png')
plt.show()

plt.figure()
plt.plot(t2, v2, label='Experimental Data', linewidth=2)
plt.plot(tvec2, vout2, label='Regression Time Constant Estimate Tau={}'.format(
        round(tau2, 5)), linewidth=2)
plt.title('RC Circuit 2', fontsize=18)
plt.xlabel('Time (sec)', fontsize=16)
plt.ylabel('Voltage (V)', fontsize=16)
plt.legend()
plt.grid()
plt.savefig('Lab4_RC_Circuit2.png')
plt.show()

plt.figure()
plt.plot(t32, v32, label='Experimental Data', linewidth=2)
plt.plot(tvec3, vout3, label='Regression Time Constant Estimate Tau={}'.format(
        round(tau3, 5)), linewidth=2)
plt.title('RC Circuit 3', fontsize=18)
plt.xlabel('Time (sec)', fontsize=16)
plt.ylabel('Voltage (V)', fontsize=16)
plt.legend()
plt.grid()
plt.savefig('Lab4_RC_Circuit3.png')
plt.show()

plt.figure()
plt.plot(t4, v4, label='Experimental Data', linewidth=2)
plt.plot(tvec4, vout4, label='Theoretical Fit zeta=0.09, wn=1000', linewidth=2)
plt.title('Op-Amp Circuit 1', fontsize=18)
plt.xlabel('Time (sec)', fontsize=16)
plt.ylabel('Voltage (V)', fontsize=16)
plt.legend()
plt.grid()
plt.savefig('Lab4_OA_Circuit1.png')
plt.show()
