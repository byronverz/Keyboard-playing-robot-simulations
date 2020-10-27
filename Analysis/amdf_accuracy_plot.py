# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 13:40:26 2020

@author: byron
"""

import numpy as np
import matplotlib.pyplot as plt

with open("../key_freq_list.txt", 'r') as kfile:
    key_freq_list = np.genfromtxt(kfile)



freqs = [630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 639.1304347826087, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 639.1304347826087, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 639.1304347826087, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0]
h, b = np.histogram(freqs)
plt.title("4 Keys/Window accuracy test (D5-#)")
plt.hist(freqs, bins = 9)
plt.vlines(x=[604.79, 640.75], ymin = 0, ymax = 22)
plt.vlines(x=[622.25], ymin = 0 ,ymax = 22, colors='red')