import numpy as np

# Input number of variables
n = int(input("Enter the number of variables: "))

# Initialize the augmented matrix
augmented_matrix = np.zeros((n, n + 1))

# Input coefficients and constants for the augmented matrix
print("Enter the augmented matrix row by row (include the constant term at the end of each row):")
for i in range(n):
    row = input(f"Row {i+1}: ").split()
    augmented_matrix[i] = [float(num) for num in row]

# Gauss-Jordan elimination
for i in range(n):
    # Make the diagonal contain all 1's
    augmented_matrix[i] = augmented_matrix[i] / augmented_matrix[i, i]
    
    # Make the other entries in the current column 0
    for j in range(n):
        if i != j:
            factor = augmented_matrix[j, i]
            augmented_matrix[j] = augmented_matrix[j] - factor * augmented_matrix[i]

# Solution
x = augmented_matrix[:, -1]

print("Solution:")
for i in range(n):
    print(f"x{i+1} = {x[i]}")
