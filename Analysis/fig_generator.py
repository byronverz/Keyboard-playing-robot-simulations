# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 21:49:25 2020

@author: byron
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import scipy.interpolate as interpolate

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
x = np.arange(1,2048, 1)
# x2 = np.arange(0,3,0.001)
# x2 = np.arange(0,5, 5/2048)
y = 10000/x
y2 = 20000/x
y3 = 44100/x
# z = np.polyfit(x,y,3)
# y2 = z[0]*x2**3 + z[1]*x2**2+z[2]*x2+z[3]
# spl = interpolate.UnivariateSpline(x,y,k=3)
# spl.set_smoothing_factor(1)
# fft = np.log(np.abs(np.fft.rfft(y)))
# freqs = np.linspace(0, 1.0/(2.0*T), 250)

f = [ 4.54756150e+02, -3.17306602e+03, -3.17683899e+03, -3.18061195e+03,
       -2.98815159e+03, -2.99169122e+03, -2.99523086e+03, -2.99877049e+03,
       -3.00231013e+03, -1.99664976e+03, -1.99898940e+03, -2.00132903e+03,
       -2.00366866e+03, -9.33733300e+02, -9.34797934e+02, -9.35862569e+02,
       -9.36927203e+02, -4.89458505e+02, -4.89989806e+02, -4.90521107e+02,
       -4.91052408e+02, -2.04242043e+02, -2.04431677e+02, -2.04621312e+02,
       -2.04810947e+02, -2.12008915e+02, -2.12206882e+02, -2.12404850e+02,
       -2.12602818e+02, -1.42717453e+02, -1.42832087e+02, -1.42946722e+02,
       -1.43061357e+02, -1.15142658e+02, -1.15223959e+02, -1.15305260e+02,
       -1.15386562e+02, -5.94011962e+01, -5.94158308e+01, -5.94304654e+01,
       -5.94451000e+01,  1.76319321e+01,  1.77089642e+01,  1.77859963e+01,
        1.78630283e+01, -3.08493958e+00, -3.03290750e+00, -2.98087542e+00,
       -1.15062177e+02, -1.15143478e+02, -1.15224779e+02, -1.15306080e+02,
       -1.15387382e+02, -6.64103496e+01, -6.64333175e+01, -6.64562854e+01,
       -6.64792533e+01, -1.57610555e+02, -1.57741856e+02, -1.57873157e+02,
       -1.58004458e+02,  5.21142404e+01,  5.22329392e+01,  5.23516379e+01,
        5.24703367e+01,  5.25890354e+01,  5.27077342e+01,  5.28264329e+01,
        5.29451317e+01,  1.30155497e+02,  1.30365863e+02,  1.30576228e+02,
        1.30786593e+02,  7.49302921e+01,  7.50739908e+01,  7.52176896e+01,
        7.53613883e+01, -8.59491292e+00, -8.55121417e+00, -8.50751542e+00,
       -8.46381667e+00, -1.54284512e+01, -1.53930858e+01, -1.53577204e+01,
       -1.53223550e+01, -2.93036562e+01, -2.92849575e+01, -2.92662587e+01,
       -2.92475600e+01, -7.12788612e+01, -7.13101625e+01, -7.13414637e+01,
       -7.13727650e+01,  2.67126004e+01,  2.67979658e+01,  2.68833313e+01,
        2.69686967e+01, -3.60209379e+01, -3.60105725e+01, -3.60002071e+01,
       -3.59898417e+01,  8.31621904e+01,  8.33142225e+01,  8.34662546e+01,
        8.36182867e+01, -2.83630146e+01, -2.83443158e+01, -2.83256171e+01,
       -2.83069183e+01, -1.12388220e+02, -1.12469521e+02, -1.12550822e+02,
       -1.12632123e+02, -1.26730091e+02, -1.26828059e+02, -1.26926027e+02,
       -1.27023995e+02, -7.10552962e+01, -7.10865975e+01, -7.11178987e+01,
        9.70508000e+01,  9.72194988e+01,  9.73881975e+01,  9.75568963e+01,
        9.77255950e+01,  7.68692938e+01,  7.70129925e+01,  7.71566913e+01,
        7.73003900e+01, -6.65591125e+00, -6.61221250e+00, -6.56851375e+00,
       -6.52481500e+00, -5.55394496e+01, -5.55540842e+01, -5.55687187e+01,
       -2.75500200e+01, -2.75313212e+01, -2.75126225e+01, -2.74939237e+01,
       -2.74752250e+01,  7.76684738e+01,  7.78121725e+01,  7.79558713e+01,
        8.01623667e+00,  8.07660208e+00,  8.13696750e+00,  8.19733292e+00,
        8.25769833e+00, -1.97152696e+01, -1.96882375e+01, -1.96612054e+01,
       -1.96341733e+01]

# x3 = np.arange(0,512,1)

# d_tau, d_tau_2, den = amdf_PE_2(y)

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
# ax2.set_title("X-axis displacement spline", fontsize=20)
# ax2.set_xlabel("Control points",fontsize=20)
# ax2.set_ylabel("Displacement from starting point A",fontsize=20)
# ax2.text(0.15,0,"A")
# ax2.text(1.15,-2,"B")
# ax2.text(2.15,12,"C")
# ax2.text(3.15,0,"A")
# ax2.text(4.15,-2,"B")
# ax2.text(5.15,12,"C")
# ax2.text(6.15,0,"A")
ax2.plot(f[3:40])
# ax2.plot(d_tau, color = 'r')
# ax3 = plt.twinx(ax2)
# ax2.plot(x,y, 'r')
# ax2.plot(x,y2, 'g')
# ax2.plot(x,y3, 'b')
# ax2.plot(x2,spl(x2), 'r')
# ax2.plot(den, color = 'k')
# ax2.vlines(200,-400,200)