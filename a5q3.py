#solve linear equations taken from user input(multiple variables) using numpy, arrays and cmath modules
import numpy as np
import cmath
n = int(input("Enter the number of variables: "))
print("Enter the coefficients of the variables in a 2D array format. For example: [[1, 2], [3, 4]]")
a = np.array(eval(input()))
print("Enter the constants in a 1D array format. For example: [5, 6]")
b = np.array(eval(input()))
x = np.linalg.solve(a, b)
print(x)