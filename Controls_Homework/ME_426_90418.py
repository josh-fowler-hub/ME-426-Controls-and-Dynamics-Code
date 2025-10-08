# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 08:39:59 2018

@author: jfowl
"""

from numpy import linspace
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from control import tf, step_response
import scipy.signal as S
import scipy.linalg as slin

k = 0.5
c = 0.02

N = [120*k]
D = [1, c]
sys = tf(N, D)
print(sys)
tout = linspace(0, 10, 1000)
tout, yout = step_response(sys, tout)
plt.plot(tout, yout, 'g--', label='Simulation')
plt.title('Time vs. Windspeed')
plt.xlabel('Time (sec)')
plt.ylabel('Measured Windspeed (m/s)')
plt.grid(b=True, which='both')
plt.show()
