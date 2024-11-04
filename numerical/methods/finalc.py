import numpy as np

def f(x):
    return x**4 - 0.165 * x**2 + 3.993e-2


def falseposition(a, b, tol=1e-6, max_it=100):
    if f(a) * f(b) >= 0:
        print("False position method fails. f(a) and f(b) should have opposite signs.")
        return None, 0, None, None
    
    loop=4
    errors = []
    c_old = a  # Initial guess (could be b as well, this is just a placeholder)
    
    for iteration in range(loop):
        c_new = b - (f(b) * (b - a)) / (f(b) - f(a))
        error = abs(c_new - c_old)
        errors.append((c_new, error))
        
        print(f"Iteration {iteration+1}: c = {c_new}, Error = {error}")
        
        if error < tol:
            return c_new, iteration + 1, errors
        
        if f(a) * f(c_new) < 0:
            b = c_new
        else:
            a = c_new
        
        c_old = c_new

    return c_new, errors
        