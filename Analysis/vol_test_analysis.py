# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 12:28:18 2020

@author: byron
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
from scipy.signal import hilbert

# filenames = []
linear_input_whistles = [[5000,30000,60000,85000],[6500,25000,65000,75000],[5000,30000,58000,85000]]
log_input_whistles = [[5000,37500,68000,90000],[5000,33000,70000,94000],[6700,35000,76000,104000]]
linear_output_whistles = [[640,6000,54000,60000],[4000,7000,62000,68000],[4000,7500,39700,44000]]
log_output_whistles = [[3400,11000,60990,68000],[2093,5500,52200,55800],[1000,6000,58400,65000]
in_filename = 'vol_test_{}_output.wav'
for i in range(1,4):    
    f, in_audio = wav.read(in_filename.format(str(i)),mmap=False)
# in_audio = in_audio.astype(np.float32)
# in_audio /= np.max(in_audio)
# in_audio = np.fromfile(in_filename, np.float16)
# in_audio_scaled = in_audio+np.min(in_audio)
# in_audio_scaled = 20*np.log10(np.abs(in_audio+0.1))

# whistle = in_audio_scaled[5000:30000]
# db_vals = whistle > -60
# db_mean = np.mean(whistle[db_vals])
# env = -np.abs(hilbert(whistle[db_vals]))
    fig,ax = plt.subplots()
    ax.plot(in_audio)
# plt.plot(env)
# plt.vlines([5000,32000,60000, 85000], -90,0)