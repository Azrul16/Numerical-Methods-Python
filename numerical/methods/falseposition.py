def false_position(f, a, b, tol=1e-6, max_iterations=100):
    if f(a) * f(b) >= 0:
        print("False Position method fails. f(a) and f(b) should have opposite signs.")
        return None, 0

    iteration = 0
    c = a  

    while iteration < max_iterations:
        c = b - (f(b) * (b - a)) / (f(b) - f(a))

        if abs(f(c)) < tol:
            return c, iteration

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        iteration += 1

    return c, iteration

# Example usage
if __name__ == "__main__":
    # Define the function for which we are finding the root
    def f(x):
        return x**2 - 3  # Example: Find the root of x^2 - 3

    # Define the interval [a, b]
    a = 1
    b = 2

    # Call the false position method
    root, iterations = false_position(f, a, b, tol=1e-6)

    if root is not None:
        print(f"Approximate root: {root}")
        print(f"Number of iterations: {iterations}")
    else:
        print("No root found in the given interval.")
