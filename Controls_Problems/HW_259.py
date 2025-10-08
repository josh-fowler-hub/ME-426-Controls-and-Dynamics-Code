# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 21:57:10 2018

@author: jfowl
"""

import numpy as np
import matplotlib.pyplot as plt

print('Problem 2.59)')
print('\n')
k = 2000
m = 5
wn = np.sqrt(k/m)
xos = [0.020, -0.020, 0.020, -0.020]
xdotos = [0.2, 0.2, -0.2, -0.2]
phis = []
As = []

for i in range(len(xos)):
    phis.append(round(np.arctan((xos[i]*wn)/xdotos[i]), 4))
    As.append(round(np.sqrt((xos[i])**2 + (xdotos[i]/wn)**2), 4))

for i in range(len(As)):
    print('phi_{} = tan^-1(({}*{})/{})'.format(i, xos[i], wn, xdotos[i]))
    print('A_{} = [{}**2 + ({}/{})**2]**(1/2)'.format(i,xos[i], xdotos[i],
          wn))
    print('x(t)_{} = {}*cos({}*t - {})'.format(i, As[i], wn, phis[i]))

print('\n\n')
print('Problem 2.60)')
k1 = 1000
m1 = 10
wn1 = np.sqrt(k1/m1)
xos1 = [0.010, -0.010, 0.010, -0.010]
xdotos1 = [0.1, 0.1, -0.1, -0.1]
phis1 = []
As1 = []

for i in range(len(xos1)):
    phis1.append(round(np.arctan((xos1[i]*wn1)/xdotos1[i]), 4))
    As1.append(round(np.sqrt((xos1[i])**2 + (xdotos1[i]/wn1)**2), 4))

print('\n')
for i in range(len(As1)):
    print('phi_{} = tan^-1(({}*{})/{})'.format(i, xos1[i], wn1, xdotos1[i]))
    print('A_{} = [{}**2 + ({}/{})**2]**(1/2)'.format(i,xos1[i], xdotos1[i],
          wn1))
    print('x(t)_{} = {}*cos({}*t - {})'.format(i, As1[i], wn1, phis1[i]))
