class ObjectiveFunction:
    def __init__(self, cube):
        self.cube = cube.cube  # Access the actual 3D list from the MagicCube instance
        self.size = cube.size
        self.magic_number = self.calculate_magic_number()

    def calculate_magic_number(self):
        return (self.size * (self.size ** 3 + 1)) // 2

    def objective_function(self):
        score = 0
        
        # Check sums of rows, columns, and pillars for each layer
        for i in range(self.size):
            for j in range(self.size):
                # Sum for rows
                row_sum = sum(self.cube[i][j][k] for k in range(self.size))
                score += abs(row_sum - self.magic_number)

                # Sum for columns
                col_sum = sum(self.cube[i][k][j] for k in range(self.size))
                score += abs(col_sum - self.magic_number)

                # Sum for pillars
                pillar_sum = sum(self.cube[k][i][j] for k in range(self.size))
                score += abs(pillar_sum - self.magic_number)

        # Check sums of main space diagonals (4 in a cube)
        diag1_sum = sum(self.cube[i][i][i] for i in range(self.size))
        diag2_sum = sum(self.cube[i][i][self.size - i - 1] for i in range(self.size))
        diag3_sum = sum(self.cube[i][self.size - i - 1][i] for i in range(self.size))
        diag4_sum = sum(self.cube[self.size - i - 1][i][i] for i in range(self.size))
        
        score += abs(diag1_sum - self.magic_number)
        score += abs(diag2_sum - self.magic_number)
        score += abs(diag3_sum - self.magic_number)
        score += abs(diag4_sum - self.magic_number)

        # Check sums of 2D slice diagonals in each dimension
        for i in range(self.size):
            # XY-plane diagonals
            diag1_xy = sum(self.cube[i][j][j] for j in range(self.size))
            diag2_xy = sum(self.cube[i][j][self.size - j - 1] for j in range(self.size))
            score += abs(diag1_xy - self.magic_number)
            score += abs(diag2_xy - self.magic_number)

            # YZ-plane diagonals
            diag1_yz = sum(self.cube[j][i][j] for j in range(self.size))
            diag2_yz = sum(self.cube[self.size - j - 1][i][j] for j in range(self.size))
            score += abs(diag1_yz - self.magic_number)
            score += abs(diag2_yz - self.magic_number)

            # XZ-plane diagonals
            diag1_xz = sum(self.cube[j][j][i] for j in range(self.size))
            diag2_xz = sum(self.cube[j][self.size - j - 1][i] for j in range(self.size))
            score += abs(diag1_xz - self.magic_number)
            score += abs(diag2_xz - self.magic_number)

        return score
