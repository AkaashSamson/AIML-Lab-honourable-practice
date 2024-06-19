#taking linear equaton from user and solving it using numpy and cmath
import numpy as np
import cmath
#n = int(input("Enter the number of variables: "))   
print("Enter the coefficient matrix: ")
a = np.array(eval(input()))   #eval() function evaluates the string like a python expression
print("Enter the constant matrix: ")
b = np.array(eval(input()))
x = np.linalg.solve(a, b)
[print(f"x{i+1}: {int(x[i])}") for i in range(len(x))]

      