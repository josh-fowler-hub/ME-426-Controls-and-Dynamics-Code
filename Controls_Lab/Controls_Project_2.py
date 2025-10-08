# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 19:27:50 2018

@author: jfowl
"""

import numpy as np
import os

cwd = os.getcwd()

h_h2o = np.genfromtxt(cwd + '\\Heating_Water_Project.csv', delimiter=',',
                      skip_header=1)
hac_h2o = np.genfromtxt(cwd + '\\Heating_and_Cooling_Water_Project.csv',
                        delimiter=',',
                        skip_header=1)
