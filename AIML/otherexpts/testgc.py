import numpy as np
import scipy.linalg
import pprint

# Generate a random matrix

# Generate random integer inputs for matrix A
def new_func():
    A = np.random.randint(9, size=(4, 4))

# Construct a symmetric positive definite matrix
    mat = np.dot(A, A.T)

# Pretty print the generated matrix
    pprint.pprint(mat)

# Perform Cholesky decomposition
    L = scipy.linalg.cholesky(mat, lower=True)

# Pretty print the result of the Cholesky decomposition
    pprint.pprint(L)
    pprint.pprint(f"LT: {L.T}")
    pprint.pprint(f"LT x L: {L.dot(L.T)}")
new_func()