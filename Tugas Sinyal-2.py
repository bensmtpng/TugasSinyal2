# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 11:19:32 2023

@author: Benny Simatupang
"""

import numpy as np

print("Nama: Benny Simatupang")
print("NRP: 5009211051")

def convolve_1d(signal1, signal2):
    len_signal1 = len(signal1)
    len_signal2 = len(signal2)
    
    result = [0] * (len_signal1 + len_signal2 - 1)
    
    for i in range(len_signal1):
        for j in range(len_signal2):
            result[i + j] += signal1[i] * signal2[j]
    
    return result

signal1 = [1, 2, 3, 4]
signal2 = [0.5, 0.25, 0.1]
result = convolve_1d(signal1, signal2)

numpy_result = np.convolve(signal1, signal2, mode='full')

print("Convolution result (custom implementation):", result)
print("Convolution result (NumPy):", numpy_result.tolist())

if np.allclose(result, numpy_result):
    print("Custom implementation matches NumPy result.")
else:
    print("Custom implementation does not match NumPy result.")
