# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 20:03:21 2018

@author: jfowl
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import control as ctl

N, D = sig.zpk2tf(0, [-7, np.complex(0, 2), np.complex(0, -2)], 5)
sys = ctl.tf(N, D)

print('Transfer Function:\n', sys)


def transfer(s):
    tf_value = 5*s/(s**3 + 7*s**2 + 4*s + 28)
    return tf_value


tvec = np.linspace(0, 100, 1000)
ss = [transfer(t) for t in tvec]

plt.plot(tvec, ss)
