# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 09:07:00 2018

@author: jfowl
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as scI
import control as ctl
import scipy.signal as sig

kp = 100
kd = 0
ki = 10

sys = ctl.tf([3*kd, 3*kp, 3*ki], [1, 4 + 3*kd, 4 + 3*kp, 3*ki])
tout = np.linspace(0, 4, 1000)
tout, aout = ctl.step_response(sys, tout)


plt.plot(tout, aout)
plt.show()

a_ss = 3*kp/(4 + 3*kp)
ess = 1 - a_ss
print(a_ss, ess)