import numpy as np
import matplotlib.pyplot as plt


x_arr = np.linspace(0, 2 * np.pi, 100)

x = 16 * ( np.sin(x_arr) ** 3 )
y = 13 * np.cos(x_arr) - 5* np.cos(2*x_arr) - 2 * np.cos(3*x_arr) - np.cos(4*x_arr)
fig, ax = plt.subplots()
ax.plot(x, y, color='red', alpha=1.00)
ax.fill_between(x, y, 0, color='red', alpha=1)

plt.show()