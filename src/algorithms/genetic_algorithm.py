import random
from typing import List
from cube.magic_cube import MagicCube
from cube.obj_function import ObjectiveFunction

class GeneticAlgorithmMagicCube:
    def __init__(self, population_size=50, mutation_rate=0.1, generations=200, best_individuals=2, restart_interval=50):
        """
        Inisialisasi algoritma genetika dengan parameter yang diberikan.

        Parameters:
        - population_size: Jumlah individu dalam populasi
        - mutation_rate: Tingkat mutasi yang diterapkan pada setiap individu
        - generations: Jumlah maksimum generasi untuk dijalankan
        - best_individuals: Jumlah individu terbaik yang dipertahankan setiap generasi
        - restart_interval: Interval generasi untuk melakukan restart populasi parsial
        """
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.generations = generations
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
        return ObjectiveFunction(state).objective_function()

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

    def search(self) -> MagicCube:
        """
                Menjalankan algoritma genetika untuk mencari solusi optimal.

                Returns:
                MagicCube: Solusi terbaik yang ditemukan setelah seluruh generasi
        """
        best_score = float('inf')
        for generation in range(self.generations):
            if generation % self.restart_interval == 0 and generation > 0:
                print(f"Restarting a portion of the population at generation {generation}")
                self.population = self.startInit()[:self.population_size // 2] + self.population[self.population_size // 2:]

            current_best = self.findBestSolution(self.population)
            current_score = self.evaluateState(current_best)
            self.objective_function_values.append(current_score)

            # Log dan perbarui best_score
            print(f"Generasi {generation}: Evaluasi terbaik = {current_score}")
            if current_score < best_score:
                best_score = current_score

            # Penghentian jika mencapai skor optimal (315)
            if best_score == 315:
                print("Solusi optimal ditemukan dengan nilai 315.")
                return current_best

            # Perbarui populasi
            self.population = self.generateNextGeneration(self.population)

        return self.findBestSolution(self.population)
