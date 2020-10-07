# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 12:07:26 2020

@author: byron
"""

import numpy as np
import matplotlib.pyplot as plt

filepath = '../../BBBW_Code/step_test_results.csv'
with open(filepath) as step_file:
    test_results = np.genfromtxt(step_file)


plt.plot(test_results)