# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 08:26:16 2018

@author: jfowl
"""
import control as ctl
import numpy as np
import matplotlib.pyplot as plt


# Proportional Gain
Kp_vec = np.linspace(0, 15, 100)

plt.figure(1)
ax = plt.gca()
ax.set_facecolor((0, 0, 0))
for Kp in Kp_vec:
    # Control
    C = Kp

    # Actuator Dynamics
    a = 3
    A = ctl.tf(a, [1, a])

    # Plant Dynamics
    G = ctl.tf(3, [1, 3, 2])
    GCL = C*G/(1 + C*G)
    CAGCL = (C*A*G)/(1 + C*A*G)

    # Response
    tout = np.linspace(0, 2.5, 1000)
    toutOL, youtOL = ctl.step_response(G, tout)
    toutCL, youtCL = ctl.step_response(GCL, tout)
    toutCAGCL, youtCAGCL = ctl.step_response(CAGCL, tout)
    plt.plot(toutOL, youtOL, label='No Actuator')
    plt.plot(toutCL, youtCL, label='No Actuator, Closed Loop')
    plt.plot(toutCAGCL, youtCAGCL, label='With Actuator')
    plt.xlim([min(toutOL), max(toutOL)])
    plt.ylim([min(youtCAGCL), max(youtCAGCL)])
    plt.xticks([])
    plt.yticks([])
    plt.pause(0.005)



