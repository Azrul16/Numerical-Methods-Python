import numpy as np

A=np.array([
    [1.00,2.00,3.00],
    [2.00,4.00,5.00],
    [3.00,5.00,6.00]
])

b=np.array([11.00,21.00,27.00])
n=3

for i in range(n):
    max_row = np.argmax(abs(A[i:, i])) + i
    if i != max_row:
        A[[i, max_row]] = A[[max_row, i]]
        b[[i, max_row]] = b[[max_row, i]]
    
    for j in range(i+1, n):
        factor = A[j, i] / A[i, i]
        A[j] = A[j] - factor * A[i]
        b[j] = b[j] - factor * b[i]

x = np.zeros(n)
for i in range(n-1, -1, -1):
    x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]

for i in range(n):
    print(f"x[{i+1}]= {x[i]}")