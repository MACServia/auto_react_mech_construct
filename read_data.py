#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:33:24 2024

@author: md1621
"""

import numpy as np
import pandas as pd
import os

# Function that reads files from a directory and returns a dictionary
def read_files(directory):
    files = os.listdir(directory)
    data = {}

    for file in files:
        if not file.startswith('.'):
            data[file[:-4]] = pd.read_csv(os.path.join(directory, file), 
                                          header = 0, index_col = None,
                                          encoding = 'latin1').values
    return data

place_holder = read_files("exp_data_fruc_HMF")

def reverse_dict(original_dict):
    reversed_dict = {key: original_dict[key] for key in reversed(original_dict)}
    return reversed_dict

in_silico_data = reverse_dict(place_holder)

# This takes the first column from each entry of the dictionary and puts it into another dictionary
initial_conditions = {}
for key, value in in_silico_data.items():
    aa = "ic_" + key[-1]
    initial_conditions[aa] = value[0]

num_exp = len(initial_conditions)
timesteps = 30
time = np.linspace(0, 2, timesteps)
t = [0, np.max(time)]
t_eval = list(time)