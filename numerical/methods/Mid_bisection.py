import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import bisect
from scipy.integrate import quad
from math import exp, sin, cos, log

# Problem (a): Define the function and find the root using Bisection Method


def f(x):
    return exp(-x) * ((3.2 * sin(x)) - 0.5 * cos(x))


# Bisection method parameters
a, b = 3, 4  # Interval [3, 4]
tolerance = 0.001  # E_step and E_abs

# Find the root
root = bisect(f, a, b, xtol=tolerance)

# Generate values for plotting
x_values = np.linspace(3, 4, 100)
y_values = [f(x) for x in x_values]

# Plot the function and root
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label="f(x) = e^(-x)((3.2 sin(x)) - 0.5 cos(x))")
plt.axhline(0, color='gray', linestyle='--')
plt.axvline(root, color='red', linestyle='--', label=f"Root at x ≈ {root:.4f}")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Bisection Method: Root of f(x) on [3, 4]")
plt.legend()
plt.grid(True)
plt.show()

root
