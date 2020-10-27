# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 13:40:26 2020

@author: byron
"""

import numpy as np
import matplotlib.pyplot as plt

freqs = [630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 639.1304347826087, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 639.1304347826087, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 639.1304347826087, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0, 630.0]

with open("key_freq_list.txt", 'r') as kfile:
    key_freq_list = np.genfromtxt(kfile)
    
with open("key_name_list.txt", 'r') as nfile:
    key_name_list = [word.strip(",") for line in nfile for word in line.split()]

half_points = []
for i in range(len(key_freq_list)-1):
    half_points.append((key_freq_list[i]+key_freq_list[i+1])/2)


for i,f_center in enumerate(key_freq_list[1:-1]):
    print(i)
    temp_freqs = freqs[i*48:(i+1)*48]
    plt.hist(freqs, bins = 9)
    plt.title("AMDF accuracy test ({})".format(key_name_list[i]))
    plt.vlines(x=[half_points[i], half_points[i+1]], ymin = 0, ymax = 22)
    plt.text(half_points[i], 25, "Threshold at {} Hz".format(half_points[i]))
    plt.text(half_points[i+1], 30, "Threshold at {} Hz".format(half_points[i+1]))
    plt.text(f_center,23, "Target key frequency at {} Hz".format(f_center))
    plt.vlines(x=f_center, ymin = 0 ,ymax = 22, colors='red')
    plt.savefig("AMDF_Accuracy_results/key_{}.png".format(key_name_list[i]))
    plt.close()
    

