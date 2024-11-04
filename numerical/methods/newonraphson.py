import numpy as np
from tabulate import tabulate

def f(x):
    # Define the function whose root you want to find
    return x**2 - 3

def f_prime(x):
    # Define the derivative of the function
    return 2 * x

def newton_raphson(x0, tol=1e-6, max_iter=100):
    x = x0
    iterations_data = []  # List to store data for each iteration

    for i in range(max_iter):
        f_x = f(x)
        f_prime_x = f_prime(x)

        if f_prime_x == 0:
            print("Zero derivative. No solution found.")
            return None, i

        # Update x using Newton-Raphson formula
        x_new = x - f_x / f_prime_x

        # Append the data for the current iteration
        iterations_data.append([i + 1, x, f_x, f_prime_x, x_new])

        # Check for convergence
        if abs(x_new - x) < tol:
            # Print table
            print(tabulate(iterations_data, headers=["Iteration", "x", "f(x)", "f'(x)", "Next x"], tablefmt="pretty"))
            return x_new, i + 1

        x = x_new

    # Print table if max iterations reached
    print("Exceeded maximum iterations. No solution found.")
    print(tabulate(iterations_data, headers=["Iteration", "x", "f(x)", "f'(x)", "Next x"], tablefmt="pretty"))
    return x, max_iter

if __name__ == "__main__":
    # Initial guess
    x0 = float(input("Enter the initial guess: "))
    
    # Call the Newton-Raphson method
    root, iterations = newton_raphson(x0)

    if root is not None:
        print(f"The approximate root is: {root:.6f}")
        print(f"Total iterations: {iterations}")
    else:
        print("No root found.")
