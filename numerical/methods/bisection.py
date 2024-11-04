import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def f(x):
    # Define the function whose root we want to find
    return x * x - 3

def bisection_method(a, b, tol=1e-6, max_iterations=100):

    if f(a) * f(b) >= 0:
        print("Bisection method fails. f(a) and f(b) should have opposite signs.")
        return None, 0, None, None

    iteration = 0
    midpoints = []  # To store midpoints for plotting
    data = []  # To store values of a, b, and c for each iteration

    while (b - a) / 2 > tol and iteration < max_iterations:
        # Calculate the midpoint
        c = (a + b) / 2
        midpoints.append(c)  # Store the midpoint
        data.append((iteration + 1, a, b, c, f(c)))  # Store iteration data for table

        # Check if we've found an exact root
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

        iteration += 1

    # Approximate root
    c = (a + b) / 2
    midpoints.append(c)  # Store the last midpoint
    data.append((iteration + 1, a, b, c, f(c)))  # Store final iteration data

    # Create a DataFrame from the data collected
    df = pd.DataFrame(data, columns=["Iteration", "a", "b", "c (midpoint)", "f(c)"])

    return c, iteration, midpoints, df

def plot_function(a, b, root, midpoints):
    # Generate x values
    x = np.linspace(a - 1, b + 1, 400)
    y = f(x)

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='f(x) = x^2 - 3', color='blue')
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(root, color='red', lw=0.5, ls='--', label=f'Root: {root:.4f}')
    
    # Plot midpoints
    for midpoint in midpoints:
        plt.plot(midpoint, f(midpoint), 'ro')  # Mark midpoints in red

    plt.title('Bisection Method Visualization')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.ylim(min(y), max(y))
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    # Define the interval [a, b] where the root lies
    a = float(input("Enter the lowest value: "))
    b = float(input("Enter the highest value: "))

    # Call the bisection method
    root, iterations, midpoints, table = bisection_method(a, b, tol=1e-6)

    if root is not None:
        print(f"Approximate root: {root}")
        print(f"Number of iterations: {iterations}")
        
        # Display the table
        print("\nTable of iterations:")
        print(table)

        # Plot the function and midpoints
        plot_function(a, b, root, midpoints)
    else:
        print("No root found in the given interval.")
