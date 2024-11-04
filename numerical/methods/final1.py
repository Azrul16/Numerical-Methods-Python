import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
  return np.exp(-x) * (3.2 * np.sin(x) - 0.5 * np.cos(x))

# Bisection method implementation
def bisection_method(f, a, b, Estep, Eabs):
  if f(a) * f(b) >= 0:
    print("Bisection method fails.")
    return None
  a_n = a
  b_n = b
  results = []
  while (b_n - a_n) / 2.0 > Estep:
    midpoint = (a_n + b_n) / 2.0
    results.append((a_n, b_n, midpoint, f(midpoint)))
    if f(midpoint) == 0 or (b_n - a_n) / 2.0 < Eabs:
      return midpoint, results
    elif f(a_n) * f(midpoint) < 0:
      b_n = midpoint
    else:
      a_n = midpoint
  results.append((a_n, b_n, midpoint, f(midpoint)))
  return (a_n + b_n) / 2.0, results

# Parameters
a = 3
b = 4
Estep = 0.001
Eabs = 0.001

# Find the root
root, results = bisection_method(f, a, b, Estep, Eabs)

# Print results in tabular format
print("a_n\t\tb_n\t\tmidpoint\tf(midpoint)")
for result in results:
  print(f"{result[0]:.6f}\t{result[1]:.6f}\t{result[2]:.6f}\t{result[3]:.6f}")

# Plot the function and the root
x = np.linspace(a, b, 400)
y = f(x)
plt.plot(x, y, label='f(x)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(root, color='r', linestyle='--', label=f'Root at x={root:.6f}')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Bisection Method')
plt.grid(True)
plt.show()