# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 21:34:35 2018

@author: jfowl
"""
import numpy as np
import control as ctl
import matplotlib.pyplot as plt

this_clss = 'ME_426'
homework = 'HW_5'



# %% PROBLEM 2a FOR PROBLEM 3


def sys_model2a(tv):
    """Problem 2a"""
    x = []
    for t in tv:
        x.append(1 - np.exp(-5*t))
    return x


tvec2a = np.linspace(0, 2, 1000)
tf2a = ctl.tf([5], [1, 5, 0])
tout2a, cout2a = ctl.impulse_response(tf2a, tvec2a)

plt.figure(1, figsize=(22, 14))
plt.plot(tvec2a, sys_model2a(tvec2a), 'r', linewidth=4,
         label='Analytic Solution')
plt.plot(tout2a, cout2a, '-.k', linewidth=2, label='Transfer Function Model')
plt.xlim([min(tvec2a), max(tvec2a)])
plt.ylim([min(cout2a), max(cout2a)])
plt.xlabel('Time (s)', fontsize=16)
plt.ylabel('C(t)', fontsize=16)
plt.title('C(t) vs. Time {}'.format(sys_model2a.__doc__), fontsize=18)
plt.legend()
plt.grid()
plt.savefig('{}_{}_{}_Plot.png'.format(this_clss, homework,
            sys_model2a.__doc__))
plt.show()
# %% PROBLEM 2b FOR PROBLEM 3


def sys_model2b(tv):
    """Problem 2b"""
    x = []
    for t in tv:
        x.append(1 - np.exp(-20*t))
    return x


tvec2b = np.linspace(0, 2, 1000)
tf2b = ctl.tf([20], [1, 20, 0])
tout2b, cout2b = ctl.impulse_response(tf2b, tvec2b)

plt.figure(2, figsize=(22, 14))
plt.plot(tvec2b, sys_model2b(tvec2b), 'r', linewidth=4,
         label='Analytic Solution')
plt.plot(tout2b, cout2b, '-.k', linewidth=2, label='Transfer Function Model')
plt.xlim([min(tvec2b), max(tvec2b)])
plt.ylim([min(cout2b), max(cout2b)])
plt.xlabel('Time (s)', fontsize=16)
plt.ylabel('C(t)', fontsize=16)
plt.title('C(t) vs. Time {}'.format(sys_model2b.__doc__), fontsize=18)
plt.legend()
plt.grid()
plt.savefig('{}_{}_{}_Plot.png'.format(this_clss, homework,
            sys_model2b.__doc__))
plt.show()
