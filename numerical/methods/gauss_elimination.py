import numpy as np

# Input number of variables
n = int(input("Enter the number of variables: "))

# Initialize coefficient matrix and constants vector
A = np.zeros((n, n))
b = np.zeros(n)

# Input coefficients matrix
print("Enter the coefficients of the matrix row by row:")
for i in range(n):
    row = input(f"Row {i+1}: ").split()
    A[i] = [float(num) for num in row]

# Input constants vector
print("Enter the constants vector:")
b = np.array([float(input(f"b[{i+1}]: ")) for i in range(n)])

# Perform Gaussian elimination with partial pivoting
for i in range(n):
    # Partial pivoting
    max_row = np.argmax(abs(A[i:, i])) + i
    if i != max_row:
        A[[i, max_row]] = A[[max_row, i]]
        b[[i, max_row]] = b[[max_row, i]]
    
    # Make the diagonal 1 and eliminate below
    for j in range(i+1, n):
        factor = A[j, i] / A[i, i]
        A[j] = A[j] - factor * A[i]
        b[j] = b[j] - factor * b[i]

# Back substitution
x = np.zeros(n)
for i in range(n-1, -1, -1):
    x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]

print("Solution:")
for i in range(n):
    print(f"x{i+1} = {x[i]}")
