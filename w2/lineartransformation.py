import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1, 2],
              [3, 4],
              [5, 6]])

T = np.array([[2, 1],
              [1, 2]])

A_transformed = np.dot(A, T)

plt.figure()
plt.plot(A[:, 0], A[:, 1], 'x', label='Original')
plt.plot(A_transformed[:, 0], A_transformed[:, 1], 'x', label='Transformed')

plt.xlim(-2, 15)
plt.ylim(-2, 15)
plt.grid(True)
plt.legend()
plt.show()
