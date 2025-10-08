# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 23:17:28 2018

@author: jfowl
"""
import numpy as np
import sympy as sp
from fractions import Fraction

s = sp.Symbol('s')

Exp = 2/s**3 + (s + 2)

Exp = sp.ratsimp(Exp)
print(Exp)
print('\n')
Exp = Exp/(s**2 + 4)
Exp = sp.ratsimp(Exp)
print(Exp)
