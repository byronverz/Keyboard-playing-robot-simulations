# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 12:07:26 2020

@author: byron
"""

import numpy as np
import matplotlib.pyplot as plt

with open('step_test_with_linear_controller_frequency_1.txt','r') as f:
    freq = np.genfromtxt(f)

with open('step_test_with_linear_controller_error_1.txt','r') as e:
    error = np.genfromtxt(e)

with open('step_test_with_linear_controller_distance_1.txt','r') as d:
    dist = np.genfromtxt(d)

with open("PI_freq_test2.txt", 'r') as p:
    pi = np.abs(np.genfromtxt(p))
    
sp = [0 for i in range(10)]
for t in range(404):
    sp.append(658.028)

# x = np.arange(0,10.35,0.025)

fig, ax1= plt.subplots()
# ax1.plot(dist)
# ax1.hlines([579.74],0,3)
# ax1.vlines([3], 0,580)
# ax1.plot(x,sp)
# plt.xticks(x)
ax2 = plt.twinx()
# plt.plot(error)
ax2.plot(pi, color='red')