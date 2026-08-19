"""
Interface Module
Manages data flow between sensors, math engines, 2D spatial slicing, and statisitcal evaluation
"""
import numpy as np
from Logic import FreezerMathBase


class FreezerSystem:
    def __init__(self, math_engine,grid_size=15):
        self.engine = math_engine #resolution of grid
        self.grid_size = grid_size
    

    def set_math_engine(self, new_engine):
        """allows swapping the math engine at runtime"""
        self.engine = new_engine
        

    def get_visuals(self,sensor_data,grid_size=None,z_slice = 0.5):
        """
        computes 3D volume and extracts 2D slice
        Uses instance grid size if none provided
        """
        if grid_size is None:
            grid_size = self.grid_size

        X,Y,Z,V = self.engine.compute_volume(sensor_data,grid_size)

        z_index = int(z_slice * (grid_size -1))
        grid_2d = V[z_index,:,:]

        return (X,Y,Z,V) , grid_2d
    
    def get_stats(self,sensor_data,X=None, Y=None, Z= None, V=None):
        """
        Calculates summary metrics
        """
        avg = sum(sensor_data) / len(sensor_data)
        if V is not None and X is not None:
            min_temp = float(np.min(V))
            max_temp = float(np.max(V))

            min_idx = np.unravel_index(np.argmin(V), V.shape)
            max_idx = np.unravel_index(np.argmax(V), V.shape)

            coldest_spot = (X[min_idx], Y[min_idx], Z[min_idx])
            warmest_spot = (X[max_idx],Y[max_idx],Z[max_idx])
            return (
                f"============================\n"
                f"       FREEZER REPORT       \n"
                f"============================\n"
                f"System mode: {self.engine.get_name()}\n"
                f"Average Temp: {avg:.2f}°C\n"
                f"Coldest Temp: {min_temp:.2f}°C at position (x={coldest_spot[0]:.2f}, y={coldest_spot[1]:.2f}, z={coldest_spot[2]:.2f})\n"
                f"Warmest Temp: {max_temp:.2f}°C at position (x={warmest_spot[0]:.2f},y={warmest_spot[1]:.2f},z={warmest_spot[2]:.2f})\n"
            )

        return f"System Mode: {self.engine.get_name()} | Avg Temp: {avg:.2f}°C"