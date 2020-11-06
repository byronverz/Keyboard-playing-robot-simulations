# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 14:37:33 2020

@author: byron
"""

import numpy as np
import matplotlib.pyplot as plt

y = [485.96, 500.68, 519.64, 536.6, 551.76, 570.52, 589.74, 608.88, 630.02, 649.12, 669.34, 693.12, 718.12, 741.06, 762.46, 783.52, 798.18, 818.48, 834.38, 857.76, 875.9, 897.82, 915.48, 932.38, 946.84]
x = np.arange(0,25)
# for i in range(25):
   # y.append(sum(key_measures[10*i:10*(i+1)])/10)
    
z = np.polyfit(x,y,1)    
y2 = x*(z[0])+z[1]
plt.plot(x,y)
plt.plot(x,y2)
print(z) 