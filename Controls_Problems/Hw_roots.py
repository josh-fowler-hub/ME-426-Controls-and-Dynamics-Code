# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 23:33:24 2018

@author: jfowl
"""
import numpy as np
import matplotlib.pyplot as plt

roots = np.roots([1, 10, 35, 50, 264])

plt.figure()
plt.plot([0 for x in np.arange(-6, 5)], [y for y in np.arange(-6, 5)], '--k')
plt.plot([x for x in np.arange(-6, 5)], [0 for y in np.arange(-6, 5)], '--k')
plt.title('P-Z Map', fontsize=20)
plt.xlabel('Re', fontsize=20)
plt.ylabel('Im', fontsize=20)
for r in roots:
    plt.plot(r.real, r.imag, 'xk')
    plt.grid(True)