# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 21:49:25 2020

@author: byron
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

with open("spectrum_levels.txt",'r') as l:
    levels = np.genfromtxt(l)

with open("spectrum_frequency.txt",'r') as f:
    sfreqs = np.genfromtxt(f)

def amdf_PE_2(inputWindow):
    D_tau = np.zeros((1,2048))
    D_tau_2 = np.zeros((1,2048))
    tau = np.arange(1,2048)
    denom = np.zeros((1,2048))
    for c in range(1):       
        inputWindow_block = inputWindow  
        for i,t in enumerate(tau):
            denom[c,i] = 0.5*np.sum(inputWindow_block[:2*t-2])
            # print(t, denom)
            shifted = np.zeros_like(inputWindow_block)
            shifted[t:] = inputWindow_block[:-t]
            D_tau[c,i] = (np.sum(np.abs(inputWindow_block-shifted))/denom[c,i])
            D_tau_2[c,i] = np.sum(np.abs(inputWindow_block-shifted))/2048
        # offset = np.argmax(D_tau[c])
        # minIndices[c] = (c*512+offset)+np.argmin(D_tau[c,offset:-1])
        # freq[c] = (44100/(minIndices[c]-(c*512)))
        # vol[c] = 20*np.log10(np.mean(np.abs(inputWindow))) - 96.3
    
    return D_tau.flatten(), D_tau_2.flatten(), denom.flatten()

T = 1/500.0
x = np.arange(0,64, 1/32)
# x2 = np.arange(0,5, 5/2048)
y = 3*np.sin(x)+np.cos(4*x)
# z = np.sin(50*x2)
fft = np.log(np.abs(np.fft.rfft(y)))
freqs = np.linspace(0, 1.0/(2.0*T), 250)

# x3 = np.arange(0,512,1)

d_tau, d_tau_2, den = amdf_PE_2(y)

# den = np.sum(y[])
matplotlib.rc('xtick',labelsize=16)
matplotlib.rc('ytick',labelsize=16)
fig,ax2 = plt.subplots()
# ax1 = fig.add_subplot(211)
# plt.subplot(211)
# ax1.plot(y)
# plt.plot(z)
# plt.plot(y, 'ro')
# plt.plot(z,'go')
# plt.title("Signal", fontsize = 20)
# # plt.xlabel("Number of samples (n)")
# plt.plot( y)
# plt.vlines([128,255],-5,40000)

# plt.ylabel("Amplitude",fontsize=20)

# ax2 = fig.add_subplot(212)
# ax2.title("AMDF Compensated")
ax2.plot(d_tau, color = 'r')
ax3 = plt.twinx(ax2)
ax3.plot(d_tau_2)
ax2.plot(den, color = 'k')
# ax2.vlines(200,-400,200)