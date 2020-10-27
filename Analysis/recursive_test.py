# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 09:35:42 2020

@author: byron
"""

import numpy as np
import matplotlib.pyplot as plt
from itertools import groupby

# def key_time(keys_arr):
#     global time, keys_out
#     key_counter = 0
#     for i in range(len(keys_arr)):
#         print("Index counter: {}".format(i))
#         if keys_arr[i] == keys_arr[i+1]:
#             curr_key = keys_arr[i]
#             key_counter += 2
#         else:
#             if keys_arr[i+2] == keys_arr[i]:
#                 curr_key = keys_arr[i]
#                 key_counter += 2
#             elif (key_counter == 0):
#                 pass
#             else:
#                 print("Key {} time ended".format(curr_key))
#                 time.append(key_counter*0.0625)
#                 keys_out.append(curr_key)
#                 key_time(keys_arr[i+1:])

def key_time2(keys_arr):
    global time, keys_out, curr_key_i, curr_key_time, next_key_i, out_key, out_key_list
    curr_key_i = 0
    next_key_i = 1
    if keys_arr[curr_key_i] == keys_arr[next_key_i]:
        out_key = keys_arr[curr_key_i]
        curr_key_time =+ 0.0625*2
        curr_key_i = next_key_i 
        next_key_i += 1
        # print("Case 1: Current and next equal \n curr_i: {} \t next_i: {}".format(curr_key_i,next_key_i))
        # print("1. New keys_arr: {}".format(keys_arr[curr_key_i:]))
        try:
            key_time2(keys_arr[curr_key_i:])
        except IndexError:
            # print("End of key list")
            out_key_list.append(out_key)
            time.append(curr_key_time)
    else:
        if keys_arr[curr_key_i] == keys_arr[next_key_i+1]:
            
            out_key = keys_arr[curr_key_i]
            curr_key_time += 0.0625*3
            curr_key_i = next_key_i+1
            next_key_i += ((next_key_i+1)+1)
            # print("Case 2: Current and next + 1 equal \n curr_i: {} \t next_i: {}".format(curr_key_i,next_key_i))
            # print("2. New keys_arr: {}".format(keys_arr[curr_key_i:]))
            try:
                key_time2(keys_arr[curr_key_i:])
            except IndexError:
                # print("End of key list")
                out_key_list.append(out_key)
                time.append(curr_key_time)
        else:
            if curr_key_time !=0:
                
                out_key_list.append(out_key)
                time.append(curr_key_time)
                curr_key_time = 0.0
                curr_key_i = next_key_i
                next_key_i += 1
                # print("Case 3: End time for key: {}".format(keys_arr[curr_key_i-1]))
                # print("3. New keys_arr: {}".format(keys_arr[curr_key_i:]))
                try:
                    key_time2(keys_arr[curr_key_i:])
                except IndexError:
                    # print("End of key list")
                    out_key_list.append(out_key)
                    time.append(curr_key_time)
            else:
                curr_key_i = next_key_i
                next_key_i += 1
                try:
                     key_time2(keys_arr[curr_key_i:])
                except IndexError:
                    # print("End of key list")
                    out_key_list.append(out_key)
                    time.append(curr_key_time)
    
                
key_list = [15.0, 17.0, 18.0, 20.0, 22.0, 23.0, 22.0, 21.0, 18.0, 18.0, 18.0, 18.0, 
            19.0, 19.0, 20.0, 20.0, 19.0, 19.0, 19.0, 19.0, 17.0, 16.0, 17.0, 17.0, 
            17.0, 19.0, 20.0, 21.0, 21.0, 21.0, 20.0, 19.0, 15.0, 15.0, 15.0, 15.0, 
            19.0, 19.0, 19.0, 19.0, 16.0, 15.0, 15.0, 15.0, 15.0, 16.0, 17.0, 18.0]
time = []
out_key_list = []
curr_key_i = 0
next_key_i = 1
curr_key_time = 0.0
key_time2(key_list)


count_dups = [sum(1 for _ in group) for _, group in groupby(key_list)]
# key_time(key_list)
print(time, out_key_list)


# print(count_dups)
                