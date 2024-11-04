import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

# Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 1.3, 3.75, 2.25])

# Means
x_mean = np.mean(x)
y_mean = np.mean(y)

# Summations
x_sum = np.sum(x)
y_sum = np.sum(y)
xy_sum = np.sum(x * y)
n = np.size(x)

# Calculating slope (a1) and intercept (a0)
a1 = ((n * xy_sum) - (x_sum * y_sum)) / ((n * np.sum(x**2)) - (x_sum**2))
a0 = y_mean - (a1 * x_mean)

print("Slope (a1):", a1)
print("Intercept (a0):", a0)

# Plotting
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', label='Data Points')  # Scatter plot of the data points

# Regression line
y_pred = a1 * x + a0  # y values predicted by the regression line
plt.plot(x, y_pred, color='red', label=f'Regression Line: y = {a1:.2f}x + {a0:.2f}')

# Adding titles and labels
plt.title('Linear Regression')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()

# Display the plot
plt.show()
