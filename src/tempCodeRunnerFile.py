
# magic_cube = MagicCube(size)
# steepest_initial_score = magic_cube.objective_function()
# print("\nFirst state of magic cube:")
# magic_cube.display()
# steepest_hill = SteepestHillClimbing(magic_cube)
# steepest_final_score, steepest_move_duration = steepest_hill.run(max_iterations)
# print("\nState of magic cube after Steepest Hill Climbing:")
# magic_cube.display()
# algorithms.append(
#     {
#         "algorithm": "Steepest Hill Climbing",
#         "initial_score": steepest_initial_score,
#         "final_score": steepest_final_score,
#         "delta": steepest_initial_score - steepest_final_score,
#         "duration": steepest_move_duration
#     }
# )

# print("\n=== Running Sideways Move Hill Climbing ===")
# magic_cube = MagicCube(size)
# sideways_initial_score = magic_cube.objective_function()
# print("\nFirst state of magic cube:")
# magic_cube.display()
# sideways_climber = SidewaysMove(magic_cube)
# sideways_final_score, sideways_move_duration = sideways_climber.run(max_iterations, max_sideways_iteration)
# print("\nState of magic cube after Sideways Move Hill Climbing:")
# magic_cube.display()
# algorithms.append(
#     {
#         "algorithm": "Sideways Move Hill Climbing",
#         "initial_score": sideways_initial_score,
#         "final_score": sideways_final_score,
#         "delta": sideways_initial_score - sideways_final_score,
#         "duration": sideways_move_duration
#     }
# )