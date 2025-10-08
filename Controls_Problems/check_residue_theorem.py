# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 00:58:06 2018

@author: jfowl
"""

import numpy as np
import control as ctl
import matplotlib.pyplot as plt
import scipy.signal as sig


def residue_calc(N, D):
    Zeros = np.roots(N)
    Poles = np.roots(D)
    numers = []
    denoms = []
    res = []
    for i in range(len(Poles)):
        terms = []
        for j in range(len(Poles)):
            if i == j:
                pass
            else:
                terms.append(Poles[i] + Poles[j])
        denoms.append(np.prod(terms))
    for i in range(len(Poles)):
        nums = []
        for j in range(len(Zeros)):
            if i == j:
                pass
            else:
                nums.append(Poles[i] + Zeros[j])
        numers.append(np.prod(nums))
    for i in range(len(Poles)):
        res.append([numers[i]/denoms[i], Poles[i]])
    return res


def residue(N, D, tvec):
    residues = residue_calc(N, D)
    values = []
    for t in tvec:
        nums = []
        for r in residues:
            nums.append(r[0]*np.exp(r[1]*t))
        values.append(sum(nums))
    return values

tvec = np.linspace(0, 5, 50)
N, D = sig.zpk2tf([0, -2], [0, 0, -2, -3], 25)
sys = ctl.tf(N, D)
res = residue(N, D, tvec)
tout, yout = ctl.impulse_response(sys, tvec)
plt.plot(tvec, res)
plt.plot(tout, yout)
