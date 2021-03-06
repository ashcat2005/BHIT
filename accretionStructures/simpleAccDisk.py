#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 23:16:05 2018

@author: ashcat
"""

import numpy as np 

class Disk:
    def __init__(self, rData, R_in = 2., R_out = 4. ):
        self.rData = rData
        self.Shape = np.shape(self.rData)
        self.R_out = R_out*np.ones(self.Shape)
        self.R_in = R_in*np.ones(self.Shape)
        self.image = 1*(self.R_in <= self.rData) * (self.rData <= self.R_out)

