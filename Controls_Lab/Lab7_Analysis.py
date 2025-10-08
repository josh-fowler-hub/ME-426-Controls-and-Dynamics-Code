# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 18:51:13 2018

@author: jfowl
"""

import numpy as np
import matplotlib.pyplot as plt


run1 = np.genfromtxt('Lab7_run1.csv', delimiter=',', skip_header=1)
run2 = np.genfromtxt('Lab7_run2.csv', delimiter=',', skip_header=1)
run3 = np.genfromtxt('Lab7_run3.csv', delimiter=',', skip_header=1)
run4 = np.genfromtxt('Lab7_run4.csv', delimiter=',', skip_header=1)
run5 = np.genfromtxt('Lab7_run5.csv', delimiter=',', skip_header=1)

data = [run1, run2, run3, run4, run5]

for i in range(len(data)):
    data_current = data[i]
    x = data_current[:, 0]
    y = data_current[:, 1]
    plt.figure(i)
    plt.plot(x, y)
    plt.title('Lab Data: Run {}'.format(i + 1))
    plt.xlabel('Time (Sec)')
    plt.ylabel('Voltage (Volts)')
    plt.grid()
    plt.savefig('Lab7_Run{}_Graph.png'.format(i + 1))
    plt.show()
    plt.figure(i + len(data))
    plt.plot(x, y)
    plt.title('Lab Data: Run {} Zoom'.format(i + 1))
    plt.xlabel('Time (Sec)')
    plt.ylabel('Voltage (Volts)')
    plt.xlim([0, 0.2])
    plt.grid()
    plt.savefig('Lab7_Run{}_Graph_Zoom.png'.format(i + 1))
    plt.show()
