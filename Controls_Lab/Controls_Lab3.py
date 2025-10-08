# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 12:31:33 2018

@author: jfowl
"""

import numpy as np
import pandas as pd

data = pd.DataFrame.from_csv('ME_429_Lab3_Data.csv', header=0, sep=',',
                             index_col=0)
data1 = pd.DataFrame.from_csv('ME_429_Lab3_Data2.csv', header=0, sep=',',
                             index_col=0)

