from cube.magic_cube import MagicCube
from cube.obj_function import ObjectiveFunction

magic_cube = MagicCube(size=5)
objective_func = ObjectiveFunction(magic_cube)
print("MN:", objective_func.calculate_magic_number())
print("Initial objective score:", objective_func.objective_function(), "\n")
magic_cube.display()
