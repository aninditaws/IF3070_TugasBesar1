from cube.magic_cube import MagicCube
from cube.magic_cube import MagicCube
from algorithms.steepest_hill_climbing import SteepestHillClimbing

magic_cube = MagicCube(size=5)
print("Magic number:", magic_cube.magic_number)
print("Initial objective score:", magic_cube.heuristic_value())
hill_climber = SteepestHillClimbing(magic_cube)
hill_climber.run(max_iterations=10)