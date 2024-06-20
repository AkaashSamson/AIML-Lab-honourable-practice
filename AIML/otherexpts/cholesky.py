# Corrected code snippet for Cholesky decomposition
import numpy as np
import scipy.linalg  # Ensure correct import
import pprint

# Define a symmetric, positive definite matrix
mat = np.array([[6, 15, 55, 225], [15, 55, 225, 979], [55, 225, 979, 4433], [225, 979, 4433, 20349]])

# Pretty print the original matrix
pprint.pprint(mat)

# Perform Cholesky decomposition
L = scipy.linalg.cholesky(mat, lower=True)  # Use scipy.linalg directly

# Pretty print the result of the Cholesky decomposition
pprint.pprint(L)