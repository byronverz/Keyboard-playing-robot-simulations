# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 13:40:26 2020

@author: byron
"""

import numpy as np
import matplotlib.pyplot as plt

with open("out_freq_list.csv", 'r') as freq_file:
    freqs = np.genfromtxt(freq_file)

with open("key_freq_list.txt", 'r') as kfile:
    key_freq_list = np.genfromtxt(kfile)
    
with open("key_name_list.txt", 'r') as nfile:
    key_name_list = [word.strip(",") for line in nfile for word in line.split()]

half_points = []
for i in range(len(key_freq_list)-1):
    half_points.append((key_freq_list[i]+key_freq_list[i+1])/2)


# for i,f_center in enumerate(key_freq_list[1:-1]):
#     print(i)
#     temp_freqs = freqs[i*48:(i+1)*48]
#     plt.hist(temp_freqs, bins = 9)
#     plt.title("AMDF accuracy test ({})".format(key_name_list[i]))
#     plt.xlabel("Frequency (Hz)")
#     plt.ylabel(("Number of frequency classifications per bin"))
#     plt.vlines(x=[half_points[i], half_points[i+1]], ymin = 0, ymax = 22)
#     plt.text(half_points[i], 25, "Threshold at \n{} Hz".format(int(half_points[i])),
#              horizontalalignment="center",verticalalignment="center", color='k')
#     plt.text(half_points[i+1], 25, "Threshold at \n{} Hz".format(int(half_points[i+1])),
#              horizontalalignment="center",verticalalignment="center",color='k')
#     plt.text(f_center,25, "Target key frequency at \n{} Hz".format(int(f_center)),
#              horizontalalignment="center",verticalalignment="center", color = 'r')
#     plt.vlines(x=f_center, ymin = 0 ,ymax = 22, colors='red')
#     plt.savefig("AMDF_Accuracy_results/key_{}.png".format(key_name_list[i]))
#     plt.close()
    
plt.plot(freqs)
for f in key_freq_list[1:-1]:
    plt.axhline(f, color='r')

