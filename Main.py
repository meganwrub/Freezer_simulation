"""
Main execution module for freezer simulation 
Generates 2D and 3D visual heat Maps
"""

import matplotlib.pyplot as plt
from Logic import TrilinearMath
from Interface import FreezerSystem

DATASETS = {
    "Normal_freezer": [-20,-17,-16,-15,-23,-21,-19,-14],
    "Warm_freezer": [-20,-19,-5,-3,-16,-15,0,2],
    "uniform_cold": [-18,-18,-18,-18,-18,-18,-18,-18],
    "simple_numbers": [10,20,30,0,10,20,40,0]
}


def main():

    sensor_data = DATASETS["simple_numbers"]

    math_engine = TrilinearMath()
    freezer = FreezerSystem(math_engine=math_engine,grid_size=15)

    (X,Y,Z,V), grid_2D = freezer.get_visuals(sensor_data, z_slice=0.5)

    print(freezer.get_stats(sensor_data,X,Y,Z, V))

    fig=plt.figure(figsize=(14,6))

    #2D heat map slice
    ax1 = fig.add_subplot(1,2,1)
    im1 = ax1.imshow(grid_2D, cmap='RdYlBu_r', origin='lower', extent = [0,1,0,1])
    plt.colorbar(im1,ax=ax1,label='Temperature (Celcius)')
    ax1.set_title("2D Heat Map (Middle slice: z= 0.5)")
    ax1.set_xlabel("Width")
    ax1.set_ylabel("Depth")

    #3D Temperature cloud
    ax2 = fig.add_subplot(1,2,2,projection='3d')
    scatter = ax2.scatter(X,Y,Z,c=V.flatten(), cmap='RdYlBu_r', s=25,alpha=0.35)

    plt.colorbar(scatter,ax=ax2,label='Temperature (Celcius)')
    ax2.set_title("3D Freezer Volume Cloud")
    ax2.set_xlabel("Width")
    ax2.set_ylabel("Depth")
    ax2.set_zlabel("Height")
    plt.tight_layout()
    plt.show()

if __name__ =="__main__":
    main()
