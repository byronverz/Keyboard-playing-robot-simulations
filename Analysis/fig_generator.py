# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 21:49:25 2020

@author: byron
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

x = np.arange(0,2*np.pi, np.pi/8)
y = np.sin(x)
z = np.sin(x+3*(np.pi/8))

matplotlib.rc('xtick',labelsize=16)
matplotlib.rc('ytick',labelsize=16)
plt.plot(y)
plt.plot(z)
plt.plot(y, 'ro')
plt.plot(z,'go')
plt.xlabel("Samples (n)", fontsize=20)
plt.ylabel("Amplitude",fontsize=20)
