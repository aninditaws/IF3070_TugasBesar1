import random
import time
import matplotlib.pyplot as plt
from typing import List
from cube.magic_cube import MagicCube

class GeneticAlgorithmMagicCube:
    def __init__(self, population_size=50, mutation_rate=0.1, iterations=200, best_individuals=2, restart_interval=50):
        """
        Inisialisasi algoritma genetika dengan parameter yang diberikan.

        Parameters:
        - population_size: Jumlah individu dalam populasi
        - mutation_rate: Tingkat mutasi yang diterapkan pada setiap individu
        - iterations: Jumlah maksimum generasi untuk dijalankan
        - best_individuals: Jumlah individu terbaik yang dipertahankan setiap generasi
        - restart_interval: Interval generasi untuk melakukan restart populasi parsial
        """
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.iterations = iterations
        self.best_individuals = best_individuals
        self.restart_interval = restart_interval
        self.population = self.startInit()  # Inisialisasi populasi awal
        self.objective_function_values = []  # Menyimpan nilai objective function per generasi

    def startInit(self) -> List[MagicCube]:
        """
        Menginisialisasi populasi awal dengan sejumlah Magic Cube acak.

        Returns:
        List of MagicCube: Daftar individu dalam populasi awal
        """
        return [MagicCube(size=5) for _ in range(self.population_size)]

    def evaluateState(self, state: MagicCube) -> float:
        """
        Mengevaluasi kualitas sebuah Magic Cube menggunakan objective function.

        Parameters:
        - state: MagicCube yang akan dievaluasi

        Returns:
        float: Nilai skor evaluasi; semakin rendah semakin baik
        """
        return state.objective_function()

    def selectParents(self, population: List[MagicCube]) -> List[MagicCube]:
        """
        Memilih dua individu dari populasi sebagai induk menggunakan metode turnamen.

        Parameters:
        - population: Daftar individu dalam populasi

        Returns:
        List[MagicCube]: Dua individu terpilih sebagai induk
        """
        tournament = random.sample(population, 10)  # Mengambil sampel 10 individu untuk turnamen
        tournament.sort(key=lambda ind: self.evaluateState(ind))
        return tournament[:2]  # Mengembalikan dua individu terbaik dari turnamen

    def crossover(self, parent1: MagicCube, parent2: MagicCube) -> MagicCube:
        """
                Melakukan crossover antara dua induk untuk menghasilkan keturunan baru.

                Parameters:
                - parent1: MagicCube pertama
                - parent2: MagicCube kedua

                Returns:
                MagicCube: Keturunan baru hasil crossover
        """
        child = MagicCube(size=5)
        for i in range(5):
            for j in range(5):
                for k in range(5):
                    child.cube[i][j][k] = parent1.cube[i][j][k] if random.random() < 0.5 else parent2.cube[i][j][k]
        return child

    def mutate(self, individual: MagicCube):
        """
                Melakukan mutasi pada MagicCube dengan menukar dua elemen acak.

                Parameters:
                - individual: MagicCube yang akan dimutasi
        """
        if random.random() < self.mutation_rate:
            i1, j1, k1 = [random.randint(0, 4) for _ in range(3)]
            i2, j2, k2 = [random.randint(0, 4) for _ in range(3)]
            individual.cube[i1][j1][k1], individual.cube[i2][j2][k2] = individual.cube[i2][j2][k2], individual.cube[i1][j1][k1]

    def generateNextGeneration(self, population: List[MagicCube]) -> List[MagicCube]:
        """
               Menghasilkan generasi baru dengan menggunakan seleksi, crossover, dan mutasi.

               Parameters:
               - population: Daftar individu dalam populasi saat ini

               Returns:
               List[MagicCube]: Populasi baru yang dihasilkan
        """
        new_population = []
        best_individuals = sorted(population, key=lambda ind: self.evaluateState(ind))[:self.best_individuals]
        new_population.extend(best_individuals)

        while len(new_population) < self.population_size:
            parent1, parent2 = self.selectParents(population)
            child = self.crossover(parent1, parent2)
            self.mutate(child)
            new_population.append(child)

        return new_population

    def findBestSolution(self, population: List[MagicCube]) -> MagicCube:
        """
                Menemukan individu terbaik dalam populasi berdasarkan nilai evaluasi.

                Parameters:
                - population: Daftar individu dalam populasi

                Returns:
                MagicCube: Individu terbaik dalam populasi
        """
        return min(population, key=lambda ind: self.evaluateState(ind))

    def run(self) -> MagicCube:
        """
                Menjalankan algoritma genetika untuk mencari solusi optimal.

                Returns:
                MagicCube: Solusi terbaik yang ditemukan setelah seluruh generasi
        """
        best_score = float('inf')
        initial_score = self.population[0].objective_function()

        start_time = time.time()
        for iteration in range(self.iterations):
            if iteration % self.restart_interval == 0 and iteration > 0:
                self.population = self.startInit()[:self.population_size // 2] + self.population[
                                                                                 self.population_size // 2:]

            current_best = self.findBestSolution(self.population)
            current_score = self.evaluateState(current_best)
            self.objective_function_values.append(current_score)

            if current_score < best_score:
                best_score = current_score
                print(f"Iteration {iteration}: Best Evaluation = {best_score}")
            if best_score == 315:
                print("Optimal solution with score 315 found.")
                break

            self.population = self.generateNextGeneration(self.population)

        end_time = time.time()

        # Plot objective function progression
        plt.figure(figsize=(10, 6))
        plt.plot(self.objective_function_values, label="Objective Score per Iteration")
        plt.xlabel("Iteration")
        plt.ylabel("Objective Score")
        plt.title(
            f"Objective Function Progression (Population: {self.population_size}, Iteration: {self.iterations})")
        plt.legend()
        plt.show()

        return initial_score, best_score, end_time - start_time