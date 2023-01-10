from scipy.linalg import polar
import numpy as np
a = np.array([[4, 1, 0, -1], [0, 3, 0, 1], [0, 0, 4, 0], [1, 0, 0, 5]])

u, p = polar(a)
print(u)
print(p)