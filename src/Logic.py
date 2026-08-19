"""
Logic module - Multivariable Math engine for a walk in freezer with 8 sensors
this module implements 3D trilinear interpolation to estimate tempersture distributions
accross a continous bolume from 8 corner sensors
"""

import numpy as np

class FreezerMathBase:
    def compute_volume(self,temps,grid_size):
        raise NotImplementedError("Subclasses must implement compute_volme!")
    def get_name(self):
        return "Base engine"

class TrilinearMath(FreezerMathBase):

    def compute_volume(self,temps,grid_size):

        axis = np.linspace(0,1,grid_size)
        X,Y,Z = np.meshgrid(axis,axis,axis)

        t000,t100,t010,t110,t001,t101,t011,t111 = temps

        #round 1: Width (X)
        t00=t000*(1-X) + t100*X
        t01 = t001 * (1-X) + t101*X
        t10 = t010 * (1-X) + t110*X
        t11 = t011 * (1-X) + t111*X

        #round 2: Depth (Y)
        t0 = t00 *(1-Y) + t10 * Y
        t1 = t01 *(1-Y) +t11*Y

        #round 3: Height (Z)
        V = t0 *(1-Z) +t1*Z

        return X,Y,Z,V
    
    def get_name(self):
        return "Triliner Interpolation"