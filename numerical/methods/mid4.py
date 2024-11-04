import numpy as np

# Given values
g = 9.81  # acceleration due to gravity in m/s^2
m1 = 2.0  # mass 1 in kg
m2 = 3.0  # mass 2 in kg
m3 = 2.5  # mass 3 in kg
k = 10.0  # spring constant in kg/s

# Coefficient matrix
A4 = np.array([[k, -k, 0],
         [-k, 2*k, -k],
         [0, -k, k]])

# Constants matrix
B4 = np.array([m1 * g, m2 * g, m3 * g])

# Augmented matrix
augmented_matrix4 = np.hstack((A4, B4.reshape(-1, 1)))

# Function to perform Gaussian elimination
def gaussian_elimination(matrix):
  rows, cols = matrix.shape
  for i in range(rows):
    # Make the diagonal contain all 1's
    matrix[i] = matrix[i] / matrix[i, i]
    for j in range(i + 1, rows):
      matrix[j] = matrix[j] - matrix[j, i] * matrix[i]

  # Back substitution
  x = np.zeros(rows)
  for i in range(rows - 1, -1, -1):
    x[i] = matrix[i, -1] - np.sum(matrix[i, i + 1:rows] * x[i + 1:rows])

  return x

# Perform Gaussian elimination
solution4 = gaussian_elimination(augmented_matrix4.copy())

# Extract the solutions
x1, x2, x3 = solution4
print(f"Displacements:")
print(f"x1: {x1} m")
print(f"x2: {x2} m")
print(f"x3: {x3} m")