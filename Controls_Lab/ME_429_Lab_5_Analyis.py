# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 14:01:40 2018

@author: jfowl
"""

from numba import jit
import numpy as np
import matplotlib.pyplot as plt
import control as ctl
import scipy.signal as sig

data = np.genfromtxt('Lab_5_Data.csv', delimiter=',', skip_header=1)

target_freqs = data[:, 0]

RC1_freqs = data[:, 1]
RC1_vin = data[:, 2]
RC1_vout = data[:, 3]
RC1_phi = data[:, 4]
RC1_dt = data[:, 5]
RC1_T = data[:, 6]

OA1_freqs = data[:, 7]
OA1_vin = data[:, 8]
OA1_vout = data[:, 9]
OA1_phi = data[:, 10]
OA1_dt = data[:, 11]
OA1_T = data[:, 12]

R1 = 1e3
C1 = 0.1e-9


@jit
def uncert_divide_per_row(dt, T):
    uncertanties = np.empty([len(dt)])
    for i in range(len(dt)):
        if np.isnan(dt[i]) is True:
            uncertanties[i] = 0.000005
        else:
            term1 = (1/T[i])*0.000005
            term2 = (-dt[i]/(T[i])**2)*0.000005
            uncertanties[i] = np.sqrt(term1**2 + term2**2)
    return uncertanties


@jit
def uncert_TC(phis, freqs, un_phis):
    uncertanties = np.empty([len(phis)])
    for i in range(len(phis)):
        term1 = ((-1/(np.cos(phis[i]))**2)/freqs[i])*un_phis[i]
        term2 = (-np.tan(-phis[i])/freqs[i]**2)*0.00005
        uncertanties[i] = np.sqrt(term1**2 + term2**2)
    return uncertanties


@jit
def Time_constant(phis, freqs):
    Taus = np.empty([len(phis)])
    for i in range(len(phis)):
        Taus[i] = abs(np.tan(-phis[i])/freqs[i])
    return Taus


@jit
def corner_freq(time_constants):
    corner_freqs = np.empty(len(time_constants))
    for i in range(len(time_constants)):
        if time_constants[i] == 0:
            corner_freqs[i] = 'inf'
        else:
            corner_freqs[i] = 1/time_constants[i]
    return corner_freqs


@jit
def Mags(phis):
    Mags = np.empty([len(phis)])
    for i in range(len(phis)):
        Mags[i] = 1/np.sqrt(1 + np.tan(-phis[i])**2)
    return Mags


@jit
def magnitudes(freqs, tcs):
    mags = np.empty([len(freqs)])
    for i in range(len(freqs)):
        mags[i] = -10*np.log10(tcs[i]*freqs[i]**2 + 1)
    return mags


def first_order_tf(R, C):
    tf = ctl.tf([1], [R*C, 1, 0])
    return tf


def second_order_tf(wn, tau, xo, Amp):
    zeros = np.roots([xo*tau, 0, wn*xo*tau + Amp])
    poles = [-wn*1j, wn*1j, -wn/tau]
    gain = 1
    N, D = sig.zpk2tf(zeros, poles, gain)
    tf = ctl.tf(N, D)
    return tf


RC1 = []
RC1.append(['Frequency', 'Actual Frequency', 'Vin', 'Vout', 'Phi',
            'Time Constant', 'Magnitude', 'Corner Frequency'])
RC1_tc = Time_constant(RC1_phi, RC1_freqs)
RC1_magnitudes = magnitudes(RC1_freqs, RC1_tc)
RC1_corner_freqs = corner_freq(RC1_tc)
for i in range(len(RC1_tc)):
    row = [target_freqs[i], RC1_freqs[i], RC1_vin[i], RC1_vout[i], RC1_phi[i],
           RC1_tc[i], RC1_magnitudes[i], RC1_corner_freqs[i]]
    RC1.append(row)
RC1 = np.asanyarray(RC1)
filename1 = 'ME_429_Lab5_RC1.csv'
np.savetxt(filename1, RC1, delimiter=',', fmt='%s')

OA1 = []
OA1.append(['Frequency', 'Actual Frequency', 'Vin', 'Vout', 'Phi',
            'Time Constant', 'Magnitude', 'Corner Frequency'])
OA1_tc = Time_constant(OA1_phi, OA1_freqs)
OA1_magnitudes = magnitudes(OA1_freqs, OA1_tc)
OA1_corner_freqs = corner_freq(OA1_tc)
for i in range(len(OA1_tc)):
    row = [target_freqs[i], OA1_freqs[i], OA1_vin[i], OA1_vout[i], OA1_phi[i],
           OA1_tc[i], OA1_magnitudes[i], OA1_corner_freqs[i]]
    OA1.append(row)
OA1 = np.asanyarray(OA1)
filename2 = 'ME_429_Lab5_OA1.csv'
np.savetxt(filename2, OA1, delimiter=',', fmt='%s')

RC1_tau = np.mean(RC1_tc)
OA1_tau = np.mean(OA1_tc)
RC1_wc = 1/RC1_tau
OA1_wc = 1/OA1_tau

OA1_tf = second_order_tf(OA1_wc, OA1_tau, max(OA1_vout), max(OA1_vout))
print(OA1_tf)
tout, vout = ctl.step_response(OA1_tf, np.linspace(0, 0.2, 1000))

plt.figure()
plt.plot(tout, vout)
plt.show()

plt.figure(figsize=(10, 10), dpi=384)
plt.title('Frequency vs. Magnitude', fontsize=20)
plt.semilogx(RC1_freqs, magnitudes(RC1_freqs,
                                   Time_constant(RC1_phi, RC1_freqs)),
             label='RC Circuit 1')
plt.semilogx(OA1_freqs, magnitudes(OA1_freqs,
                                   Time_constant(OA1_phi, OA1_freqs)),
             label='Op-Amp Circuit 2')
plt.xlabel('Frequency (Hz)', fontsize=16)
plt.ylabel('Magnitude (dB)', fontsize=16)
plt.grid()
plt.legend()
plt.savefig('ME_429_FvM_Lab5.png', bbox_inches='tight')
plt.show()

plt.figure(figsize=(10, 10), dpi=384)
plt.title('Frequency*Tau vs. Phase', fontsize=20)
plt.semilogx(RC1_freqs, RC1_phi, label='RC Circuit 1')
plt.semilogx(OA1_freqs, OA1_phi, label='Op-Amp Circuit 2')
plt.xlabel('Frequency*Tau', fontsize=16)
plt.ylabel('Phase (deg)', fontsize=16)
plt.grid()
plt.legend()
plt.savefig('ME_429_FvP_Lab5.png', bbox_inches='tight')
plt.show()

ctl.bode_plot(OA1_tf, omega=OA1_freqs)