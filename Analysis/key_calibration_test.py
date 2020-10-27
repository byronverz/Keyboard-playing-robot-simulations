# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 14:37:33 2020

@author: byron
"""

import numpy as np
import matplotlib.pyplot as plt

y = [372.44, 388.28, 404.64, 422.84, 440.92, 459.62, 476.24, 496.72, 515.88, 537.36, 
     561.4, 581.68, 604.04, 628.88, 651.24, 675.44, 703.24, 731.76, 751.44, 778.0, 
     795.92, 816.28, 830.68, 846.44, 859.44]
x = np.arange(0,25)
# for i in range(25):
   # y.append(sum(key_measures[10*i:10*(i+1)])/10)
    
z = np.polyfit(x,y,1)    
y2 = x*(z[0])+z[1]
plt.plot(x,y)
plt.plot(x,y2)
print(z) 