import random

class MagicCube:
    def __init__(self, size=5):
        self.size = size
        self.cube = [[[0 for _ in range(size)] for _ in range(size)] for _ in range(size)]
        self.initialize_random_state()
        self.magic_number = self.calculate_magic_number()

    def initialize_random_state(self):
        numbers = list(range(1, self.size ** 3 + 1))
        random.shuffle(numbers)
        
        index = 0
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    self.cube[i][j][k] = numbers[index]
                    index += 1

    def calculate_magic_number(self):
        return (self.size * (self.size ** 3 + 1)) // 2

    def heuristic_value(self):
        score = 0
        
        # Check sums of rows, columns, and pillars for each layer
        for i in range(self.size):
            for j in range(self.size):
                row_sum = sum(self.cube[i][j][k] for k in range(self.size))
                score += abs(row_sum - self.magic_number)

                col_sum = sum(self.cube[i][k][j] for k in range(self.size))
                score += abs(col_sum - self.magic_number)

                pillar_sum = sum(self.cube[k][i][j] for k in range(self.size))
                score += abs(pillar_sum - self.magic_number)

        # Main space diagonals
        diag1_sum = sum(self.cube[i][i][i] for i in range(self.size))
        diag2_sum = sum(self.cube[i][i][self.size - i - 1] for i in range(self.size))
        diag3_sum = sum(self.cube[i][self.size - i - 1][i] for i in range(self.size))
        diag4_sum = sum(self.cube[self.size - i - 1][i][i] for i in range(self.size))
        
        score += abs(diag1_sum - self.magic_number)
        score += abs(diag2_sum - self.magic_number)
        score += abs(diag3_sum - self.magic_number)
        score += abs(diag4_sum - self.magic_number)

        # 2D slice diagonals in each dimension
        for i in range(self.size):
            diag1_xy = sum(self.cube[i][j][j] for j in range(self.size))
            diag2_xy = sum(self.cube[i][j][self.size - j - 1] for j in range(self.size))
            score += abs(diag1_xy - self.magic_number)
            score += abs(diag2_xy - self.magic_number)

            diag1_yz = sum(self.cube[j][i][j] for j in range(self.size))
            diag2_yz = sum(self.cube[self.size - j - 1][i][j] for j in range(self.size))
            score += abs(diag1_yz - self.magic_number)
            score += abs(diag2_yz - self.magic_number)

            diag1_xz = sum(self.cube[j][j][i] for j in range(self.size))
            diag2_xz = sum(self.cube[j][self.size - j - 1][i] for j in range(self.size))
            score += abs(diag1_xz - self.magic_number)
            score += abs(diag2_xz - self.magic_number)

        return score

    def display(self):
        for layer in range(self.size):
            print(f"Layer {layer + 1}:")
            for element in self.cube[layer]:
                print(" ".join(f"{num:3}" for num in element))
            print("\n" + "-" * 25 + "\n")
