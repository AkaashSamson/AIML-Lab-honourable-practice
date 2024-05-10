#solve linear equations with 3 variables using numpy, arrays and cmath modules
import numpy as np
import cmath
a = np.array([[2, 3, 4], [1, 2, 3], [4, 5, 7]])  # Changed last element of the third row coz previously 
b = np.array([[2], [3], [4]])                    # the matrix was singular and had no solution
x = np.linalg.solve(a, b)
print(x)
print(np.allclose(np.dot(a, x), b))