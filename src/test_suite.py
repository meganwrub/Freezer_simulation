
import numpy as np
from Logic import TrilinearMath
from Interface import FreezerSystem


DATASETS = {
    "Normal_freezer": [-20,-17,-16,-15,-23,-21,-19,-14],
    "Warm_freezer": [-20,-19,-5,-3,-16,-15,0,2],
    "uniform_cold": [-18,-18,-18,-18,-18,-18,-18,-18],
    "simple_numbers": [10,20,30,0,10,20,40,0]
}

def run_tests():
    print("Running Automated freezer tests...")
    engine = TrilinearMath()
    system = FreezerSystem(math_engine=engine, grid_size=3)

    #Test 1: Center point symmetry check
    temps = DATASETS["simple_numbers"]
    (X,Y,Z,V), grid_2D = system.get_visuals(temps,grid_size=3,z_slice=0.5)

    expected_center = sum(temps)/8
    actual_center = V[1,1,1] #middle of 3x3 grid

    assert np.isclose(actual_center,expected_center), (f"Test 1 failed. Expected center {expected_center}, got {actual_center}")

    print("Test one passed grid center is correct")

    #test 2: Uniform temperature check
    temps_uniform = DATASETS["uniform_cold"]
    (X,Y,X,V_uniform), _ = system.get_visuals(temps_uniform,grid_size=5)

    assert np.allclose(V_uniform,-18), "Test 2 failed"
    print("Test 2 passed: Uniform freezer readings maintain uniform volume")

    #Test 3: output bounds check
    door_temps = DATASETS["Warm_freezer"]
    (X,Y,Z,V_door),_ = system.get_visuals(door_temps, grid_size=10)

    assert np.min(V_door) >= min(door_temps), "test 3 failed: minimum out of bounds"
    assert np.max(V_door) <= max(door_temps), "test 3 failed: maximum out of bounds"
    print("\ntest 3 passed")

    print("\n all 3 tests passed successfully")

if __name__ == "__main__":
    run_tests()