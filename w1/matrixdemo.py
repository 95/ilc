import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Matrix Addition
C = A + B
print(C)

# Matrix Subtraction
D = A - B
print(D)

# Matrix Multiplication (element-wise)
E = A * B
print(E)

# (dot product)
F = A @ B
print(F)

# Transpose
G = A.T
print(G)
