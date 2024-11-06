import sys
import time
import matplotlib.pyplot as plt
from cube.magic_cube import MagicCube
from cube.obj_function import ObjectiveFunction
from algorithm.genetic_algorithm import GeneticAlgorithmMagicCube
# from algorithm.simulated_annealing import SimulatedAnnealingMagicCube
# from algorithm.steepest_hill_climbing import HillClimbingMagicCube

def initialize_magic_cube():
    # Inisialisasi Magic Cube dan Objective Function
    magic_cube = MagicCube(size=5)
    objective_func = ObjectiveFunction(magic_cube)

    # Menampilkan Magic Number dan nilai objektif awal dari Magic Cube
    print("Magic Number:", objective_func.calculate_magic_number())
    print("Initial Objective Score:", objective_func.objective_function(), "\n")

    # Menampilkan susunan awal kubus
    print("Initial Magic Cube:")
    magic_cube.display()

    return magic_cube, objective_func

def run_genetic_algorithm(population_size, generations):
    print("\nMemulai Genetic Algorithm...\n")

    # Inisialisasi genetic algorithm dengan parameter tertentu
    ga = GeneticAlgorithmMagicCube(population_size=population_size, mutation_rate=0.1, generations=generations)

    # Mulai pencatatan waktu
    start_time = time.time()
    best_solution = ga.search()
    end_time = time.time()

    # Durasi proses pencarian
    duration = end_time - start_time

    # Evaluasi solusi terbaik yang ditemukan
    best_objective_func = ObjectiveFunction(best_solution)
    final_score = best_objective_func.objective_function()
    print("\nSolusi terbaik Genetic Algorithm:")
    print("Objective Score Terbaik:", final_score)
    print("Durasi Proses Pencarian (detik):", duration)
    print("Final Magic Cube:")
    best_solution.display()

    # Plot nilai objective function terhadap generasi
    plt.figure(figsize=(10, 6))
    plt.plot(ga.objective_function_values, label="Objective Score per Generation")
    plt.xlabel("Generation")
    plt.ylabel("Objective Score")
    plt.title(f"Objective Function Progression (Population: {population_size}, Generations: {generations})")
    plt.legend()
    plt.show()

    return {
        "initial_state": ga.population[0],  # Menyimpan state awal dari salah satu individu
        "final_state": best_solution,
        "final_score": final_score,
        "duration": duration,
        "objective_function_values": ga.objective_function_values
    }

# def run_simulated_annealing():

# def run_hill_climbing():

if __name__ == "__main__":
    # Menampilkan Magic Cube awal
    magic_cube, objective_func = initialize_magic_cube()

    # Memilih algoritma yang akan dijalankan berdasarkan input pengguna
    print("\nPilih algoritma yang ingin digunakan:")
    print("1. Genetic Algorithm")
    print("2. Simulated Annealing")
    print("3. Hill Climbing")

    choice = input("Masukkan nomor algoritma yang ingin digunakan: ")

    if choice == '1':
        population_size = int(input("Masukkan jumlah populasi: "))
        generations = int(input("Masukkan banyak iterasi (generasi): "))
        results = run_genetic_algorithm(population_size, generations)
    # elif choice == '2':
    #     run_simulated_annealing()
    # elif choice == '3':
    #     run_hill_climbing()
    else:
        print("ERROR! Masukkan angka algoritma yang benar.")
        sys.exit(1)
