# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 21:49:25 2020

@author: byron
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib


def amdf_PE_2(inputWindow):
    D_tau = np.zeros((4,256))
    minIndices = np.empty(4)
    freq = np.empty(4)
    vol = np.empty(4)
    tau = np.arange(1,256)
    
    for c in range(4):       
        inputWindow_block = inputWindow[c*512: (c+1)*512]  
        for i,t in enumerate(tau, start = 1):
            denom = 0.5*np.sum(inputWindow_block[:2*t-2])
            shifted = np.zeros_like(inputWindow_block)
            shifted[t:] = inputWindow_block[:-t]
            D_tau[c,i] = np.sum(np.abs(inputWindow_block-shifted))/denom
            
        offset = np.argmax(D_tau[c])
        minIndices[c] = (c*512+offset)+np.argmin(D_tau[c,offset:-1])
        freq[c] = (44100/(minIndices[c]-(c*512)))
        vol[c] = 20*np.log10(np.mean(np.abs(inputWindow))) - 96.3
    
    return D_tau.flatten()


x = np.arange(0,256, 1)
# x2 = np.arange(0,5, 5/2048)
y = 44100/x
# z = np.sin(50*x2)

x3 = np.arange(0,512,1)

# d_tau = amdf_PE_2(y)

# matplotlib.rc('xtick',labelsize=16)
# matplotlib.rc('ytick',labelsize=16)

plt.subplot(211)
# plt.plot(y)
# plt.plot(z)
# plt.plot(y, 'ro')
# plt.plot(z,'go')
plt.title("Full hyperbolic pitch to frequency mapping", fontsize = 20)
# plt.xlabel("Number of samples (n)")
plt.plot( y)
plt.vlines([128,255],-5,40000)

# plt.ylabel("Amplitude",fontsize=20)

plt.subplot(212)
plt.title("Linear region of the hyperbolic function", fontsize = 20)
plt.plot(y[160:256])