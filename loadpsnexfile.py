#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 18:07:01 2024

@author: yogehs
"""
import os
from parsepsnexheader import parsePSNEXheader, parsePSNEXsegmentheader
from nptdms import TdmsFile

def loadPSNEXfile(filepath, UFF):
    """
    Function used to load the metadata of a PS_nex file.

            Parameters:
                    filepath (str): Path to the PS_nex file.
                    UFF (uff.UFF): UFF object to load the metadata into.
            
            Returns:
                    UFF (uff.UFF): UFF object containing the loaded metadata.
    """
    UFF.filemetadata = parsePSNEXheader(filepath)
    UFF.isFV = UFF.filemetadata["mapping_bool"]
    #key for the channel of ht and defleciton

    UFF.filemetadata['found_vDeflection'] = True
    UFF.filemetadata['height_channel_key'] = "Zpiezo stage (V)"
    UFF.filemetadata['deflection_chanel_key'] = "Deflection (V)"
    curve_properties = {}

    curve_indices =  UFF.filemetadata["number_consecutive_scans"] 

    index = 1 if curve_indices == 0 else 3

    for i in range( UFF.filemetadata["num_segments"] ):
        if index == 3:
            #curve_id = segment_group[0].split("/")[1]
            curve_id =  UFF.filemetadata["curve_id"] 
        else:
            curve_id = '0'
        segment_id = i
        if not curve_id in curve_properties.keys():
            curve_properties.update({curve_id:{}})

        curve_properties = parsePSNEXsegmentheader(filepath,curve_properties, segment_id,curve_id )

    UFF.filemetadata['curve_properties'] = curve_properties

    return UFF


    