import numpy as np # type: ignore

# Coefficients matrix
A = np.array([
    [1, 1, 1],
    [0.02, 0.03, 0.06],
    [1, 1, -1]
])

# Constants vector
b = np.array([8500, 380, 0])

# Calculate determinant of A
det_A = np.linalg.det(A)

# Check if the system is solvable
if det_A == 0:
    print("The system has no unique solution.")
else:
    # Calculate determinants of modified matrices
    A_x = A.copy()
    A_x[:, 0] = b
    det_A_x = np.linalg.det(A_x)
    
    A_y = A.copy()
    A_y[:, 1] = b
    det_A_y = np.linalg.det(A_y)
    
    A_z = A.copy()
    A_z[:, 2] = b
    det_A_z = np.linalg.det(A_z)
    
    # Calculate solutions using Cramer's rule
    x = det_A_x / det_A
    y = det_A_y / det_A
    z = det_A_z / det_A
    
    print("Solution:")
    print(f"x (amount invested at 2%) = {x}")
    print(f"y (amount invested at 3%) = {y}")
    print(f"z (amount invested at 6%) = {z}")
