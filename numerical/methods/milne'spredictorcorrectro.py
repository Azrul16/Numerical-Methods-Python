import numpy as np # type: ignore

def f(x, y):
    return x + y  # Example equation: dy/dx = x + y

# Use the Runge-Kutta method to compute the first four points
def runge_kutta_step(x, y, h):
    k1 = h * f(x, y)
    k2 = h * f(x + h / 2, y + k1 / 2)
    k3 = h * f(x + h / 2, y + k2 / 2)
    k4 = h * f(x + h, y + k3)
    return y + (k1 + 2 * k2 + 2 * k3 + k4) / 6

# Milne's Predictor-Corrector Method
def milne_method(x0, y0, h, steps):
    # Initialize arrays to store x and y values
    x = np.zeros(steps)
    y = np.zeros(steps)
    x[0], y[0] = x0, y0

    # Compute the first three points using Runge-Kutta
    for i in range(1, 4):
        x[i] = x[i - 1] + h
        y[i] = runge_kutta_step(x[i - 1], y[i - 1], h)

    # Apply Milne's Predictor-Corrector for the rest of the points
    for i in range(3, steps - 1):
        # Predictor Step
        y_pred = y[i - 3] + (4 * h / 3) * (2 * f(x[i], y[i]) - f(x[i - 1], y[i - 1]) + 2 * f(x[i - 2], y[i - 2]))
        
        # Calculate x[i+1] for reference
        x[i + 1] = x[i] + h

        # Corrector Step
        y_corr = y[i - 1] + (h / 3) * (f(x[i + 1], y_pred) + 4 * f(x[i], y[i]) + f(x[i - 1], y[i - 1]))

        # Store the corrected value
        y[i + 1] = y_corr

    return x, y

# Example usage
if __name__ == "__main__":
    # Initial conditions and parameters
    x0 = 0
    y0 = 1
    h = 0.1  # Step size
    steps = 10  # Number of steps

    # Compute solution using Milne's Method
    x_values, y_values = milne_method(x0, y0, h, steps)

    # Display results
    for i in range(steps):
        print(f"x = {x_values[i]:.2f}, y = {y_values[i]:.6f}")
