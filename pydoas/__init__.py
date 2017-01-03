# -*- coding: utf-8 -*-
"""
Initiation of pydoas library

.. moduleauthor:: Jonas Gliß <jg@nilu.no>

.. todo:
    
    Future ideas:
    
    #. Spectral results and Analysis (:mod:analysis`)
        1. Currently only DOASIS resultfile support
        #. Include "scans" (e.g. for MAX DOAS measurements)
            1. Defined by Start/Stop of individual FitResultFiles
        #. Convenience functionality for scans
            #. All scans in time interval
            #. All data with species X (e.g. SO2) larger / smaller than thresh 
            (e.g. 1E+18 cm-2)
        #. Plotting
            1. Diurnal profiles (e.g. BrO/SO2)
            #. Individual scans (data vs. Elevation / Azimuth /plume age)
                1. Plume cross section 
                #. Plume evolution
            #. Standard time series plotting
            #. Scatter plot
                1. start, stop
                # additional conditioning (e.g. SO2 > ..., plume age > ..., 
                above detection limit)
            
        #. Include more input routines for reading results :class:`SpectralResults`
            1. csv, txt, etc..
            #. Autoidentify data and start, stop
        
    #. UNCERTAINTY treatment
       
"""
#==============================================================================
# import os, so2cam
# moduleBasePath=os.path.dirname(so2cam.__file__)
#==============================================================================
from os.path import abspath, dirname

_LIBDIR = abspath(dirname(__file__))

from .inout import *  #from .io import get_data_dirs, get_data_files
import dataimport
import analysis

