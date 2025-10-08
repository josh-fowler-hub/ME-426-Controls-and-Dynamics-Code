# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 14:53:14 2018

@author: jfowl
"""

import numpy as np

data = np.genfromtxt('C:/Users/jfowl/Downloads/Lab_6_controls_lab.csv',
                     delimiter=',', skip_header=1, usecols=(5, 6, 7, 8, 9))


A1 = data[:, 0]
A2 = data[:, 1]
A3 = data[:, 2]
Vout = data[:, 3]
Vref = 10.02


def ADC_equation(As, Vref):
    constant = Vref
    terms = []
    for i in range(len(As)):
        terms.append(As[i]/(2**(i + 1)))
    tot = constant*sum(terms)
    return tot


Vout_a = []
for i in range(len(A1)):
    Vout_a.append(ADC_equation([A1[i], A2[i], A3[i]], Vref))

filename = 'ME_429_Lab6.csv'
names = ['$A_1$', '$A_2$', '$A_3$',
         '$ V_{out} $',
         '$ V_{Expected} $']
final_data = []
final_data.append(names)
for i in range(len(names)):
    row = [A1[i], A2[i], A3[i], Vout[i], Vout_a[i]]
    final_data.append(row)
final_data = np.asanyarray(final_data)
np.savetxt(filename, final_data, delimiter=',', fmt='%s')

print(Vout)
print(Vout_a)
