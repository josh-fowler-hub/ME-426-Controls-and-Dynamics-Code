# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 08:28:52 2018

@author: jfowl
"""

import numpy as np
from sympy import symbol

t = symbol.Symbol('t')

A = np.array([[0, 1], [-1, -2]])

Ainv = np.linalg.inv(A)
print(Ainv)