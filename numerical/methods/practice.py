import matplotlib.pyplot as plt
from tabulate import tabulate

def bisection(func, a, b, tol=1e-6, max_iter=100):
    iterations = []
    a_values = []
    b_values = []
    c_values = []
    f_a_values = []
    f_b_values = []
    f_c_values = []

    # Check if the function changes sign over the interval
    if func(a) * func(b) >= 0:
        raise ValueError("Function does not change sign over the interval [a, b]")

    # Bisection method loop
    for i in range(max_iter):
        c = (a + b) / 2
        iterations.append(i)
        a_values.append(a)
        b_values.append(b)
        c_values.append(c)

        f_a = func(a)
        f_b = func(b)
        f_c = func(c)

        f_a_values.append(f_a)
        f_b_values.append(f_b)
        f_c_values.append(f_c)

        # Check for root or tolerance
        if f_c == 0 or abs(b - a) / 2 < tol:
            break
        elif f_a * f_c < 0:
            b = c
        else:
            a = c

    # Prepare table of results
    results = list(zip(iterations, a_values, b_values, c_values, f_a_values, f_b_values, f_c_values))
    table = tabulate(results, headers=["Iteration", "a", "b", "c (mid value)", "f(a)", "f(b)", "f(c)"],
                     tablefmt="pretty")

    # Plot function and root approximation
    x = [i / 10 for i in range(int(10 * min(a, b)) - 1, int(10 * max(a, b)) + 2)]
    y = [func(xi) for xi in x]

    plt.plot(x, y, label='f(x)')
    plt.axhline(0, color='red', linestyle='--', label='y=0')
    plt.axvline(c, color='green', linestyle='--', label='Root Approximation')
    plt.title('Bisection Method')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Print the table
    print(table)
    return c

# Function to get the function from the user
def get_function():
    func_input = input("Enter the function in terms of x (e.g., x ** 2 - 3): ")
    return lambda x: eval(func_input)

# Main function
if __name__ == "__main__":
    func = get_function()
    a = float(input("Enter the lower bound (a): "))
    b = float(input("Enter the upper bound (b): "))
    tol = float(input("Enter the tolerance (default is 1e-6): ") or 1e-6)
    max_iter = int(input("Enter the maximum number of iterations (default is 100): ") or 100)
    
    try:
        root = bisection(func, a, b, tol, max_iter)
        print(f"The approximate root is: {root:.6f}")
    except ValueError as e:
        print(e)
