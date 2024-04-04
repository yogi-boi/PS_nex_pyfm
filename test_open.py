#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 18:17:24 2024

@author: yogehs
"""

from loadpsnexcurve import loadPSNEXcurve
from loadpsnexfile import loadPSNEXfile

from pyfmreader.uff import UFF
import os 
import matplotlib.pyplot as plt 


#%%find the files  
def find_all_PSnexfiles(directory = None):
    '''
    input folder path of day's experiment,
    return 
    '''
    all_PSnexfiles = []

    assert os.path.isdir(directory)
    for cur_path, directories, files in os.walk(directory):
        all_PSnexfiles+= [os.path.join(directory, cur_path, f) for f in files if f.endswith('.tdms')]#glob.glob('./*.jpk-force-map')
         
    return all_PSnexfiles

#load the example file 
file_path = '/Users/yogehs/Documents/ATIP_PhD/PS_nex/PS_nex_pyfm/PS_nex_pyfm/example/Fz_Vapp_002501_Vret_007502_20240313_160832.903_000.tdms'
#%%load the UFF object 

uffobj = UFF()
load_file = loadPSNEXfile(file_path, uffobj)
FC = loadPSNEXcurve(load_file.filemetadata)
height_channel_key = load_file.filemetadata['height_channel_key']
FC.preprocess_force_curve(load_file.filemetadata['invOLS_(nm/V)'],height_channel_key )

for _, segment in FC.get_segments():
    segment_data = segment
    print(segment_data.segment_type)
    plt.scatter(segment_data.zheight,segment_data.vdeflection,label = segment_data.segment_type)
    plt.xlabel("Z height ")
    plt.ylabel("deflection signal ")
plt.legend()